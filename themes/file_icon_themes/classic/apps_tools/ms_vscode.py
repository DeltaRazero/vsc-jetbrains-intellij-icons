from icon_theme_builder.file_icon_theme import *

icons = [

    icon.FileIcon(
        "/jetbrains/AllIcons/wizard/vscode.svg",
        file_extensions=[".code-workspace", ".vscodeignore"],
    ),

    icon.FolderIcon(
        (
            "/customico/VSCodeIcons/vscodeFolder.svg",
            "/customico/VSCodeIcons/vscodeFolder-open.svg",
        ),
        [".vscode"],
    ),

]
