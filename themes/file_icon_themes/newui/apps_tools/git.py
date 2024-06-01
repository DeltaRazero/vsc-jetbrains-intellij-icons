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

    icon.FolderIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FolderIconDefinition(
                                        "/customico/GitIcons/expui/gitFolder_dark.svg",
                                        "/customico/GitIcons/expui/gitFolder_dark-open.svg",
                                    ),
            ColorTheme.LIGHT       : icon.FolderIconDefinition(
                                        "/customico/GitIcons/expui/gitFolder.svg",
                                        "/customico/GitIcons/expui/gitFolder-open.svg",
                                    ),
        },
        [".git", "githooks", ".githooks", "submodules", ".submodules"]
    ),

]
