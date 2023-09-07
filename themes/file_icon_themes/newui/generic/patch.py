from icon_theme_builder.file_icon_theme import *

icons = [

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/patch_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/patch.svg"),
        },
        file_extensions=["patch", "diff", "xdelta"],
    ),

    # TODO: Make custom icon
    icon.FileIcon(
        "/jetbrains/LocalizationIcons/icons/com/jetbrains/localization/i18n.svg",
        # Translations/localization file
        file_extensions=["pot", "po", "mo"],
    ),

]
