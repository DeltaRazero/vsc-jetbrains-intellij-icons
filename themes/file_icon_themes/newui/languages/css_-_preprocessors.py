from icon_theme_builder.file_icon_theme import *

icons = [

    icon.FileIcon(
        "/jetbrains/AllIcons/expui/fileTypes/css.svg",
        file_extensions=["css"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/less_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/less.svg"),
        },
        file_extensions=["less"],
    ),

    icon.FileIcon(
        "/jetbrains/AllIcons/expui/fileTypes/scss.svg",
        file_extensions=["scss", "sass"],
    ),

    # https://stylus-lang.com/
    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/StylusIcons/org/jetbrains/plugins/stylus/expui/stylus_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/StylusIcons/org/jetbrains/plugins/stylus/expui/stylus.svg"),
        },
        file_extensions=["styl"],
    ),

]
