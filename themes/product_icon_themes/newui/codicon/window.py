from icon_theme_builder.product_icon_theme import *

icons = helper.all_as_glyph([

    # TODO: Is this right? Maybe use openNewTab
    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AquaWIIcons/icons/toolwindow/expui/openInNewWindow_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AquaWIIcons/icons/toolwindow/expui/openInNewWindow.svg"),
        },
        ["empty-window"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/windows/close_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/windows/close.svg"),
        },
        ["chrome-close"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/windows/maximize_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/windows/maximize.svg"),
        },
        ["chrome-maximize"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/windows/minimize_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/windows/minimize.svg"),
        },
        ["chrome-minimize"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/windows/restore_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/windows/restore.svg"),
        },
        ["chrome-restore"]
    ),

    # TODO: Custom icon
    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/windows/restore_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/windows/restore.svg"),
        },
        ["window"]
    ),

])
