from icon_theme_builder.file_icon_theme import *

icons = [

    icon.LanguageIdIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.LanguageIdIconDefinition("/customico/CSharpIcons/icons/expui/cs_dark.svg"),
            ColorTheme.LIGHT       : icon.LanguageIdIconDefinition("/customico/CSharpIcons/icons/expui/cs.svg"),
        },
        language_ids=["csharp"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/customico/CSharpIcons/icons/expui/cs_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/customico/CSharpIcons/icons/expui/cs.svg"),
        },
        file_extensions=["cs"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/customico/CSharpIcons/icons/expui/csx_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/customico/CSharpIcons/icons/expui/csx.svg"),
        },
        file_extensions=["csx"],
    ),

]
