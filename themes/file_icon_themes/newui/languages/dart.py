from icon_theme_builder.file_icon_theme import *

icons = [

    # TODO: Make custom icon?

    icon.LanguageIdIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.LanguageIdIconDefinition("/jetbrains/DartIcons/icons/dart_file_dark.svg"),
            ColorTheme.LIGHT       : icon.LanguageIdIconDefinition("/jetbrains/DartIcons/icons/dart_file.svg"),
        },
        language_ids=["dart"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/DartIcons/icons/dart_file_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/DartIcons/icons/dart_file.svg"),
        },
        file_extensions=["dart"],
    ),

]
