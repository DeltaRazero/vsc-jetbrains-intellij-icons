from icon_theme_builder.file_icon_theme import *

icons = [

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/javaScript_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/javaScript.svg"),
        },
        file_extensions=["js", "cjs", "mjs"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/react_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/react.svg"),
        },
        file_extensions=["jsx", "esx"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/JavaScriptPsiIcons/icons/expui/fileTypes/typeScript_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/JavaScriptPsiIcons/icons/expui/fileTypes/typeScript.svg"),
        },
        file_extensions=["ts"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/react_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/react.svg"),
        },
        file_extensions=["tsx"],
    ),

    # TODO: Make custom icon
    icon.FileIcon(
        "/jetbrains/JavaScriptLanguageIcons/icons/library/jsCompact.svg",
        file_extensions=["asm.js", "wasm"],
    ),

]
