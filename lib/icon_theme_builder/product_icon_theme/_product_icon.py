from __future__ import annotations as _annotations

class __:

    import dataclasses
    import typing as t

    from icon_theme_builder.lib import (
        exporter,
        IconTheme,
        ColorTheme,
    )

    from ._icon import ProductIconThemeIcon

# *****************************************************************************

@__.dataclasses.dataclass
class ProductIconDefinition:
    file : str

# *****************************************************************************

class ProductIcon (__.ProductIconThemeIcon):

    # :: TYPES :: #

    _definition_t = str | ProductIconDefinition | dict[__.ColorTheme, ProductIconDefinition]


    # :: PRIVATE ATTRIBUTES :: #

    _definitionss : dict[__.ColorTheme, ProductIconDefinition]
    _icon_ids : __.t.List[str]


    # :: CONSTRUCTOR :: #

    def __init__(self, definition: _definition_t, icon_ids: __.t.List[str]):
        super().__init__()

        match definition:
            case str():
                definition = __.t.cast(str, definition)
                self._definitions = {__.ColorTheme.DEFAULT_DARK: ProductIconDefinition(definition)}
            case ProductIconDefinition():
                definition = __.t.cast(ProductIconDefinition, definition)
                self._definitions = {__.ColorTheme.DEFAULT_DARK: definition}
            case _:
                definition = __.t.cast(dict[__.ColorTheme, ProductIconDefinition], definition)
                self._definitions = definition

        self._icon_ids = icon_ids

        return


    def add_to_theme(self, theme: __.IconTheme, color_theme: __.ColorTheme):

        definition = self._definitions.get(color_theme, None)
        reuse_default = definition is None

        if (reuse_default):
            definition = self._definitions.get(__.ColorTheme.DEFAULT_DARK, None)
            if (definition is None):
                return

        json = {
            "iconDefinitions": {},
        }

        exporter = theme.get_exporters().get(self._get_exporter_klass(), None)
        if (exporter is None):
            raise Exception("Too lazy to build right now")

        match exporter:
            case __.exporter.FontExporter() | __.exporter.ColrFontExporter():
                glyph_code = exporter.get_glyph_code()
                exporter.add_icon(definition.file, self._get_properties())
                for icon_id in self._icon_ids:
                    json["iconDefinitions"][icon_id] = {
                        "fontCharacter": fr'\{glyph_code}',
                        "fontId": exporter.get_font_id(),
                    }
            case _:
                raise Exception("Too lazy to build right now")

        theme.add_to_theme_json(json, reuse_default)

        return
