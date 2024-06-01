from icon_theme_builder.file_icon_theme import *

icons = [

    icon.LanguageIdIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.LanguageIdIconDefinition("/jetbrains/CMakeIcons/icons/expui/CMake_dark.svg"),
            ColorTheme.LIGHT       : icon.LanguageIdIconDefinition("/jetbrains/CMakeIcons/icons/expui/CMake.svg"),
        },
        ["cmake"]
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/CMakeIcons/icons/expui/CMake_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/CMakeIcons/icons/expui/CMake.svg"),
        },
        file_names=["CMakeLists.txt", "cmakecache.txt"],
    ),

]
