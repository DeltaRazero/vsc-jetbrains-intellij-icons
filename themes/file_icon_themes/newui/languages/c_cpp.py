from icon_theme_builder.file_icon_theme import *

icons = [

    icon.LanguageIdIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.LanguageIdIconDefinition("/jetbrains/CidrLangIcons/icons/expui/fileTypes/c_dark.svg"),
            ColorTheme.LIGHT       : icon.LanguageIdIconDefinition("/jetbrains/CidrLangIcons/icons/expui/fileTypes/c.svg"),
        },
        language_ids=["c"],
    ),

    icon.LanguageIdIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.LanguageIdIconDefinition("/jetbrains/CidrLangIcons/icons/expui/fileTypes/cpp_dark.svg"),
            ColorTheme.LIGHT       : icon.LanguageIdIconDefinition("/jetbrains/CidrLangIcons/icons/expui/fileTypes/cpp.svg"),
        },
        language_ids=["cpp"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/CidrLangIcons/icons/expui/fileTypes/c_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/CidrLangIcons/icons/expui/fileTypes/c.svg"),
        },
        file_extensions=["c", "i", "mi"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/CidrLangIcons/icons/expui/fileTypes/h_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/CidrLangIcons/icons/expui/fileTypes/h.svg"),
        },
        file_extensions=["h"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/CidrLangIcons/icons/expui/fileTypes/m_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/CidrLangIcons/icons/expui/fileTypes/m.svg"),
        },
        file_extensions=["m", "mm"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/CidrLangIcons/icons/expui/fileTypes/cpp_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/CidrLangIcons/icons/expui/fileTypes/cpp.svg"),
        },
        file_extensions=["cc", "cpp", "cxx", "c++", "cp", "mii", "ii"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/customico/CidrLangIcons/icons/expui/fileTypes/hpp_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/customico/CidrLangIcons/icons/expui/fileTypes/hpp.svg"),
        },
        file_extensions=["hh", "hpp", "hxx", "h++", "hp", "tcc", "inl"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/CidrLinkerscriptIcons/icons/expui/ld_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/CidrLinkerscriptIcons/icons/expui/ld.svg"),
        },
        file_extensions=["ld"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/DatabaseIcons/icons/expui/binaryData_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/DatabaseIcons/icons/expui/binaryData.svg"),
        },
        file_extensions=["o", "obj"],
    ),

]
