from icon_theme_builder.file_icon_theme import *

icons = [

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/CidrLangIcons/icons/expui/fileTypes/cu_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/CidrLangIcons/icons/expui/fileTypes/cu.svg"),
        },
        file_extensions=["cu", "cuda"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/CidrLangIcons/icons/expui/fileTypes/cuh_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/CidrLangIcons/icons/expui/fileTypes/cuh.svg"),
        },
        file_extensions=["cuh", "cudah"],
    ),

]
