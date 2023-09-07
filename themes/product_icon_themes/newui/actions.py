from icon_theme_builder.product_icon_theme import *

icons = [

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/add_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/add.svg"),
        },
        ["add"]
    ),

]
