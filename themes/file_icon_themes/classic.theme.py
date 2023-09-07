from icon_theme_builder.file_icon_theme import *

theme = FileIconThemeBuilder(
    FileIconThemeArgs(
        theme_module  = __file__,
        theme_name    = "IntelliJ File Icon Theme (Classic)",
        icon_base_dir = "../../resources/icons",
        variant_with_explorer_arrows    = False,
        variant_without_explorer_arrows = True
    )
)

def add_icons(fp: str):
    [theme.add_icon(icon) for icon in helper.all_as_colr_glyph(theme.find_icons(fp))]

# *****************************************************************************

add_icons("./classic")
