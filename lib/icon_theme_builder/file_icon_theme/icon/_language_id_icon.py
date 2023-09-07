from __future__ import annotations as _annotations

class __:

    import dataclasses
    import typing as t

    from icon_theme_builder.lib import (
        exporter,
        IconTheme,
        ColorTheme,
    )

    from .. import (
        FileIconThemeIcon,
    )

# *****************************************************************************

@__.dataclasses.dataclass
class LanguageIdIconDefinition:
    language : str


class LanguageIdIcon (__.FileIconThemeIcon):

    # :: TYPES :: #

    _definition_t = str | LanguageIdIconDefinition | dict[__.ColorTheme, LanguageIdIconDefinition]


    # :: PRIVATE ATTRIBUTES :: #

    _definitions : dict[__.ColorTheme, LanguageIdIconDefinition]
    _language_ids : list[str]


    # :: CONSTRUCTOR :: #

    def __init__(self,
                 definition: _definition_t,
                 languages_ids: list[str],
                 icon_id: str | None=None,
    ):
        super().__init__(icon_id)

        match definition:
            case str():
                definition = __.t.cast(str, definition)
                self._definitions = {__.ColorTheme.DEFAULT_DARK: LanguageIdIconDefinition(definition)}
            case LanguageIdIconDefinition():
                definition = __.t.cast(LanguageIdIconDefinition, definition)
                self._definitions = {__.ColorTheme.DEFAULT_DARK: definition}
            case _:
                definition = __.t.cast(dict[__.ColorTheme, LanguageIdIconDefinition], definition)
                self._definitions = definition

        self._language_ids = languages_ids

        return


    def add_to_theme(self, theme: __.IconTheme, color_theme: __.ColorTheme):
        json_root  = {
            "iconDefinitions": {}
        }

        definition = self._definitions.get(color_theme, None)
        if (definition is None):
            return

        json = {
            "languageIds": {},
        }
        id = self.get_id(color_theme)

        exporter = theme.get_exporters().get(self._get_exporter_klass(), None)
        if (exporter is None):
            raise Exception("Too lazy to build right now")

        match exporter:
            case __.exporter.FontExporter() | __.exporter.ColrFontExporter():
                glyph_code = exporter.add_icon(definition.language) # TODO: Get glyph from method
                json_root["iconDefinitions"][id] = {
                    "fontCharacter": glyph_code,
                    "fontId": exporter.get_font_id(),
                }
            case _:
                raise Exception("Too lazy to build right now")

        for language_id in self._language_ids:
            json["languageIds"][language_id] = id

        match color_theme:
            case __.ColorTheme.DEFAULT_DARK:
                json_root |= json
            case __.ColorTheme.LIGHT:
                json_root["light"] = json
            case __.ColorTheme.CONTRAST:
                json_root["highContrast"] = json

        theme.add_to_theme_json(json_root, False)

        return
