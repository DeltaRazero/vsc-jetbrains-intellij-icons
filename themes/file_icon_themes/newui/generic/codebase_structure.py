from icon_theme_builder.file_icon_theme import *

icons = [
    # TODO: expui
    icon.FolderIcon(
        (
            "/jetbrains/MpsIcons19/intentionsModel.svg",
            "/customico/MpsIcons19/intentionsModel-open.svg",
        ),
        helper.name_combinations(["idea", "poc", "wip"], [".", "_"], ["s"])
    ),

    icon.FolderIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FolderIconDefinition(
                                        "/jetbrains/AllIcons/expui/nodes/excludeRoot_dark.svg",
                                        "/customico/AllIcons/expui/nodes/excludeRoot_dark-open.svg",
                                    ),
            ColorTheme.LIGHT       : icon.FolderIconDefinition(
                                        "/jetbrains/AllIcons/expui/nodes/excludeRoot.svg",
                                        "/customico/AllIcons/expui/nodes/excludeRoot-open.svg",
                                    ),
        },
        helper.name_combinations(["exclude"], [".", "_"], ["s"])
    ),

    icon.FolderIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FolderIconDefinition(
                                        "/jetbrains/AllIcons/expui/nodes/sourceRoot_dark.svg",
                                        "/customico/AllIcons/expui/nodes/sourceRoot_dark-open.svg",
                                    ),
            ColorTheme.LIGHT       : icon.FolderIconDefinition(
                                        "/jetbrains/AllIcons/expui/nodes/sourceRoot.svg",
                                        "/customico/AllIcons/expui/nodes/sourceRoot-open.svg",
                                    ),
        },
        helper.name_combinations(["source", "src"], [".", "_"], ["s"]) + ["code"]
    ),

    icon.FolderIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FolderIconDefinition(
                                        "/customico/PythonIcons/icons/com/jetbrains/python/expui/templateRoot_dark.svg",
                                        "/customico/PythonIcons/icons/com/jetbrains/python/expui/templateRoot_dark-open.svg",
                                    ),
            ColorTheme.LIGHT       : icon.FolderIconDefinition(
                                        "/customico/PythonIcons/icons/com/jetbrains/python/expui/templateRoot.svg",
                                        "/customico/PythonIcons/icons/com/jetbrains/python/expui/templateRoot-open.svg",
                                    ),
        },
        helper.name_combinations(["template", "include"], [".", "_"], ["s"]) # TODO: Make a unique folder color for includes?
    ),

    icon.FolderIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FolderIconDefinition(
                                        "/jetbrains/AllIcons/expui/nodes/testRoot_dark.svg",
                                        "/customico/AllIcons/expui/nodes/testRoot_dark-open.svg",
                                    ),
            ColorTheme.LIGHT       : icon.FolderIconDefinition(
                                        "/jetbrains/AllIcons/expui/nodes/testRoot.svg",
                                        "/customico/AllIcons/expui/nodes/testRoot-open.svg",
                                    ),
        },
        helper.name_combinations(["test"], [".", "_"], ["s"])
    ),

    # TODO: expui
    icon.FolderIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FolderIconDefinition(
                                        "/customico/AllIcons/modules/trashFolder_dark.svg",
                                        "/customico/AllIcons/modules/trashFolder_dark-open.svg",
                                    ),
            ColorTheme.LIGHT       : icon.FolderIconDefinition(
                                        "/customico/AllIcons/modules/trashFolder.svg",
                                        "/customico/AllIcons/modules/trashFolder-open.svg",
                                    ),
        },
        helper.name_combinations(["trash"], [".", "_"])
    ),

    icon.FolderIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FolderIconDefinition(
                                        "/jetbrains/AllIcons/expui/nodes/generated_dark.svg",
                                        "/customico/AllIcons/expui/nodes/generated_dark-open.svg",
                                    ),
            ColorTheme.LIGHT       : icon.FolderIconDefinition(
                                        "/jetbrains/AllIcons/expui/nodes/generated.svg",
                                        "/customico/AllIcons/expui/nodes/generated-open.svg",
                                    ),
        },
        helper.name_combinations(
            [
                "distribution",
                "dist",
                "output",
                "out",
                "build",
                "release",
                "rel",
                "binary",
                "binaries",
                "bin",
            ],
            [".", "_"]
        )
    ),

    # TODO: expui
    icon.FolderIcon(
        (
            "/jetbrains/MpsIcons25/pluginModel.svg",
            "/customico/MpsIcons25/pluginModel-open.svg",
        ),
        helper.name_combinations(["plugin", "addon", "extension"], [".", "_"], ["s"])
    ),

    icon.FolderIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FolderIconDefinition(
                                        "/jetbrains/AllIcons/expui/nodes/resourcesRoot_dark.svg",
                                        "/customico/AllIcons/expui/nodes/resourcesRoot_dark-open.svg",
                                    ),
            ColorTheme.LIGHT       : icon.FolderIconDefinition(
                                        "/jetbrains/AllIcons/expui/nodes/resourcesRoot.svg",
                                        "/customico/AllIcons/expui/nodes/resourcesRoot-open.svg",
                                    ),
        },
        helper.name_combinations(["resource", "rsrc"], [".", "_"], ["s"]) +\
        helper.name_combinations(["res", "static"], [".", "_"])
    ),

    icon.FolderIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FolderIconDefinition(
                                        "/jetbrains/AppcodeIcons/icons/expui/assets_dark.svg",
                                        "/customico/AppcodeIcons/icons/expui/assets_dark-open.svg",
                                    ),
            ColorTheme.LIGHT       : icon.FolderIconDefinition(
                                        "/jetbrains/AppcodeIcons/icons/expui/assets.svg",
                                        "/customico/AppcodeIcons/icons/expui/assets-open.svg",
                                    ),
        },
        helper.name_combinations(["asset"], [".", "_"], ["s"])
    ),

    icon.FolderIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FolderIconDefinition(
                                        "/jetbrains/AllIcons/expui/nodes/libraryFolder_dark.svg",
                                        "/customico/AllIcons/expui/nodes/libraryFolder_dark-open.svg",
                                    ),
            ColorTheme.LIGHT       : icon.FolderIconDefinition(
                                        "/jetbrains/AllIcons/expui/nodes/libraryFolder.svg",
                                        "/customico/AllIcons/expui/nodes/libraryFolder-open.svg",
                                    ),
        },
        helper.name_combinations(["library", "libraries", "lib", "libs", "third-party"], [".", "_"])
    ),

    # TODO: expui
    icon.FolderIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FolderIconDefinition(
                                        "/customico/AllIcons/nodes/localeFolder_dark.svg",
                                        "/customico/AllIcons/nodes/localeFolder_dark-open.svg",
                                    ),
            ColorTheme.LIGHT       : icon.FolderIconDefinition(
                                        "/customico/AllIcons/nodes/localeFolder.svg",
                                        "/customico/AllIcons/nodes/localeFolder-open.svg",
                                    ),
        },
        helper.name_combinations(
            [
                "i18n",
                "l10n",
                "internationalization",
                "lang",
                "language",
                "languages",
                "locale",
                "locales",
                "localization",
                "translation",
                "translations",
                "translate",
            ],
            [".", "_"]
        ) + [".tx"]
    ),

    # TODO: expui
    icon.FolderIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FolderIconDefinition(
                                        "/jetbrains/AllIcons/nodes/logFolder_dark.svg",
                                        "/customico/AllIcons/nodes/logFolder_dark-open.svg",
                                    ),
            ColorTheme.LIGHT       : icon.FolderIconDefinition(
                                        "/jetbrains/AllIcons/nodes/logFolder.svg",
                                        "/customico/AllIcons/nodes/logFolder-open.svg",
                                    ),
        },
        helper.name_combinations(["log"], [".", "_"], ["s"])
    ),

]
