from icon_theme_builder.file_icon_theme import *

icons = [

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/anyType_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/anyType.svg"),
        },
        [""],
    ).as_default(),

    icon.FolderIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FolderIconDefinition(
                                        "/jetbrains/AllIcons/expui/nodes/folder_dark.svg",
                                        "/jetbrains/RubyIcons/icons/expui/rails/projectView/incompleteFolder_dark.svg",
                                    ),
            ColorTheme.LIGHT       : icon.FolderIconDefinition(
                                        "/jetbrains/AllIcons/expui/nodes/folder.svg",
                                        "/jetbrains/RubyIcons/icons/expui/rails/projectView/incompleteFolder.svg",
                                    ),
        },
        [""],
    ).as_default(),

]
