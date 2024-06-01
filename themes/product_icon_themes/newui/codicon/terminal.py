from icon_theme_builder.product_icon_theme import *

icons = helper.all_as_glyph([


    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/TerminalIcons/icons/expui/toolwindow/terminal_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/TerminalIcons/icons/expui/toolwindow/terminal.svg"),
        },
        ["console"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/TerminalIcons/icons/expui/toolwindow/terminal_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/TerminalIcons/icons/expui/toolwindow/terminal.svg"),
        },
        ["repl"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/TerminalIcons/icons/expui/toolwindow/terminal_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/TerminalIcons/icons/expui/toolwindow/terminal.svg"),
        },
        ["terminal"]
    ),

])
