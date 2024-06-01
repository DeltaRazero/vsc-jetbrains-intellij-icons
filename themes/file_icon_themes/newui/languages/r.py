from icon_theme_builder.file_icon_theme import *

icons = [

    icon.LanguageIdIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.LanguageIdIconDefinition("/customico/RIcons/icons/expui/r_dark.svg"),
            ColorTheme.LIGHT       : icon.LanguageIdIconDefinition("/customico/RIcons/icons/expui/r.svg"),
        },
        language_ids=["r"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/customico/RIcons/icons/expui/r_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/customico/RIcons/icons/expui/r.svg"),
        },
        file_extensions=[
            "r",
            "rdata",
            "rds",
            "rda"
        ],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/customico/RIcons/icons/expui/rMarkdown_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/customico/RIcons/icons/expui/rMarkdown.svg"),
        },
        file_extensions=["rmd"],
    ),

]
