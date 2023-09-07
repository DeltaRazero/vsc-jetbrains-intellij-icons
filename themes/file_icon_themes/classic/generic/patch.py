from icon_theme_builder.file_icon_theme import *

icons = [

    icon.FileIcon(
        "/jetbrains/AllIcons/vcs/patch_file.svg",
        file_extensions=["patch", "diff", "xdelta"],
    ),

    icon.FileIcon(
        "/jetbrains/LocalizationIcons/icons/com/jetbrains/localization/i18n.svg",
        # Translations/localization file
        file_extensions=["pot", "po", "mo"],
    ),

]
