from icon_theme_builder.file_icon_theme import *

icons = [

    icon.LanguageIdIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.LanguageIdIconDefinition("/customico/HaskellIcons/icons/expui/haskell_dark.svg"),
            ColorTheme.LIGHT       : icon.LanguageIdIconDefinition("/customico/HaskellIcons/icons/expui/haskell.svg"),
        },
        language_ids=["haskell"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/customico/HaskellIcons/icons/expui/haskell_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/customico/HaskellIcons/icons/expui/haskell.svg"),
        },
        file_extensions=["hs", "lhs"],
    ),

]
