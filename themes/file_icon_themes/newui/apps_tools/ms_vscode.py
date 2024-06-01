from icon_theme_builder.file_icon_theme import *

icons = [

    icon.FileIcon(
        "/jetbrains/AllIcons/wizard/vscode.svg",
        file_extensions=["code-workspace", "vscodeignore"],
    ),

    icon.FolderIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FolderIconDefinition(
                                        "/customico/VSCodeIcons/expui/vscodeFolder_dark.svg",
                                        "/customico/VSCodeIcons/expui/vscodeFolder_dark-open.svg",
                                    ),
            ColorTheme.LIGHT       : icon.FolderIconDefinition(
                                        "/customico/VSCodeIcons/expui/vscodeFolder.svg",
                                        "/customico/VSCodeIcons/expui/vscodeFolder-open.svg",
                                    ),
        },
        [".vscode"],
    ),

]
