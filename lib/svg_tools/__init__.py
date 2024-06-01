
class __:

    import io
    import xml.etree.ElementTree as ElementTree

    from ._svg_frame_adder import SvgFrameAdder
    from ._svg_inline_style_converter import SvgInlineStyleConverter
    from ._svg_scaler import SvgScaler


class SvgTools:

    _xml : __.ElementTree.ElementTree

    def __init__(self, xml: __.ElementTree.ElementTree):
        self._xml = xml
        __.ElementTree.register_namespace('', "http://www.w3.org/2000/svg")
        return


    # :: I/O :: #

    @staticmethod
    def load(data: str) -> 'SvgTools':
        xml = __.ElementTree.parse(__.io.StringIO(data))
        return SvgTools(xml)

    def dump(self) -> str:
        ss = __.io.StringIO()
        self._xml.write(ss)
        return ss.read()

    @staticmethod
    def open(fp: str) -> 'SvgTools':
        xml: __.ElementTree.ElementTree | None = None
        with open(fp, 'r') as f:
            xml = __.ElementTree.parse(f)
        if (not xml):
            raise RuntimeError("Not valid XML/SVG")
        return SvgTools(xml)

    def write(self, fp: str) -> None:
        self._xml.write(fp)
        return


    # :: ACTIONS :: #

    def add_frame(self) -> 'SvgTools':
        __.SvgFrameAdder.add_frame(self._xml)
        return self

    def convert_style_to_inline(self) -> 'SvgTools':
        __.SvgInlineStyleConverter.convert(self._xml)
        return self

    def scale(self, args: dict) -> 'SvgTools':
        __.SvgScaler.scale(self._xml, **args)
        return self
