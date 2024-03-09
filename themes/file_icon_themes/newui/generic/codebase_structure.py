from icon_theme_builder.file_icon_theme import *

icons = [

    # TODO: todo

    icon.FolderIcon(
        (
            "/jetbrains/MpsIcons19/intentionsModel.svg",
            "/customico/MpsIcons19/intentionsModel-open.svg",
        ),
        helper.name_combinations(["idea", "poc", "wip"], [".", "_"], ["s"])
    ),

    icon.FolderIcon(
        (
            "/jetbrains/AllIcons/modules/excludeRoot.svg",
            "/customico/AllIcons/modules/excludeRoot-open.svg",
        ),
        helper.name_combinations(["exclude"], [".", "_"], ["s"])
    ),

    icon.FolderIcon(
        (
            "/jetbrains/AllIcons/modules/sourceRoot.svg",
            "/customico/AllIcons/modules/sourceRoot-open.svg",
        ),
        helper.name_combinations(["source", "src"], [".", "_"], ["s"]) + ["code"]
    ),

    icon.FolderIcon(
        (
            "/jetbrains/PythonIcons/icons/com/jetbrains/python/templateRoot.svg",
            "/customico/PythonIcons/icons/com/jetbrains/python/templateRoot-open.svg",
        ),
        helper.name_combinations(["template", "include"], [".", "_"], ["s"]) # TODO: Make a unique folder color for includes?
    ),

    icon.FolderIcon(
        (
            "/jetbrains/AllIcons/modules/testRoot.svg",
            "/customico/AllIcons/modules/testRoot-open.svg",
        ),
        helper.name_combinations(["test"], [".", "_"], ["s"])
    ),

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
        (
            "/jetbrains/AllIcons/modules/generatedFolder.svg",
            "/customico/AllIcons/modules/generatedFolder-open.svg",
        ),
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

    icon.FolderIcon(
        (
            "/jetbrains/MpsIcons25/pluginModel.svg",
            "/customico/MpsIcons25/pluginModel-open.svg",
        ),
        helper.name_combinations(["plugin", "addon", "extension"], [".", "_"], ["s"])
    ),

    icon.FolderIcon(
        (
            "/jetbrains/AllIcons/modules/resourcesRoot.svg",
            "/customico/AllIcons/modules/resourcesRoot-open.svg",
        ),
        helper.name_combinations(["resource", "rsrc"], [".", "_"], ["s"]) +\
        helper.name_combinations(["res", "static"], [".", "_"])
    ),

    icon.FolderIcon(
        (
            "/jetbrains/AppcodeIcons/icons/Assets.svg",
            "/customico/AppcodeIcons/icons/Assets-open.svg",
        ),
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
