from icon_theme_builder.file_icon_theme import *

icons = [

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/font_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/font.svg"),
        },
        file_extensions=[
            "chr",
            "eot",
            "fnt",
            "fon",
            "font",
            "glif",
            "odttf",
            "otf",
            "pf2",
            "pfr",
            "ttc",
            "ttf",
            "woff",
            "woff",
            "woff2",
        ]
    ),

]
