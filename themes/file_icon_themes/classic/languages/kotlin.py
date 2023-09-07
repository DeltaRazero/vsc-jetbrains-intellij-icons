from icon_theme_builder.file_icon_theme import *

icons = [

    icon.FileIcon(
        "/jetbrains/KotlinBaseResourcesIcons/org/jetbrains/kotlin/idea/icons/kotlin_file.svg",
        file_extensions=["kt", "ktm"],
    ),

    icon.FileIcon(
        "/jetbrains/KotlinBaseResourcesIcons/org/jetbrains/kotlin/idea/icons/kotlin_script.svg",
        file_extensions=["kts"],
    ),

]
