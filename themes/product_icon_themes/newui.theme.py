from icon_theme_builder.product_icon_theme import *

theme = ProductIconThemeBuilder(
    ProductIconThemeArgs(
        theme_module  = __file__,
        theme_name    = "IntelliJ Product Icon Theme (NewUI)",
        icon_base_dir = "../../resources/icons",
    )
)

def add_icons(fp: str):
    [theme.add_icon(icon) for icon in theme.find_icons(fp)]

# *****************************************************************************

add_icons("./newui")
