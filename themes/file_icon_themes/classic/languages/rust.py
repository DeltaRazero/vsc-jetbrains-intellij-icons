from icon_theme_builder.file_icon_theme import *

icons = [

    icon.FileIcon(
        "/customico/RustIcons/rustFile.svg",
        file_extensions=["rs"],
    ),

    icon.FileIcon(
        "/customico/RustIcons/rlib.svg",
        file_extensions=["rlib"],
    ),

    icon.FileIcon(
        "/customico/RustIcons/cargo_center.svg",
        file_names=["cargo.toml"],
    ),

    icon.FileIcon(
        "/customico/RustIcons/cargoLock_center.svg",
        file_names=["cargo.lock"],
    ),

]
