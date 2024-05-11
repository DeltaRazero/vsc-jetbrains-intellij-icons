from icon_theme_builder.file_icon_theme import *

icons = [

    icon.LanguageIdIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.LanguageIdIconDefinition("/jetbrains/CMakeIcons/icons/expui/cuda_dark.svg"),
            ColorTheme.LIGHT       : icon.LanguageIdIconDefinition("/jetbrains/CMakeIcons/icons/expui/cuda.svg"),
        },
        language_ids=["cuda", "cuda-cpp"],
    ),

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
