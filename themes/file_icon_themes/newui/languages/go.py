from icon_theme_builder.file_icon_theme import *

icons = [

    icon.LanguageIdIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.LanguageIdIconDefinition("/customico/GoGeneratedIcons/icons/expui/goFile_dark.svg"),
            ColorTheme.LIGHT       : icon.LanguageIdIconDefinition("/customico/GoGeneratedIcons/icons/expui/goFile.svg"),
        },
        language_ids=["go"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/customico/GoGeneratedIcons/icons/expui/goFile_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/customico/GoGeneratedIcons/icons/expui/goFile.svg"),
        },
        file_extensions=["go"],
    ),

    # TODO: todo
    icon.FolderIcon(
        (
            "/jetbrains/GoGeneratedIcons/icons/vendor.svg",
            "/customico/GoGeneratedIcons/icons/vendor-open.svg",
        ),
        ["vendor"],
    ),

]
