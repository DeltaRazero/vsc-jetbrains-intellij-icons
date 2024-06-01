from icon_theme_builder.file_icon_theme import *

icons = [

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/customico/AllIcons/expui/fileTypes/libraryDynamic_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/customico/AllIcons/expui/fileTypes/libraryDynamic.svg"),
        },
        file_extensions=["so", "dll", "dylib"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/customico/AllIcons/expui/fileTypes/libraryStatic_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/customico/AllIcons/expui/fileTypes/libraryStatic.svg"),
        },
        file_extensions=["a", "lib"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/AllIcons/expui/runConfigurations/application_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/AllIcons/expui/runConfigurations/application.svg"),
        },
        file_extensions=["exe", "x", "app"],
    ),

    # TODO: Installer file, "msi", "deb", "rpm", etc.

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/AllIcons/expui/nodes/library_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/AllIcons/expui/nodes/library.svg"),
        },
        # Driver kernel module
        file_extensions=["ko", "sys"],
    ),

]
