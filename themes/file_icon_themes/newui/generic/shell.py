from icon_theme_builder.file_icon_theme import *

icons = [

    icon.LanguageIdIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.LanguageIdIconDefinition("/jetbrains/AllIcons/expui/fileTypes/shell_dark.svg"),
            ColorTheme.LIGHT       : icon.LanguageIdIconDefinition("/jetbrains/AllIcons/expui/fileTypes/shell.svg"),
        },
        language_ids=[
            "bat",
            "powershell",
            "shellscript",
            "bash",
            "sh",
        ]
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/shell_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/shell.svg"),
        },
        file_extensions=[
            "bash",
            "bat",
            "cmd",
            "ksh",
            "ps1",
            "ps1xml",
            "psc1",
            "psd1",
            "psm1",
            "pssc",
            "sh",
            "zsh",
        ],
    ),

]
