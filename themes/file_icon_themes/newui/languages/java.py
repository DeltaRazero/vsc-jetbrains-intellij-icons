from icon_theme_builder.file_icon_theme import *

icons = [

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/java_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/java.svg"),
        },
        file_extensions=["java"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/jsp_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/jsp.svg"),
        },
        file_extensions=["jsp"],
    ),

    # TODO: Make custom icon
    icon.FileIcon(
        "/jetbrains/AllIcons/fileTypes/javaClass.svg",
        file_extensions=["class"],
    ),

    # TODO: Make custom icon
    icon.FileIcon(
        "/jetbrains/AllIcons/nodes/ppJar.svg",
        file_extensions=["jar"],
    ),

    # TODO: todo
    icon.FolderIcon(
        (
            "/jetbrains/AllIcons/nodes/jarDirectory.svg",
            "/customico/AllIcons/nodes/jarDirectory-open.svg",
        ),
        ["jar"]
    ),

    # TODO: todo
    icon.FolderIcon(
        (
            "/jetbrains/AllIcons/nodes/javaDocFolder.svg",
            "/customico/AllIcons/nodes/javaDocFolder-open.svg",
        ),
        ["javadoc"]
    ),

]
