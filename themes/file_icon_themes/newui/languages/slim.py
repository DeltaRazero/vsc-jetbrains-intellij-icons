from icon_theme_builder.file_icon_theme import *

icons = [

    icon.LanguageIdIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.LanguageIdIconDefinition("/jetbrains/SlimIcons/icons/expui/slim_dark.svg"),
            ColorTheme.LIGHT       : icon.LanguageIdIconDefinition("/jetbrains/SlimIcons/icons/expui/slim.svg"),
        },
        language_ids=["slim"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/SlimIcons/icons/expui/slim_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/SlimIcons/icons/expui/slim.svg"),
        },
        file_extensions=["slim"],
    ),

]
