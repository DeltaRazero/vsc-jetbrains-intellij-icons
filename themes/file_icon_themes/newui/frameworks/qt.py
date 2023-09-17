from icon_theme_builder.file_icon_theme import *

icons = [

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/QmlCommonIcons/icons/expui/qml_dark.svg",),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/QmlCommonIcons/icons/expui/qml.svg",),
        },
        file_extensions=["qml"],
    ),

]
