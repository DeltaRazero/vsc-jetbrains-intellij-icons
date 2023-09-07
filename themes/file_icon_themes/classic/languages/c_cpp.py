from icon_theme_builder.file_icon_theme import *

icons = [

    icon.FileIcon(
        "/jetbrains/CidrLangIcons/icons/fileTypes/c.svg",
        file_extensions=["c", "i", "mi"],
    ),

    icon.FileIcon(
        "/jetbrains/CidrLangIcons/icons/fileTypes/h.svg",
        file_extensions=["h"],
    ),

    icon.FileIcon(
        "/jetbrains/CidrLangIcons/icons/fileTypes/m.svg",
        file_extensions=["m"],
    ),

    icon.FileIcon(
        "/customico/CidrLangIcons/icons/fileTypes/mm.svg",
        file_extensions=["mm"],
    ),

    icon.FileIcon(
        "/jetbrains/CidrLangIcons/icons/fileTypes/cpp.svg",
        file_extensions=["cc", "cpp", "cxx", "c++", "cp", "mii", "ii"],
    ),

    icon.FileIcon(
        "/customico/CidrLangIcons/icons/fileTypes/hpp.svg",
        file_extensions=["hh", "hpp", "hxx", "h++", "hp", "tcc", "inl"],
    ),

    icon.FileIcon(
        "/jetbrains/CidrLinkerscriptIcons/icons/ld.svg",
        file_extensions=["ld"],
    ),

    # TODO: Make a custom icon using the any_file + AllIcons/nodes/compiledClassesFolder icon
    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/DatabaseIcons/icons/binaryData_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/DatabaseIcons/icons/binaryData.svg"),
        },
        file_extensions=["o", "obj"],
    ),

]
