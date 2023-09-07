from icon_theme_builder.file_icon_theme import *

icons = [

    icon.FileIcon(
        "/jetbrains/AllIcons/fileTypes/any_type.svg",
        [""],
    ).as_default(),

    icon.FolderIcon(
        (
            "/jetbrains/AllIcons/nodes/folder.svg",
            "/customico/AllIcons/nodes/folder_open.svg",
        ),
        [""],
    ).as_default(),

]
