from icon_theme_builder.file_icon_theme import *

icons = [

    icon.LanguageIdIcon(
        "/jetbrains/AllIcons/expui/fileTypes/gitignore.svg",
        ["git-commit", "git-rebase"]
    ),

    icon.FileIcon(
        "/jetbrains/AllIcons/expui/fileTypes/gitignore.svg",
        file_names=[".gitignore", ".gitconfig", ".gitattributes", ".gitmodules",
                    ".gitkeep", "git-history"]
    ),

    # TODO: Make custom icon
    icon.FolderIcon(
        (
            "/customico/GitIcons/gitFolder.svg",
            "/customico/GitIcons/gitFolder-open.svg",
        ),
        [".git", "githooks", ".githooks", "submodules", ".submodules"]
    ),

]
