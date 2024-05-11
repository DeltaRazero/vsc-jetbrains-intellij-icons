from icon_theme_builder.file_icon_theme import *

icons = [

    icon.LanguageIdIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.LanguageIdIconDefinition("/jetbrains/JavaScriptPsiIcons/icons/expui/fileTypes/typeScript_dark.svg"),
            ColorTheme.LIGHT       : icon.LanguageIdIconDefinition("/jetbrains/JavaScriptPsiIcons/icons/expui/fileTypes/typeScript.svg"),
        },
        language_ids=["typescript"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/JavaScriptPsiIcons/icons/expui/fileTypes/typeScript_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/JavaScriptPsiIcons/icons/expui/fileTypes/typeScript.svg"),
        },
        file_extensions=["ts"],
    ),

]
