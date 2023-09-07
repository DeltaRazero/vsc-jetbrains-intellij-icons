from icon_theme_builder.file_icon_theme import *

icons = [

    icon.FileIcon(
        "/customico/GoGeneratedIcons/icons/go_file.svg",
        file_extensions=["go"],
    ),

    icon.FolderIcon(
        (
            "/jetbrains/GoGeneratedIcons/icons/vendor.svg",
            "/customico/GoGeneratedIcons/icons/vendor-open.svg",
        ),
        ["vendor"],
    ),

]
