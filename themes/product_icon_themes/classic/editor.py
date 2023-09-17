from icon_theme_builder.product_icon_theme import *

icons = [

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/actions/intentionBulb_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/actions/intentionBulb.svg"),
        },
        ["light-bulb", "lightbulb"]
    ).as_glyf_colr_glyph(),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/actions/quickfixBulb_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/actions/quickfixBulb.svg"),
        },
        ["lightbulb-autofix"]
    ).as_glyf_colr_glyph(),

]
