from icon_theme_builder.file_icon_theme import *

icons = [

    icon.FileIcon(
        "/jetbrains/PhpIcons/icons/php-icon.svg",
        file_extensions=["php", "php3", "php4", "php5", "phtml"],
    ),

    icon.FolderIcon(
        (
            "/jetbrains/PhpIcons/icons/phpRuntime.svg",
            "/customico/PhpIcons/icons/phpRuntime-open.svg",
        ),
        ["php", "phpmailer"]
    ),

]
