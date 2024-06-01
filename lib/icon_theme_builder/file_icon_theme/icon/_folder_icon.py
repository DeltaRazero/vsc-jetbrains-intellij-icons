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
        DefaultableFileIconThemeIcon,
    )

# *****************************************************************************

@__.dataclasses.dataclass
class FolderIconDefinition:
    folder_closed : str
    folder_open   : str | None = None


class FolderIcon (__.DefaultableFileIconThemeIcon):

    # :: TYPES :: #

    _definition_t = str | tuple[str, str] | FolderIconDefinition | dict[__.ColorTheme, FolderIconDefinition]


    # :: PRIVATE ATTRIBUTES :: #

    _definitions : dict[__.ColorTheme, FolderIconDefinition]
    _folder_names : list[str]


    # :: CONSTRUCTOR :: #

    def __init__(self,
                 definition: _definition_t,
                 folder_names: list[str],
                 icon_id: str | None=None,
    ):
        super().__init__(icon_id)

        match definition:
            case str():
                definition = __.t.cast(str, definition)
                self._definitions = {__.ColorTheme.DEFAULT_DARK: FolderIconDefinition(definition)}
            case tuple():
                definition = __.t.cast(tuple, definition)
                self._definitions = {__.ColorTheme.DEFAULT_DARK: FolderIconDefinition(definition[0], definition[1])}
            case FolderIconDefinition():
                definition = __.t.cast(FolderIconDefinition, definition)
                self._definitions = {__.ColorTheme.DEFAULT_DARK: definition}
            case _:
                definition = __.t.cast(dict[__.ColorTheme, FolderIconDefinition], definition)
                self._definitions = definition

        self._folder_names = folder_names

        return


    def add_to_theme(self, theme: __.IconTheme, color_theme: __.ColorTheme):
        json_root  = {
            "iconDefinitions": {}
        }

        definition = self._definitions.get(color_theme, None)
        if (definition is None):
            return

        json = {
            "folderNames": {},
            "folderNamesExpanded" : {},
        }
        base_id = self.get_id(color_theme)

        exporter = theme.get_exporters().get(self._get_exporter_klass(), None)
        if (exporter is None):
            raise ValueError("No exporter was set!")

        for is_open_icon, icon_fp in enumerate([definition.folder_closed, definition.folder_open]):
            if icon_fp is None: continue

            id = f'{base_id}-o' if is_open_icon else f'{base_id}-c'

            match exporter:
                case __.exporter.FontExporter() | __.exporter.ColrFontExporter():
                    exporter.add_icon(icon_fp, self._get_properties())
                    glyph_code = exporter.get_glyph_code()
                    json_root["iconDefinitions"][id] = {
                        "fontCharacter": fr'\{glyph_code}',
                        "fontId": exporter.get_font_id(),
                    }
                case _:
                    raise ValueError(f"Icon type `{type(self).__name__}` does not support exporter type `{type(exporter).__name__}`!")

            if (self._as_default):
                attr_name = "folderExpanded" if is_open_icon else "folder"
                json[attr_name] = id
            else:
                attr_name = "folderNamesExpanded" if is_open_icon else "folderNames"
                for folder_name in self._folder_names:
                    json[attr_name][folder_name] = id

        match color_theme:
            case __.ColorTheme.DEFAULT_DARK:
                json_root |= json
            case __.ColorTheme.LIGHT:
                json_root["light"] = json
            case __.ColorTheme.CONTRAST:
                json_root["highContrast"] = json

        theme.add_to_theme_json(json_root, False)

        return
