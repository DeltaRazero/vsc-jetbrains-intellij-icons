from icon_theme_builder.file_icon_theme import *

icons = [

    icon.LanguageIdIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.LanguageIdIconDefinition("/customico/DIcons/icons/expui/dFile_dark.svg"),
            ColorTheme.LIGHT       : icon.LanguageIdIconDefinition("/customico/DIcons/icons/expui/dFile.svg"),
        },
        language_ids=["d"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/customico/DIcons/icons/expui/dFile_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/customico/DIcons/icons/expui/dFile.svg"),
        },
        file_extensions=["d"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/customico/DIcons/icons/expui/dppFile_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/customico/DIcons/icons/expui/dppFile.svg"),
        },
        file_extensions=["dpp", "d++"],
    ),

]
