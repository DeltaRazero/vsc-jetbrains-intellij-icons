from icon_theme_builder.file_icon_theme import *

icons = [

    icon.LanguageIdIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.LanguageIdIconDefinition("/jetbrains/ClionMakefileIcons/icons/expui/makefile_dark.svg"),
            ColorTheme.LIGHT       : icon.LanguageIdIconDefinition("/jetbrains/ClionMakefileIcons/icons/expui/makefile.svg"),
        },
        ["makefile"]
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/ClionMakefileIcons/icons/expui/makefile_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/ClionMakefileIcons/icons/expui/makefile.svg"),
        },
        file_names=["makefile"],
        file_extensions=["make", "makefile"],
    ),

]
