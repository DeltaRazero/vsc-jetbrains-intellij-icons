
class __:

    import pathlib as path
    import shutil
    import json
    import os

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

    def add_icon(self, icon_fp: str, properties: __.IconProperties) -> str:
        """Returns glyph codepoint."""
        glyph = f'{self._current_glyph:x}'.upper() # Format as HEX (no leading '0x')
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

        return fr'\{glyph}'


    def get_font_id(self) -> str:
        return self._font_id


    def consolidate(self, dist_dir: __.path.Path):

        # We need to do some pre-processing to ensure svgtofont works properly
        for svg in self._svg_dir.glob('*.svg'):
            # svg2ttf used by svgtofont has problems with strokes, so convert strokes to fill paths
            cmd = f'cd / && bash /usr/src/myapp/include/svg-stroke-to-path/svg-stroke-to-path all {svg}'
            with __.os.popen(cmd) as stroke_path_fixer_p:
                stroke_path_fixer_p.read()

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
