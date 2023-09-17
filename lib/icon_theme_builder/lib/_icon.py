from __future__ import annotations as _annotations

class __:

    import abc
    import typing as t

    from . import exporter
    from ._icon_theme      import IconTheme
    from ._color_theme     import ColorTheme
    from ._icon_properties import IconProperties

# *****************************************************************************

class Icon (__.abc.ABC, object):

    # :: PROTECTED ATTRIBUTES :: #

    _base_path : str


    # :: PRIVATE ATTRIBUTES :: #

    _exporter_klass : __.t.Type[__.exporter.Exporter] | None
    _properties : __.IconProperties

    # :: CONSTRUCTOR :: #

    def __init__(self) -> None:
        self._exporter_klass = None
        self._base_path = ""
        self._properties = __.IconProperties()
        return


    # :: PUBLIC METHODS :: #

    def as_glyph(self) -> 'Icon':
        self._exporter_klass = __.exporter.FontExporter
        return self


    def as_glyf_colr_glyph(self) -> 'Icon':
        """Enables colored export (using COLRv1)"""
        self._exporter_klass = __.exporter.GlyfColrFontExporter
        return self


    def as_cbdt_colr_glyph(self) -> 'Icon':
        """Enables colored export (using COLRv1)"""
        self._exporter_klass = __.exporter.CbdtColrFontExporter
        return self

    def scaled(self, scale: float) -> 'Icon':
        self._properties.scale = scale
        return self


    @__.abc.abstractmethod
    def add_to_theme(self, theme: __.IconTheme, color_theme: __.ColorTheme) -> bool:
        ...


    # :: PROTECTED METHODS :: #

    def _get_exporter_klass(self) -> __.t.Type[__.exporter.Exporter]:
        if (self._exporter_klass is None):
            raise RuntimeError("Exporter class not set!")
        return self._exporter_klass


    def _get_properties(self) -> __.IconProperties:
        return self._properties
