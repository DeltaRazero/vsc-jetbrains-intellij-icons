from icon_theme_builder.file_icon_theme import *

icons = [

    icon.LanguageIdIcon(
        "/customico/AllIcons/expui/fileTypes/htaccess.svg",
        ["apacheconf"]
    ),

    icon.FileIcon(
        "/customico/AllIcons/expui/fileTypes/htaccess.svg",
        file_extensions=["htaccess", "htgroups", "htpasswd"],
    ),

]
