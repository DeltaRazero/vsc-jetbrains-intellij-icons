from icon_theme_builder.file_icon_theme import *

icons = [

    # TODO: todo

    icon.LanguageIdIcon(
        "/customico/RIcons/icons/rFile.svg",
        language_ids=["r"],
    ),

    icon.FileIcon(
        "/customico/RIcons/icons/rFile.svg",
        file_extensions=["r"],
    ),

    icon.FileIcon(
        "/jetbrains/RIcons/icons/fileTypes/rMarkdown.svg",
        file_extensions=["rmd"],
    ),

    icon.FileIcon(
        "/customico/RIcons/icons/r-bigger.svg",
        file_extensions=["rdata", "rds", "rda"],
    ),


]
