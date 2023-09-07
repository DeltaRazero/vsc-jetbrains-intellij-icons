from icon_theme_builder.file_icon_theme import *

icons = [

    icon.FileIcon(
        "/jetbrains/AllIcons/fileTypes/javaScript.svg",
        file_extensions=["js", "cjs", "mjs"],
    ),

    icon.FileIcon(
        "/jetbrains/JavaScriptPsiIcons/icons/fileTypes/jsx.svg",
        file_extensions=["jsx", "esx"],
    ),

    icon.FileIcon(
        "/jetbrains/JavaScriptPsiIcons/icons/fileTypes/TypeScriptFile.svg",
        file_extensions=["ts"],
    ),

    icon.FileIcon(
        "/jetbrains/JavaScriptPsiIcons/icons/fileTypes/TSX.svg",
        file_extensions=["tsx"],
    ),

    icon.FileIcon(
        "/jetbrains/JavaScriptLanguageIcons/icons/library/jsCompact.svg",
        file_extensions=["asm.js", "wasm"],
    ),

]
