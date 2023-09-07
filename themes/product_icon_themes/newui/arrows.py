from icon_theme_builder.product_icon_theme import *

icons = helper.all_as_glyph([

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/down_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/down.svg"),
        },
        ["arrow-down"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/left_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/left.svg"),
        },
        ["arrow-left"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/right_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/right.svg"),
        },
        ["arrow-right"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/up_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/up.svg"),
        },
        ["arrow-up"]
    ),

    # TODO: arrow-circle

    # TODO: arrow-small

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/customico/AllIcons/expui/general/swap_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/customico/AllIcons/expui/general/swap.svg"),
        },
        ["arrow-swap"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/chevronDown_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/chevronDown.svg"),
        },
        ["chevron-down"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/chevronLeft_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/chevronLeft.svg"),
        },
        ["chevron-left"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/chevronRight_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/chevronRight.svg"),
        },
        ["chevron-right"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/chevronUp_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/chevronUp.svg"),
        },
        ["chevron-up"]
    ),

])
