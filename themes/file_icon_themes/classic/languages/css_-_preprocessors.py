from icon_theme_builder.file_icon_theme import *

icons = [

    icon.FileIcon(
        "/jetbrains/AllIcons/fileTypes/css.svg",
        file_extensions=["css"],
    ),

    icon.FileIcon(
        "/jetbrains/LessIcons/icons/less.svg",
        file_extensions=["less"],
    ),

    icon.FileIcon(
        "/jetbrains/SassIcons/org/jetbrains/plugins/sass/sass.svg",
        file_extensions=["scss", "sass"],
    ),

    # https://stylus-lang.com/
    icon.FileIcon(
        "/jetbrains/StylusIcons/org/jetbrains/plugins/stylus/styl.svg",
        file_extensions=["styl"],
    ),

]
