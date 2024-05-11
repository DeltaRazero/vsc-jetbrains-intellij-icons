from icon_theme_builder.file_icon_theme import *

icons = [

    icon.LanguageIdIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.LanguageIdIconDefinition("/customico/CrystalIcons/icons/expui/crystal_dark.svg"),
            ColorTheme.LIGHT       : icon.LanguageIdIconDefinition("/customico/CrystalIcons/icons/expui/crystal.svg"),
        },
        language_ids=["crystal"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/customico/CrystalIcons/icons/expui/crystal_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/customico/CrystalIcons/icons/expui/crystal.svg"),
        },
        file_extensions=["cr", "ecr", "slang"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/customico/CrystalIcons/icons/expui/crystal_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/customico/CrystalIcons/icons/expui/crystal.svg"),
        },
        file_names=["shard.yml"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/customico/CrystalIcons/icons/expui/crystalLock_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/customico/CrystalIcons/icons/expui/crystalLock.svg"),
        },
        file_names=["shard.lock"],
    ),

]
