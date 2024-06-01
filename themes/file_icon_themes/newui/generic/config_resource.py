from icon_theme_builder.file_icon_theme import *

icons = [

    icon.LanguageIdIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.LanguageIdIconDefinition("/jetbrains/AllIcons/expui/fileTypes/config_dark.svg"),
            ColorTheme.LIGHT       : icon.LanguageIdIconDefinition("/jetbrains/AllIcons/expui/fileTypes/config.svg"),
        },
        ["ini"]
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/config_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/config.svg"),
        },
        file_extensions=[
            "ini",
            "dlc",
            "config",
            "conf",
            "prop",
            "settings",
            "options",
            "props",
            "prefs",
            "cfg",
        ],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/properties_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/properties.svg"),
        },
        file_extensions=["properties"],
    ),

    icon.FolderIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FolderIconDefinition(
                                        "/customico/AllIcons/expui/nodes/configFolder_dark.svg",
                                        "/customico/AllIcons/expui/nodes/configFolder_dark-open.svg",
                                    ),
            ColorTheme.LIGHT       : icon.FolderIconDefinition(
                                        "/customico/AllIcons/expui/nodes/configFolder.svg",
                                        "/customico/AllIcons/expui/nodes/configFolder-open.svg",
                                    ),
        },
        [
            "config",
            "configs",
            "cfg",
            "configuration",
            "configurations",
            "settings",
            ".settings",
            "META-INF"
        ]
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/manifest_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/manifest.svg"),
        },
        file_extensions=["manifest"],
    ),

]
