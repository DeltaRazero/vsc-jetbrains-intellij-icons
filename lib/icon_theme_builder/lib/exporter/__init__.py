
class __:
    import typing as t

from ._exporter  import Exporter
from ._font      import FontExporter
from ._colr_font import (
    ColrFontType,
    ColrFontExporter,
    CbdtColrFontExporter,
    GlyfColrFontExporter,
)

ExportersType = dict[__.t.Type[Exporter], Exporter | None]
