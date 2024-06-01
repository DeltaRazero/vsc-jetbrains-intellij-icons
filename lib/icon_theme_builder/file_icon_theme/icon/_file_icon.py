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
class FileIconDefinition:
    file : str


class FileIcon (__.DefaultableFileIconThemeIcon):

    # :: TYPES :: #

    _definition_t = str | FileIconDefinition | dict[__.ColorTheme, FileIconDefinition]


    # :: PRIVATE ATTRIBUTES :: #

    _definitions : dict[__.ColorTheme, FileIconDefinition]
    _file_names      : list[str]
    _file_extensions : list[str]


    # :: CONSTRUCTOR :: #

    def __init__(self,
                 definition: _definition_t,
                 file_names     : list[str] | None=None,
                 file_extensions: list[str] | None=None,
                 icon_id: str | None=None,
    ):
        super().__init__(icon_id)

        match definition:
            case str():
                definition = __.t.cast(str, definition)
                self._definitions = {__.ColorTheme.DEFAULT_DARK: FileIconDefinition(definition)}
            case FileIconDefinition():
                definition = __.t.cast(FileIconDefinition, definition)
                self._definitions = {__.ColorTheme.DEFAULT_DARK: definition}
            case _:
                definition = __.t.cast(dict[__.ColorTheme, FileIconDefinition], definition)
                self._definitions = definition

        if file_names      is None: file_names      = []
        if file_extensions is None: file_extensions = []

        # Ensure that either file names or extension names have been set
        if not (file_names or file_extensions):
            raise ValueError("Either file names or file extensions must be given at minimum!")

        self._file_names      = file_names
        self._file_extensions = file_extensions

        return


    def add_to_theme(self, theme: __.IconTheme, color_theme: __.ColorTheme):
        json_root  = {
            "iconDefinitions": {}
        }

        definition = self._definitions.get(color_theme, None)
        if (definition is None):
            return

        json = {
            "fileNames": {},
            "fileExtensions" : {},
        }
        id = self.get_id(color_theme)

        exporter = theme.get_exporters().get(self._get_exporter_klass(), None)
        if (exporter is None):
            raise ValueError("No exporter was set!")

        match exporter:
            case __.exporter.FontExporter() | __.exporter.ColrFontExporter():
                exporter.add_icon(definition.file, self._get_properties())
                glyph_code = exporter.get_glyph_code()
                json_root["iconDefinitions"][id] = {
                    "fontCharacter": fr'\{glyph_code}',
                    "fontId": exporter.get_font_id(),
                }
            case _:
                raise ValueError(f"Icon type `{type(self).__name__}` does not support exporter type `{type(exporter).__name__}`!")

        if (self._as_default):
            json["file"] = id
        else:
            for file_name      in self._file_names     : json["fileNames"][file_name] = id
            for file_extension in self._file_extensions: json["fileExtensions"][file_extension] = id

        match color_theme:
            case __.ColorTheme.DEFAULT_DARK:
                json_root |= json
            case __.ColorTheme.LIGHT:
                json_root["light"] = json
            case __.ColorTheme.CONTRAST:
                json_root["highContrast"] = json

        theme.add_to_theme_json(json_root, False)

        return
