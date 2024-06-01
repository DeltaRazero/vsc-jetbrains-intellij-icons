from icon_theme_builder.product_icon_theme import *

icons = helper.all_as_glyph([

    ProductIcon(
        "/customico/AllIcons/expui/run/runAll_stroke.svg",
        ["debug-all"]
    ),

    ProductIcon(
        "/customico/AllIcons/expui/run/debug_stroke_fixed.svg",
        ["debug", "debug-alt"]
    ),

    ProductIcon(
        "/customico/AllIcons/expui/run/debug_stroke_fixed.svg",
        ["debug-alt-small"]
    ).scaled(0.75),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/run/resume_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/run/resume.svg"),
        },
        ["debug-all"]
    ),

    ProductIcon(
        "/customico/AllIcons/expui/run/debugConsole_stroke.svg",
        ["debug-console"]
    ),

    ProductIcon(
        "/customico/SerialMonitorIcons/icons/expui/disconnectedSerial_stroke.svg",
        ["debug-disconnect"]
    ),

    ProductIcon(
        "/customico/AllIcons/expui/run/debugLineByLine_stroke.svg",
        ["debug-line-by-line"]
    ),

    ProductIcon(
        "/customico/AllIcons/expui/run/muteBreakpoints_stroke.svg",
        ["activate-breakpoints"]
    ),

])
