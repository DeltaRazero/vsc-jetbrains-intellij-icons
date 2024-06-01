from icon_theme_builder.file_icon_theme import *

icons = [

    icon.LanguageIdIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.LanguageIdIconDefinition("/customico/LuaIcons/icons/expui/lua_dark.svg"),
            ColorTheme.LIGHT       : icon.LanguageIdIconDefinition("/customico/LuaIcons/icons/expui/lua.svg"),
        },
        language_ids=["lua"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/customico/LuaIcons/icons/expui/lua_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/customico/LuaIcons/icons/expui/lua.svg"),
        },
        file_names=[".luacheckrc"],
        file_extensions=["lua"],
    ),

]
