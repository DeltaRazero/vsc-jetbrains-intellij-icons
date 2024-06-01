from icon_theme_builder.file_icon_theme import *

icons = [

    icon.LanguageIdIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.LanguageIdIconDefinition("/jetbrains/HamlIcons/icons/expui/haml_dark.svg"),
            ColorTheme.LIGHT       : icon.LanguageIdIconDefinition("/jetbrains/HamlIcons/icons/expui/haml.svg"),
        },
        ["haml"]
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/HamlIcons/icons/expui/haml_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/HamlIcons/icons/expui/haml.svg"),
        },
        file_extensions=["haml"],
    ),

]
