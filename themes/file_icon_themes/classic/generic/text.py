from icon_theme_builder.file_icon_theme import *

icons = [

    icon.FileIcon(
        "/jetbrains/AllIcons/fileTypes/text.svg",
        file_extensions=["txt", "text", "rst"],
        file_names=["readme", "license"],
    ),

    icon.FileIcon(
        "/jetbrains/MarkdownIcons/icons/MarkdownPlugin.svg",
        file_extensions=["md", "markdown"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/DatabaseIcons/icons/scripting_script_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/DatabaseIcons/icons/scripting_script.svg"),
        },
        file_extensions=["log", "logs"],
    ),

]
