
class __:
    import typing as t

from ._exporter  import Exporter
from ._font      import FontExporter
from ._colr_font import ColrFontExporter

ExportersType = dict[__.t.Type[Exporter], Exporter | None]
