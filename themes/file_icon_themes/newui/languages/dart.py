from icon_theme_builder.file_icon_theme import *

icons = [

    icon.LanguageIdIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.LanguageIdIconDefinition("/customico/DartIcons/icons/expui/dart_dark.svg"),
            ColorTheme.LIGHT       : icon.LanguageIdIconDefinition("/customico/DartIcons/icons/expui/dart.svg"),
        },
        language_ids=["dart"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/customico/DartIcons/icons/expui/dart_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/customico/DartIcons/icons/expui/dart.svg"),
        },
        file_extensions=["dart"],
    ),

]
