from icon_theme_builder.file_icon_theme import *

icons = [

    # TODO: todo

    icon.LanguageIdIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.LanguageIdIconDefinition("/jetbrains/KotlinBaseResourcesIcons/org/jetbrains/kotlin/idea/icons/expui/kotlin_dark.svg"),
            ColorTheme.LIGHT       : icon.LanguageIdIconDefinition("/jetbrains/KotlinBaseResourcesIcons/org/jetbrains/kotlin/idea/icons/expui/kotlin.svg"),
        },
        language_ids=["kotlin"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/KotlinBaseResourcesIcons/org/jetbrains/kotlin/idea/icons/expui/kotlin_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/KotlinBaseResourcesIcons/org/jetbrains/kotlin/idea/icons/expui/kotlin.svg"),
        },
        file_extensions=["kt", "ktm"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/KotlinBaseResourcesIcons/org/jetbrains/kotlin/idea/icons/expui/kotlinScript_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/KotlinBaseResourcesIcons/org/jetbrains/kotlin/idea/icons/expui/kotlinScript.svg"),
        },
        file_extensions=["kts"],
    ),

]
