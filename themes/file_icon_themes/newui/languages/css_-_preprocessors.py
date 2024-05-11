from icon_theme_builder.file_icon_theme import *

icons = [

    icon.LanguageIdIcon(
        "/jetbrains/AllIcons/expui/fileTypes/css.svg",
        language_ids=["css"],
    ),

    icon.LanguageIdIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.LanguageIdIconDefinition("/jetbrains/AllIcons/expui/fileTypes/less_dark.svg"),
            ColorTheme.LIGHT       : icon.LanguageIdIconDefinition("/jetbrains/AllIcons/expui/fileTypes/less.svg"),
        },
        language_ids=["less"],
    ),

    icon.LanguageIdIcon(
        "/jetbrains/AllIcons/expui/fileTypes/scss.svg",
        language_ids=["scss", "sass"],
    ),

    icon.LanguageIdIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.LanguageIdIconDefinition("/jetbrains/StylusIcons/org/jetbrains/plugins/stylus/expui/stylus_dark.svg"),
            ColorTheme.LIGHT       : icon.LanguageIdIconDefinition("/jetbrains/StylusIcons/org/jetbrains/plugins/stylus/expui/stylus.svg"),
        },
        language_ids=["stylus"],
    ),

    icon.FileIcon(
        "/jetbrains/AllIcons/expui/fileTypes/css.svg",
        file_extensions=["css"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/less_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/less.svg"),
        },
        file_extensions=["less"],
    ),

    icon.FileIcon(
        "/jetbrains/AllIcons/expui/fileTypes/scss.svg",
        file_extensions=["scss", "sass"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/StylusIcons/org/jetbrains/plugins/stylus/expui/stylus_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/StylusIcons/org/jetbrains/plugins/stylus/expui/stylus.svg"),
        },
        file_extensions=["styl"],
    ),

]
