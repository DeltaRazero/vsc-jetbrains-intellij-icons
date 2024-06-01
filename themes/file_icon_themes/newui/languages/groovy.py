from icon_theme_builder.file_icon_theme import *

icons = [

    icon.LanguageIdIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.LanguageIdIconDefinition("/jetbrains/JetgroovyIcons/icons/groovy/newui/groovy_dark.svg"),
            ColorTheme.LIGHT       : icon.LanguageIdIconDefinition("/jetbrains/JetgroovyIcons/icons/groovy/newui/groovy.svg"),
        },
        language_ids=["groovy"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/JetgroovyIcons/icons/groovy/newui/groovy_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/JetgroovyIcons/icons/groovy/newui/groovy.svg"),
        },
        file_extensions=["groovy"],
    ),

]
