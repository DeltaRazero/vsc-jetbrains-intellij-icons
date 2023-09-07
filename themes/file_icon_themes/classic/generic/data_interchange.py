from icon_theme_builder.file_icon_theme import *

icons = [

    # TODO: Graphql

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/AllIcons/fileTypes/json_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/AllIcons/fileTypes/json.svg"),
        },
        file_extensions=["json", "json5", "jsonc"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/AllIcons/fileTypes/jsonSchema_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/AllIcons/fileTypes/jsonSchema.svg"),
        },
        file_names=["schema.json"],
        file_extensions=["schema.json", "jschema"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/TomlIcons/icons/toml-file_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/TomlIcons/icons/toml-file.svg"),
        },
        file_extensions=["toml"],
    ),

    icon.FileIcon(
        "/jetbrains/AllIcons/fileTypes/xml.svg",
        file_extensions=["xml", "plist", "iml", "xquery", "tmLanguage"],
    ),

    icon.FileIcon(
        "/jetbrains/AllIcons/fileTypes/yaml.svg",
        file_extensions=["yaml", "yml", "YAML-tmLanguage"],
    ),

]
