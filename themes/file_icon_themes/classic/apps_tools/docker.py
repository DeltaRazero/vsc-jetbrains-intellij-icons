from icon_theme_builder.file_icon_theme import *

icons = [

    icon.FileIcon(
        "/jetbrains/DockerIcons/icons/DockerFile_1.svg",
        file_names=["dockerfile"],
        file_extensions=["dockerfile"],
    ),

    # TODO: Custom icon
    icon.FileIcon(
        "/jetbrains/DockerIcons/icons/DockerFile_1.svg",
        file_extensions=["dockerignore"],
    ),

    icon.FileIcon(
        "/jetbrains/DockerIcons/icons/DockerComposeFile.svg",
        file_names=helper.name_combinations(
            helper.name_combinations(
                ["docker-compose"],
                suffixes=[
                    ".dev",
                    ".development",
                    ".prod",
                    ".production",
                    ".test",
                    ".local",
                    ".ci",
                    ".override",
                    ".staging",
                ],
            ),
            suffixes=[".yml", ".yaml"],
            include_empty=False
        )
    ),

]
