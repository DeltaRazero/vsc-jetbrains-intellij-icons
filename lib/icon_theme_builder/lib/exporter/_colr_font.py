
class __:

    import abc
    import pathlib as path
    import shutil
    import os
    import enum
    from multiprocessing import cpu_count
    from concurrent.futures import ThreadPoolExecutor

    from ._font import FontExporter

    import svg_tools

# *****************************************************************************

class ColrFontType (__.enum.Enum):
    GLYF = __.enum.auto()
    CBDT = __.enum.auto()


class ColrFontExporter (__.FontExporter, __.abc.ABC):

    # :: PRIVATE ATTRIBUTES :: #

    _nanoemoji_args : str
    _colr_font_type : ColrFontType


    # :: CONSTRUCTOR :: #

    def __init__(self, colr_font_type: ColrFontType) -> None:
        super().__init__()
        self._nanoemoji_args = ""
        self._colr_font_type = colr_font_type
        return


    # :: PUBLIC METHODS :: #

    def add_nanoemoji_args(self, args: str):
        self._nanoemoji_args = f"{args} "
        return


    def consolidate(self, dist_dir: __.path.Path):

        # Picosvg (used by nanoemoji in its backend) does not support style tags so convert them to inline style
        # properties
        def process_svg(svg: __.path.Path) -> None:
            __.svg_tools.SvgInlineStyleConverter.convert(str(svg))
            __.svg_tools.SvgFrameAdder.convert(str(svg))

        with __.ThreadPoolExecutor(__.cpu_count()) as pool:
            pool.map(process_svg, self._svg_dir.glob('*.svg'))

        # We'll do an additional cleanup here to cut down size
        svgo_config_fp = __.path.Path(__file__).parent / "svgo_config.js"
        cmd = f'svgo --multipass -f {self._svg_dir} -o {self._svg_dir} --config {svgo_config_fp}'
        with __.os.popen(cmd) as svgo_p:
            svgo_p.read()

        svgs = [f'"{svg_fp}"' for svg_fp in sorted(self._svg_dir.glob('*.svg'))]
        colr_format = {
            ColrFontType.CBDT : "cbdt",
            ColrFontType.GLYF : "glyf_colr_1",
        }[self._colr_font_type]
        cmd = f'cd "{self._copy_dir}" && nanoemoji {self._nanoemoji_args} --color_format={colr_format} --clip_to_viewbox=false {" ".join(svgs)}'
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

# *****************************************************************************

class GlyfColrFontExporter (ColrFontExporter):
    def __init__(self) -> None:
        super().__init__(ColrFontType.GLYF)
        return

class CbdtColrFontExporter (ColrFontExporter):
    def __init__(self) -> None:
        super().__init__(ColrFontType.CBDT)
        return
