from icon_theme_builder.file_icon_theme import *

icons = [

    icon.FileIcon(
        "/jetbrains/AllIcons/nodes/nodejs.svg",
        file_names=[
            ".esmrc",
            ".node-version",
            ".nvmrc",
            "package.json",
        ],
    ),

    icon.FileIcon(
        "/customico/JavaScriptLanguageIcons/icons/nodejs/nodejsLock.svg",
        file_names=["package-lock.json"],
    ),

    icon.FileIcon(
        "/customico/JavaScriptLanguageIcons/icons/nodejs/npm.svg",
        file_names=[".npmignore", ".npmrc"],
    ),

    icon.FolderIcon(
        (
            "/jetbrains/AllIcons/modules/excludeRoot.svg",
            "/customico/AllIcons/modules/excludeRoot-open.svg",
        ),
        ["node_modules"],
    ),

]
