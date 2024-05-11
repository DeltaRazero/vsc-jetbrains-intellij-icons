from icon_theme_builder.product_icon_theme import *

icons = helper.all_as_glyph([

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/toolwindow/project_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/toolwindow/project.svg"),
        },
        ["files"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/search_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/search.svg"),
        },
        ["search"]
    ),

    # TODO: Make outline version
    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/DatabaseIcons/icons/expui/extension_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/DatabaseIcons/icons/expui/extension.svg"),
        },
        ["extensions"]
    ),

])
