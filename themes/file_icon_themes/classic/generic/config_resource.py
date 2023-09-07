from icon_theme_builder.file_icon_theme import *

icons = [

    icon.FileIcon(
        "/jetbrains/AllIcons/fileTypes/manifest.svg",
        file_extensions=["manifest"],
    ),

    icon.FileIcon(
        "/jetbrains/AllIcons/fileTypes/config.svg",
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
        "/jetbrains/AllIcons/fileTypes/properties.svg",
        file_extensions=["properties"],
    ),

    icon.FileIcon(
        "/jetbrains/AllIcons/nodes/editorconfig.svg",
        file_extensions=["editorconfig"],
    ),

    icon.FolderIcon(
        (
            "/jetbrains/AllIcons/nodes/configFolder.svg",
            "/customico/AllIcons/nodes/configFolder-open.svg",
        ),
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

]
