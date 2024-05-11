from icon_theme_builder.file_icon_theme import *

icons = [

    icon.LanguageIdIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.LanguageIdIconDefinition("/customico/CoffeescriptIcons/org/coffeescript/images/expui/coffeescript_dark.svg"),
            ColorTheme.LIGHT       : icon.LanguageIdIconDefinition("/customico/CoffeescriptIcons/org/coffeescript/images/expui/coffeescript.svg"),
        },
        language_ids=["coffeescript"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/customico/CoffeescriptIcons/org/coffeescript/images/expui/coffeescript_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/customico/CoffeescriptIcons/org/coffeescript/images/expui/coffeescript.svg"),
        },
        file_extensions=["coffee", "cson", "iced"],
    ),

]
