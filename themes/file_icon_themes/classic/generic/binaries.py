from icon_theme_builder.file_icon_theme import *

icons = [

    icon.FileIcon(
        "/customico/AllIcons/fileTypes/libraryDynamic.svg",
        file_extensions=["so", "dll", "dylib"],
    ),

    icon.FileIcon(
        "/customico/AllIcons/fileTypes/libraryStatic.svg",
        file_extensions=["a", "lib"],
    ),

    icon.FileIcon(
        "/jetbrains/AllIcons/runConfigurations/applet.svg",
        file_extensions=["exe", "x", "app"],
    ),

    # TODO: Installer file, "msi", "deb", "rpm", etc.

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/AllIcons/objectBrowser/showLibraryContents_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/AllIcons/objectBrowser/showLibraryContents.svg"),
        },
        # Driver kernel module
        file_extensions=["ko", "sys"],
    ),

]
