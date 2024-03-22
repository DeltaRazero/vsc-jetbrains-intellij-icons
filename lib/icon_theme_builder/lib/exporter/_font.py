
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

    import svg_tools

# *****************************************************************************

class FontExporter (__.Exporter):

    # :: PRIVATE ATTRIBUTES :: #

    _font_id : str

    _current_glyph : int

    START_GLYPH = 0xE000

    _copy_dir : __.path.Path
    _svg_dir  : __.path.Path


    # :: CONSTRUCTOR :: #

    def __init__(self) -> None:
        super().__init__()

        self._font_id = __.util.generate_uid(5)
        self._current_glyph = self.START_GLYPH
        self._copy_dir = __.path.Path(f'/tmp/glyph_fonts/{self._font_id}')

        if (self._copy_dir.exists()):
            __.shutil.rmtree(self._copy_dir)
        self._copy_dir.mkdir(parents=True, exist_ok=True)

        self._svg_dir = self._copy_dir / 'svg'
        self._svg_dir.mkdir(parents=True, exist_ok=True)

        return


    # :: PUBLIC METHODS :: #

    def add_icon(self, icon_fp: str, properties: __.IconProperties) -> None:
        """Returns glyph codepoint."""
        glyph = self.get_glyph_code()
        self._current_glyph += 1

        icon_file = self._fp(icon_fp)
        if not icon_file.exists: raise RuntimeError("File does not exist.")
        if icon_file.suffix != ".svg": raise RuntimeError("File must be SVG.")

        # Append unicode to filepath and copy file to temp dir
        temp_file_svg = (self._svg_dir / f'u{glyph}.svg')
        __.shutil.copy(
            icon_file,
            temp_file_svg,
        )

        __.svg_tools.SvgScaler.scale(str(temp_file_svg), properties.scale)

        return


    def get_font_id(self) -> str:
        return self._font_id


    def get_glyph_code(self) -> str:
        """Gets the current glyph code counter value. You should call method this before using `add_icon()`."""
        return f'{self._current_glyph:x}'.upper() # Format as HEX (no leading '0x')


    def consolidate(self, dist_dir: __.path.Path):

        # We need to do some pre-processing to ensure svgtofont works properly
        def process_svg(svg: __.path.Path) -> None:
            # svg2ttf used by svgtofont does not support strokes and the 'evenodd' fill-rule. We can use
            # Inkscape's CLI to convert strokes to fill-paths and fix paths that use the 'evenodd' fill-rule
            inkscape_actions = ''

            svg_str: str = None
            with open(svg, 'r') as svg_f:
                svg_str = svg_f.read()

            # Quick and dirty way to check what actions we should carry out
            if (svg_str.find('stroke') >= 0): inkscape_actions += ';object-stroke-to-path'
            if (svg_str.find('fill-rule="evenodd"') >= 0): inkscape_actions += ';path-break-apart;path-exclusion'

            del svg_str

            if (inkscape_actions):
                cmd = f'inkscape --actions="select-all:all{inkscape_actions}" --export-filename="{svg}" "{svg}"'
                with __.os.popen(cmd) as evenodd_fixer_p:
                    evenodd_fixer_p.read()

        with __.ThreadPoolExecutor(__.cpu_count()) as pool:
            pool.map(process_svg, self._svg_dir.glob('*.svg'))

        # Minify svgs for smaller font sizes
        svgo_config_fp = __.path.Path(__file__).parent / "svgo_config.js"
        cmd = f'svgo --multipass -f {self._svg_dir} -o {self._svg_dir} --config {svgo_config_fp}'
        with __.os.popen(cmd) as svgo_p:
            svgo_p.read()

        svgtofont_config = {
            "startUnicode": f'0x{self.START_GLYPH:x}',
            # "svgicons2svgfont": {
            #     "fontHeight": 1000, # TODO: Check if this even does anything?
            #     "round": 10e18 # TODO: Check if this even does anything?
            # },
            # "svgicons2svgfont.fontHeight": 1000,
            # "svgicons2svgfont.round": 10e18,
        }
        with open(self._copy_dir / ".svgtofontrc", 'w') as f:
            __.json.dump(svgtofont_config, f, separators=(',', ':'))

        cmd = f'cd "{self._copy_dir}" && svgtofont --sources "{self._svg_dir}" --output "{self._copy_dir}/build" --fontName {self._font_id}'
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
