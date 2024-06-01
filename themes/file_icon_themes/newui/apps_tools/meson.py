from icon_theme_builder.file_icon_theme import *

icons = [

    icon.LanguageIdIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.LanguageIdIconDefinition("/customico/MesonIcons/icons/expui/meson_dark.svg"),
            ColorTheme.LIGHT       : icon.LanguageIdIconDefinition("/customico/MesonIcons/icons/expui/meson.svg"),
        },
        ["meson"]
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/customico/MesonIcons/icons/expui/meson_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/customico/MesonIcons/icons/expui/meson.svg"),
        },
        file_names=["meson.build"],
    ),

]
