from icon_theme_builder.file_icon_theme import *

icons = [

    icon.LanguageIdIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.LanguageIdIconDefinition("/jetbrains/AppcodeIcons/icons/expui/metal_dark.svg"),
            ColorTheme.LIGHT       : icon.LanguageIdIconDefinition("/jetbrains/AppcodeIcons/icons/expui/metal.svg"),
        },
        language_ids=["metal"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/AppcodeIcons/icons/expui/metal_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/AppcodeIcons/icons/expui/metal.svg"),
        },
        file_extensions=["metal"],
    ),

]
