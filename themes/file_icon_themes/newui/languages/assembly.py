from icon_theme_builder.file_icon_theme import *

icons = [

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/CidrLangIcons/icons/expui/fileTypes/asm_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/CidrLangIcons/icons/expui/fileTypes/asm.svg"),
        },
        file_extensions=["asm", "a51", "inc", "nasm", "s", "agc", "aea", "argus", "mitigus", "binsource"],
    ),

]
