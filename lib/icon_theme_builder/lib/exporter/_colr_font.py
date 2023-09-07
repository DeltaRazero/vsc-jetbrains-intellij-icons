
class __:

    import pathlib as path
    import shutil
    import os

    from ._font import FontExporter

    from svg_inline_styles import SvgInlineStyleConverter

# *****************************************************************************

class ColrFontExporter (__.FontExporter):

    # :: PUBLIC ATTRIBUTES :: #

    _nanoemoji_args : str


    # :: CONSTRUCTOR :: #

    def __init__(self) -> None:
        super().__init__()
        self._nanoemoji_args = ""
        return


    # :: PUBLIC METHODS :: #

    def add_nanoemoji_args(self, args: str):
        self._nanoemoji_args = f"{args} "
        return


    def consolidate(self, dist_dir: __.path.Path):

        # Nanoemoji breaks because it uses PicoSVG and it cannot handle when <style> tag is used pretty much, so
        # convert the class style attributes to inline style attributes
        for svg in self._svg_dir.glob('*.svg'):
            __.SvgInlineStyleConverter.convert(str(svg))

        # We'll do an additional cleanup here to cut down size
        svgo_config_fp = __.path.Path(__file__).parent / "svgo_config.js"
        cmd = f'svgo --multipass -f {self._svg_dir} -o {self._svg_dir} --config {svgo_config_fp}'
        with __.os.popen(cmd) as svgo_p:
            svgo_p.read()

        svgs = [f'"{svg_fp}"' for svg_fp in sorted(self._svg_dir.glob('*.svg'))]
        cmd = f'cd "{self._copy_dir}" && nanoemoji {self._nanoemoji_args} --color_format=glyf_colr_1 --clip_to_viewbox=true --linegap=0 {" ".join(svgs)}'
        # cmd = f'cd "{self._copy_dir}" && nanoemoji {self._nanoemoji_args} --clip_to_viewbox false --linegap 0 --color_format cbdt --width 2 {" ".join(svgs)}'
        print(cmd)
        with __.os.popen(cmd) as nanoemoji_p:
            nanoemoji_p.read()

        # TODO: Check if generation was succesfull

        # nanoemoji places generated files in ./build
        ttf_file = self._copy_dir / "build" / "Font.ttf"
        cmd = f'woff2_compress "{ttf_file}"'
        with __.os.popen(cmd) as woff2_compress_p:
            woff2_compress_p.read()

        # TODO: Check if generation was succesfull

        __.shutil.copy(
            str(ttf_file.with_suffix(".woff2")),
            str(dist_dir / f'{self._font_id}.woff2'),
        )

        __.shutil.rmtree(self._copy_dir)

        return
