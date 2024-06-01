from icon_theme_builder.file_icon_theme import *

icons = [

    icon.LanguageIdIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.LanguageIdIconDefinition("/jetbrains/AllIcons/expui/fileTypes/text_dark.svg"),
            ColorTheme.LIGHT       : icon.LanguageIdIconDefinition("/jetbrains/AllIcons/expui/fileTypes/text.svg"),
        },
        language_ids=[
            "plaintext",
            "latex",
            "restructuredtext",
            "tex",
        ],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/text_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/text.svg"),
        },
        file_extensions=["txt", "text", "rst", "tex"],
        file_names=["readme", "license"],
    ),

    icon.LanguageIdIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.LanguageIdIconDefinition("/jetbrains/MarkdownIcons/icons/expui/markdown_dark.svg"),
            ColorTheme.LIGHT       : icon.LanguageIdIconDefinition("/jetbrains/MarkdownIcons/icons/expui/markdown.svg"),
        },
        language_ids=["markdown"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/MarkdownIcons/icons/expui/markdown_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/MarkdownIcons/icons/expui/markdown.svg"),
        },
        file_extensions=["md", "markdown"],
    ),

    # TODO: Make custom icon
    icon.LanguageIdIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.LanguageIdIconDefinition("/jetbrains/DatabaseIcons/icons/scripting_script_dark.svg"),
            ColorTheme.LIGHT       : icon.LanguageIdIconDefinition("/jetbrains/DatabaseIcons/icons/scripting_script.svg"),
        },
        language_ids=[
            "latex",
            "plaintext",
            "restructuredtext",
            "text",
        ],
    ),

    # TODO: Make custom icon
    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/DatabaseIcons/icons/scripting_script_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/DatabaseIcons/icons/scripting_script.svg"),
        },
        file_extensions=["log", "logs"],
    ),

]
