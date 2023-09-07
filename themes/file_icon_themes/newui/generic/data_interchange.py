from icon_theme_builder.file_icon_theme import *

icons = [

    # TODO: Graphql

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/json_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/json.svg"),
        },
        file_extensions=["json", "json5", "jsonc"],
    ),

    # TODO: Custom icon?
    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/json_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/json.svg"),
        },
        file_names=["schema.json"],
        file_extensions=["schema.json", "jschema"],
    ),

    # FIXME: Wait for expui icon?
    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/TomlIcons/icons/toml-file_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/TomlIcons/icons/toml-file.svg"),
        },
        file_extensions=["toml"],
    ),


    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/xml_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/xml.svg"),
        },
        file_extensions=["xml", "plist", "iml", "xquery", "tmLanguage"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/yaml_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/yaml.svg"),
        },
        file_extensions=["yaml", "yml", "YAML-tmLanguage"],
    ),

]
