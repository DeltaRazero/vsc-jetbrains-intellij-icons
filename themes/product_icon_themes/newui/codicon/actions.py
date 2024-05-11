from icon_theme_builder.product_icon_theme import *

icons = helper.all_as_glyph([

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/add_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/add.svg"),
        },
        ["add", "plus"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/close_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/close.svg"),
        },
        ["close", "remove-close", "x"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/expandAll_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/expandAll.svg"),
        },
        ["expand-all"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/export_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/export.svg"),
        },
        ["export"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/customico/AllIcons/expui/general/filter_dark-filled.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/customico/AllIcons/expui/general/filter-filled.svg"),
        },
        ["filter-filled"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/filter_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/filter.svg"),
        },
        ["filter"]
    ),

])
