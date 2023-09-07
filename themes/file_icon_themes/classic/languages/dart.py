from icon_theme_builder.file_icon_theme import *

icons = [

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/DartIcons/icons/dart_file_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/DartIcons/icons/dart_file.svg"),
        },
        file_extensions=["dart"],
    ),

]
