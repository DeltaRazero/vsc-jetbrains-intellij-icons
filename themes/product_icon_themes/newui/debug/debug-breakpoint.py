from icon_theme_builder.product_icon_theme import *

icons = helper.all_as_colr_glyph([

    # :: BREAKPOINT NORMAL :: #

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/breakpoints/breakpoint_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/breakpoints/breakpoint.svg"),
        },
        ["debug-breakpoint", "debug-hint"]
    ).scaled(0.65),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/breakpoints/breakpointMuted_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/breakpoints/breakpointMuted.svg"),
        },
        ["debug-breakpoint-disabled"]
    ).scaled(0.65),

    # :: BREAKPOINT CONDITIONAL :: #

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/breakpoints/breakpointDependent_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/breakpoints/breakpointDependent.svg"),
        },
        ["debug-breakpoint-conditional"]
    ).scaled(0.65),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/breakpoints/breakpointMutedDependent_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/breakpoints/breakpointMutedDependent.svg"),
        },
        ["debug-breakpoint-conditional-disabled"]
    ).scaled(0.65),

    # :: BREAKPOINT DATA :: #

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/breakpoints/breakpointField_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/breakpoints/breakpointField.svg"),
        },
        ["debug-breakpoint-data"]
    ).scaled(0.65),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/breakpoints/breakpointFieldMuted_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/breakpoints/breakpointFieldMuted.svg"),
        },
        ["debug-breakpoint-data-disabled"]
    ).scaled(0.65),

    # :: BREAKPOINT FUNCTION :: #

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/breakpoints/breakpointMethod_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/breakpoints/breakpointMethod.svg"),
        },
        ["debug-breakpoint-function"]
    ).scaled(0.65),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/breakpoints/breakpointMethodMuted_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/breakpoints/breakpointMethodMuted.svg"),
        },
        ["debug-breakpoint-function-disabled"]
    ).scaled(0.65),

    # :: BREAKPOINT LOG :: #

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/breakpoints/breakpointException_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/breakpoints/breakpointException.svg"),
        },
        ["debug-breakpoint-log"]
    ).scaled(0.775),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/customico/AllIcons/expui/breakpoints/breakpointExceptionMuted_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/customico/AllIcons/expui/breakpoints/breakpointExceptionMuted.svg"),
        },
        ["debug-breakpoint-log-disabled"]
    ).scaled(0.775),

    # :: OTHER :: #

    # TODO: Maybe change with 'Unsuspendent' variant (requires custom icon for conditional breakpoint)
    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/breakpoints/questionBadge_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/breakpoints/questionBadge.svg"),
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
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/breakpoints/breakpointInvalid_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/breakpoints/breakpointInvalid.svg"),
        },
        ["debug-breakpoint-unsupported"]
    ).scaled(0.775),

])
