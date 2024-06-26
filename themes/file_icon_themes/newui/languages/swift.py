from icon_theme_builder.file_icon_theme import *

icons = [

    icon.LanguageIdIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.LanguageIdIconDefinition("/jetbrains/SwiftIcons/icons/expui/swiftLang_dark.svg"),
            ColorTheme.LIGHT       : icon.LanguageIdIconDefinition("/jetbrains/SwiftIcons/icons/expui/swiftLang.svg"),
        },
        language_ids=["swift"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/SwiftIcons/icons/expui/swiftLang_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/SwiftIcons/icons/expui/swiftLang.svg"),
        },
        file_extensions=["swift"],
    ),

    # TODO: Custom icon
    icon.FileIcon(
        "/customico/SwiftIcons/icons/modulemap.svg",
        file_extensions=["map"],
    ),

]
