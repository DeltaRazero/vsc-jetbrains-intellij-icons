from icon_theme_builder.file_icon_theme import *

icons = [

    icon.LanguageIdIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.LanguageIdIconDefinition("/jetbrains/DockerIcons/icons/expui/docker_dark.svg"),
            ColorTheme.LIGHT       : icon.LanguageIdIconDefinition("/jetbrains/DockerIcons/icons/expui/docker.svg"),
        },
        ["dockerfile"]
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/DockerIcons/icons/expui/docker_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/DockerIcons/icons/expui/docker.svg"),
        },
        file_names=["dockerfile"],
        file_extensions=["dockerfile"],
    ),

    # TODO: Custom icon, use mavenIgnored
    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/DockerIcons/icons/expui/dockerComposeScaledServiceStopped_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/DockerIcons/icons/expui/dockerComposeScaledServiceStopped.svg"),
        },
        file_extensions=["dockerignore"],
    ),

    icon.LanguageIdIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.LanguageIdIconDefinition("/jetbrains/DockerIcons/icons/expui/dockerCompose_dark.svg"),
            ColorTheme.LIGHT       : icon.LanguageIdIconDefinition("/jetbrains/DockerIcons/icons/expui/dockerCompose.svg"),
        },
        ["dockercompose"]
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/DockerIcons/icons/expui/dockerCompose_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/DockerIcons/icons/expui/dockerCompose.svg"),
        },
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
