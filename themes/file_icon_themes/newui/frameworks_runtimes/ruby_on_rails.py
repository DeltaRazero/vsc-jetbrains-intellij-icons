from icon_theme_builder.file_icon_theme import *

icons = [

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/HamlIcons/icons/expui/haml_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/HamlIcons/icons/expui/haml.svg"),
        },
        file_extensions=["haml"],
    ),

]
