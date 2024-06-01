
class __:

    import pathlib as path
    import shutil
    import json
    import os
    from multiprocessing import cpu_count
    from concurrent.futures import ThreadPoolExecutor

    from ._exporter import Exporter
    from .._icon_properties import IconProperties

    from icon_theme_builder.lib import util

    from svg_tools import SvgTools

# *****************************************************************************

class FontExporter (__.Exporter):

    # :: PRIVATE ATTRIBUTES :: #

    _font_id : str

    _current_glyph : int
    _added_glyph   : int

    # str: filepath, [int: glyph code, IconProperties]
    _glyph_lut : dict[str, tuple[int, __.IconProperties]]

    START_GLYPH = 0xE000

    _copy_dir : __.path.Path
    _svg_dir  : __.path.Path


    # :: CONSTRUCTOR :: #

    def __init__(self) -> None:
        super().__init__()

        self._font_id = __.util.generate_uid(5)

        self._current_glyph = self.START_GLYPH
        self._added_glyph   = self.START_GLYPH
        self._glyph_lut     = {}

        self._copy_dir = __.path.Path(f'/tmp/glyph_fonts/{self._font_id}')

        if (self._copy_dir.exists()):
            __.shutil.rmtree(self._copy_dir)
        self._copy_dir.mkdir(parents=True, exist_ok=True)

        self._svg_dir = self._copy_dir / 'svg'
        self._svg_dir.mkdir(parents=True, exist_ok=True)

        return


    # :: PUBLIC METHODS :: #

    def add_icon(self, icon_fp: str, properties: __.IconProperties) -> None:

        # Check if icon was already added based on filepath so we can dedupe and save space a bit
        if (icon_fp in self._glyph_lut and properties == self._glyph_lut[icon_fp][1]):
            self._added_glyph = self._glyph_lut[icon_fp][0]
        # New icon
        else:
            self._added_glyph = self._current_glyph
            self._current_glyph += 1
            formatted_glyph = self.get_glyph_code()

            icon_file = self._fp(icon_fp)
            if not icon_file.exists: raise RuntimeError("File does not exist.")
            if icon_file.suffix != ".svg": raise RuntimeError("File must be SVG.")

            # Append unicode to filepath and copy file to temp dir
            temp_file_svg = (self._svg_dir / f'u{formatted_glyph}.svg')
            __.shutil.copy(
                icon_file,
                temp_file_svg,
            )

            if (properties.scale != 1.0):
                (__.SvgTools.open(str(temp_file_svg))
                            .scale({'scale': properties.scale})
                            .write(str(temp_file_svg)))

        return


    def get_font_id(self) -> str:
        return self._font_id


    def get_glyph_code(self) -> str:
        """Gets the glyph code counter value of the added icon. You should call method this after using `add_icon()`."""
        return f'{self._added_glyph:x}'.upper() # Format as HEX (no leading '0x')


    def consolidate(self, dist_dir: __.path.Path):

        # svg2ttf (used by svgtofont) does not support strokes and also does not support paths using the 'evenodd'
        # fill-rule. We need to preprocess fonts to ensure svgtofont converts them properly
        def process_svg(svg: __.path.Path) -> None:
            # Use Inkscape CLI to convert strokes to fill-paths
            with open(svg, 'r') as svg_f:
                if (svg_f.read().find('stroke') >= 0):
                    cmd = f'inkscape --actions="select-all:all;object-stroke-to-path" --export-filename="{svg}" "{svg}"'
                    print(cmd)
                    with __.os.popen(cmd) as inkscape_p:
                        inkscape_p.read()

            # Use picosvg to simplify and also take care of converting paths that use the 'evenodd' fill-rule to normal
            # fill paths
            # NOTE: picosvg does not support style tags so convert them to inline style properties
            (__.SvgTools.open(str(svg))
                        .convert_style_to_inline()
                        .write(str(svg)))

            cmd = f'picosvg "{svg}" --output_file="{svg}"'
            print(cmd)
            with __.os.popen(cmd) as picosvg_p:
                picosvg_p.read()

        with __.ThreadPoolExecutor(__.cpu_count()) as pool:
            pool.map(process_svg, self._svg_dir.glob('*.svg'))

        # Minify svgs for smaller font sizes
        svgo_config_fp = __.path.Path(__file__).parent / "svgo_config.js"
        cmd = f'svgo --multipass -f {self._svg_dir} -o {self._svg_dir} --config {svgo_config_fp}'
        print(cmd)
        with __.os.popen(cmd) as svgo_p:
            svgo_p.read()

        svgtofont_config = {
            "startUnicode": f'0x{self.START_GLYPH:x}',
        }
        with open(self._copy_dir / ".svgtofontrc", 'w') as f:
            __.json.dump(svgtofont_config, f, separators=(',', ':'))

        cmd = f'cd "{self._copy_dir}" && svgtofont --sources "{self._svg_dir}" --output "{self._copy_dir}/build" --fontName {self._font_id}'
        print(cmd)
        with __.os.popen(cmd) as svgtofont_p:
            svgtofont_p.read()

        # TODO: Check if generation was succesfull

        # svgtofont places generated files in ./build
        __.shutil.copy(
            str(self._copy_dir / "build" / f'{self._font_id}.woff2'),
            str(dist_dir / f'{self._font_id}.woff2'),
        )

        __.shutil.rmtree(self._copy_dir)

        return
