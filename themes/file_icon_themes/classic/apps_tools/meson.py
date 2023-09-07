from icon_theme_builder.file_icon_theme import *

icons = [

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/customico/MesonIcons/icons/meson_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/customico/MesonIcons/icons/meson_light.svg"),
        },
        file_names=["meson.build"],
    ),

]
