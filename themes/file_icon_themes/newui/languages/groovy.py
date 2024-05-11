from icon_theme_builder.file_icon_theme import *

icons = [

    # TODO: Make custom icon

    icon.LanguageIdIcon(
        "/jetbrains/JetgroovyIcons/icons/groovy/groovy_16x16.svg",
        language_ids=["groovy"],
    ),

    icon.FileIcon(
        "/jetbrains/JetgroovyIcons/icons/groovy/groovyFile.svg",
        file_extensions=["groovy"],
    ),

]
