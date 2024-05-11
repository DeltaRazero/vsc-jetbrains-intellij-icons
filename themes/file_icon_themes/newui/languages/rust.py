from icon_theme_builder.file_icon_theme import *

icons = [

    icon.LanguageIdIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.LanguageIdIconDefinition("/customico/RustIcons/expui/rust_dark.svg"),
            ColorTheme.LIGHT       : icon.LanguageIdIconDefinition("/customico/RustIcons/expui/rust.svg"),
        },
        language_ids=["rust"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/customico/RustIcons/expui/rust_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/customico/RustIcons/expui/rust.svg"),
        },
        file_extensions=["rs"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/customico/RustIcons/expui/rlib_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/customico/RustIcons/expui/rlib.svg"),
        },
        file_extensions=["rlib"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/customico/RustIcons/expui/cargo_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/customico/RustIcons/expui/cargo.svg"),
        },
        file_names=["cargo.toml"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/customico/RustIcons/expui/cargoLock_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/customico/RustIcons/expui/cargoLock.svg"),
        },
        file_names=["cargo.lock"],
    ),

]
