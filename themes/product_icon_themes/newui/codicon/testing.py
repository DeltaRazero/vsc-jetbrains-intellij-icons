from icon_theme_builder.product_icon_theme import *

icons = helper.all_as_glyph([

    ProductIcon(
        {
            # ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/toolwindow/coverage_dark.svg"),
            # ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/toolwindow/coverage.svg"),
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/customico/AllIcons/expui/toolwindow/test_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/customico/AllIcons/expui/toolwindow/test.svg"),
        },
        ["beaker"]
    ),

])
