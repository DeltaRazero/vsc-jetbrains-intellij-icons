from icon_theme_builder.file_icon_theme import *

icons = [

    # TODO: Make directory icons for models, views, controllers, migrations
    # TODO: Make file icons for migrations

    icon.FolderIcon(
        (
            "/jetbrains/MpsIcons53/nodes/model.svg",
            "/jetbrains/MpsIcons53/nodes/model.svg", # TODO: Open Icon
        ),
        ["model", "models"],
    ),

    icon.FolderIcon(
        (
            "/jetbrains/MpsIcons22/migrationModel.svg",
            "/jetbrains/MpsIcons22/migrationModel.svg", # TODO: Open Icon
        ),
        ["migration", "migrations"],
    ),

    icon.FolderIcon(
        (
            "/jetbrains/AllIcons/nodes/webFolder.svg",
            "/customico/AllIcons/nodes/webFolder-open.svg",
        ),
        helper.name_combinations(["web", "website", "www", "wwwroot", "public"], [".", "_"])
    ),

]
