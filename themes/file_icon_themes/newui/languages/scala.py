from icon_theme_builder.file_icon_theme import *

icons = [

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/scala_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/scala.svg"),
        },
        file_extensions=["sc", "scala"],
    ),

    # TODO: More...

]
