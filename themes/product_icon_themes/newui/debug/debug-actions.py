from icon_theme_builder.product_icon_theme import *

icons = helper.all_as_colr_glyph([

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/run/resume_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/run/resume.svg"),
        },
        ["debug-continue"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/run/runWithCoverage_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/run/runWithCoverage.svg"),
        },
        ["debug-coverage"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/run/pause_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/run/pause.svg"),
        },
        ["debug-pause"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/run/rerun_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/run/rerun.svg"),
        },
        ["debug-rerun"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/run/restart_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/run/restart.svg"),
        },
        ["debug-restart"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/run/restartFrame_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/run/restartFrame.svg"),
        },
        ["debug-restart-frame"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/GoGeneratedIcons/icons/expui/resumeReverse_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/GoGeneratedIcons/icons/expui/resumeReverse.svg"),
        },
        ["debug-reverse-continue"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/run/run_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/run/run.svg"),
        },
        ["debug-start"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/customico/AllIcons/expui/run/stepInto_dark-colored.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/customico/AllIcons/expui/run/stepInto-colored.svg"),
        },
        ["debug-step-into"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/customico/AllIcons/expui/run/stepOut_dark-colored.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/customico/AllIcons/expui/run/stepOut-colored.svg"),
        },
        ["debug-step-out"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/customico/AllIcons/expui/run/stepOver_dark-colored.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/customico/AllIcons/expui/run/stepOver-colored.svg"),
        },
        ["debug-step-over"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/run/stop_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/run/stop.svg"),
        },
        ["debug-stop"]
    ),

])
