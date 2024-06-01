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

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/DatabaseIcons/icons/expui/connector_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/DatabaseIcons/icons/expui/connector.svg"),
        },
        ["extensions"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/vcs/vcs_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/vcs/vcs.svg"),
        },
        ["source-control"]
    ),

    ProductIcon(
        "/customico/AllIcons/expui/toolwindow/referencesScan_stroke.svg",
        ["references"]
    ),

])
