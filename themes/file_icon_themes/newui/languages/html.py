from icon_theme_builder.file_icon_theme import *

icons = [

    icon.LanguageIdIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.LanguageIdIconDefinition("/jetbrains/AllIcons/expui/fileTypes/html_dark.svg"),
            ColorTheme.LIGHT       : icon.LanguageIdIconDefinition("/jetbrains/AllIcons/expui/fileTypes/html.svg"),
        },
        language_ids=["html"],
    ),

    icon.LanguageIdIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.LanguageIdIconDefinition("/jetbrains/AllIcons/expui/fileTypes/xhtml_dark.svg"),
            ColorTheme.LIGHT       : icon.LanguageIdIconDefinition("/jetbrains/AllIcons/expui/fileTypes/xhtml.svg"),
        },
        language_ids=["xhtml"],
    ),

    # TODO: Move "asp" to ASP.NET file
    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/html_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/html.svg"),
        },
        file_extensions=["asp", "htm", "html"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/xhtml_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/xhtml.svg"),
        },
        file_extensions=["xhtml"],
    ),

]
