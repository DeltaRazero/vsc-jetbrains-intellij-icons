from icon_theme_builder.product_icon_theme import *

icons = helper.all_as_colr_glyph([

    # :: BREAKPOINT NORMAL :: #

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/debugger/db_set_breakpoint_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/debugger/db_set_breakpoint.svg"),
        },
        ["debug-breakpoint", "debug-hint"]
    ).scaled(0.65),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/debugger/db_muted_breakpoint_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/debugger/db_muted_breakpoint.svg"),
        },
        ["debug-breakpoint-disabled"]
    ).scaled(0.65),

    # :: BREAKPOINT CONDITIONAL :: #

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/debugger/db_dep_line_breakpoint_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/debugger/db_dep_line_breakpoint.svg"),
        },
        ["debug-breakpoint-conditional"]
    ).scaled(0.65),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/debugger/db_muted_dep_line_breakpoint_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/debugger/db_muted_dep_line_breakpoint.svg"),
        },
        ["debug-breakpoint-conditional-disabled"]
    ).scaled(0.65),

    # :: BREAKPOINT DATA :: #

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/debugger/db_field_breakpoint_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/debugger/db_field_breakpoint.svg"),
        },
        ["debug-breakpoint-data"]
    ).scaled(0.65),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/debugger/db_muted_field_breakpoint_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/debugger/db_muted_field_breakpoint.svg"),
        },
        ["debug-breakpoint-data-disabled"]
    ).scaled(0.65),

    # :: BREAKPOINT FUNCTION :: #

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/debugger/db_method_breakpoint_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/debugger/db_method_breakpoint.svg"),
        },
        ["debug-breakpoint-function"]
    ).scaled(0.65),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/debugger/db_muted_method_breakpoint_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/debugger/db_muted_method_breakpoint.svg"),
        },
        ["debug-breakpoint-function-disabled"]
    ).scaled(0.65),

    # :: BREAKPOINT LOG :: #

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/debugger/db_exception_breakpoint_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/debugger/db_exception_breakpoint.svg"),
        },
        ["debug-breakpoint-log"]
    ).scaled(0.775),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/customico/AllIcons/debugger/db_muted_exception_breakpoint_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/customico/AllIcons/debugger/db_muted_exception_breakpoint.svg"),
        },
        ["debug-breakpoint-log-disabled"]
    ).scaled(0.775),

    # :: OTHER :: #

    # TODO: Maybe change with 'Unsuspendent' variant (requires custom icon for conditional breakpoint)
    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/debugger/question_badge_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/debugger/question_badge.svg"),
        },
        helper.name_combinations(
            [
                "debug-breakpoint",
                "debug-breakpoint-conditional",
                "debug-breakpoint-data",
                "debug-breakpoint-function",
                "debug-breakpoint-log",
            ],
            suffixes=["-unverified"],
            include_empty=False
        )
    ).scaled(0.775),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/debugger/db_invalid_breakpoint_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/debugger/db_invalid_breakpoint.svg"),
        },
        ["debug-breakpoint-unsupported"]
    ).scaled(0.775),

])
