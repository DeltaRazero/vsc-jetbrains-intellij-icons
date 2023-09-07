from icon_theme_builder.file_icon_theme import *

icons = [

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/PhpIcons/icons/expui/php_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/PhpIcons/icons/expui/php.svg"),
        },
        file_extensions=["php", "php3", "php4", "php5", "phtml"],
    ),

    # TODO: todo
    icon.FolderIcon(
        (
            "/jetbrains/PhpIcons/icons/phpRuntime.svg",
            "/customico/PhpIcons/icons/phpRuntime-open.svg",
        ),
        ["php", "phpmailer"]
    ),

]
