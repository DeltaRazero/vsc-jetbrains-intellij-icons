from icon_theme_builder.file_icon_theme import *

icons = [

    # TODO: Change color of dark variant
    # TODO: Wider border(?)
    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/customico/CrystalIcons/icons/crystalFile_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/customico/CrystalIcons/icons/crystalFile_light.svg"),
        },
        file_extensions=["cr", "ecr", "slang"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/customico/CrystalIcons/icons/crystal_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/customico/CrystalIcons/icons/crystal_light.svg"),
        },
        file_names=["shard.yml"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/customico/CrystalIcons/icons/crystalLock_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/customico/CrystalIcons/icons/crystalLock_light.svg"),
        },
        file_names=["shard.lock"],
    ),

]
