from icon_theme_builder.file_icon_theme import *

icons = [

    # TODO: Make custom icon
    icon.FileIcon(
        "/jetbrains/AllIcons/nodes/nodejs.svg",
        file_names=[
            ".esmrc",
            ".node-version",
            ".nvmrc",
            "package.json",
        ],
    ),

    # TODO: Make custom icon
    icon.FileIcon(
        "/customico/JavaScriptLanguageIcons/icons/nodejs/nodejsLock.svg",
        file_names=["package-lock.json"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/JavaScriptLanguageIcons/icons/expui/fileTypes/npm_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/JavaScriptLanguageIcons/icons/expui/fileTypes/npm.svg"),
        },
        file_names=[".npmignore", ".npmrc"],
    ),

    icon.FolderIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FolderIconDefinition(
                                        "/jetbrains/AllIcons/expui/nodes/excludeRoot_dark.svg",
                                        "/jetbrains/AllIcons/expui/nodes/excludeRoot_dark.svg", # TODO: Make custom open icon
                                    ),
            ColorTheme.LIGHT       : icon.FolderIconDefinition(
                                        "/jetbrains/AllIcons/expui/nodes/excludeRoot.svg",
                                        "/jetbrains/AllIcons/expui/nodes/excludeRoot.svg", # TODO: Make custom open icon
                                    ),
        },
        ["node_modules"],
    ),

]
