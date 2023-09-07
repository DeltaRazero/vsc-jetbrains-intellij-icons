from icon_theme_builder.file_icon_theme import *

icons = [

    icon.FileIcon(
        "/jetbrains/SwiftIcons/icons/FileType_swift.svg",
        file_extensions=["swift"],
    ),

    icon.FileIcon(
        "/customico/SwiftIcons/icons/modulemap.svg",
        file_extensions=["map"],
    ),

    # TODO: More

]
