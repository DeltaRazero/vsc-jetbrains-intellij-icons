from icon_theme_builder.file_icon_theme import *

icons = [

    icon.LanguageIdIcon(
        "/customico/GitIcons/git.svg",
        ["git-commit", "git-rebase"]
    ),

    icon.FileIcon(
        "/customico/GitIcons/git.svg",
        file_names=[".gitignore", ".gitconfig", ".gitattributes", ".gitmodules",
                    ".gitkeep", "git-history"]
    ),

    icon.FolderIcon(
        (
            "/customico/GitIcons/gitFolder.svg",
            "/customico/GitIcons/gitFolder-open.svg",
        ),
        [".git", "githooks", ".githooks", "submodules", ".submodules"]
    ),

]
