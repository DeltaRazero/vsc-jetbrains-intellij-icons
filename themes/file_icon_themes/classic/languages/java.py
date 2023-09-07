from icon_theme_builder.file_icon_theme import *

icons = [

    icon.FileIcon(
        "/jetbrains/AllIcons/fileTypes/java.svg",
        file_extensions=["java"],
    ),

    icon.FileIcon(
        "/jetbrains/AllIcons/fileTypes/jsp.svg",
        file_extensions=["jsp"],
    ),

    icon.FileIcon(
        "/jetbrains/AllIcons/fileTypes/javaClass.svg",
        file_extensions=["class"],
    ),

    icon.FileIcon(
        "/jetbrains/AllIcons/nodes/ppJar.svg",
        file_extensions=["jar"],
    ),

    icon.FolderIcon(
        (
            "/jetbrains/AllIcons/nodes/jarDirectory.svg",
            "/customico/AllIcons/nodes/jarDirectory-open.svg",
        ),
        ["jar"]
    ),

    icon.FolderIcon(
        (
            "/jetbrains/AllIcons/nodes/javaDocFolder.svg",
            "/customico/AllIcons/nodes/javaDocFolder-open.svg",
        ),
        ["javadoc"]
    ),

]
