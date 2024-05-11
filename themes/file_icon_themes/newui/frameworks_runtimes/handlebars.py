from icon_theme_builder.file_icon_theme import *

icons = [

    icon.LanguageIdIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.LanguageIdIconDefinition("/customico/HandlebarsIcons/icons/expui/handlebars_dark.svg"),
            ColorTheme.LIGHT       : icon.LanguageIdIconDefinition("/customico/HandlebarsIcons/icons/expui/handlebars.svg"),
        },
        language_ids=["handlebars"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/customico/HandlebarsIcons/icons/expui/handlebars_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/customico/HandlebarsIcons/icons/expui/handlebars.svg"),
        },
        file_extensions=["hbs", "mustache"],
    ),

]
