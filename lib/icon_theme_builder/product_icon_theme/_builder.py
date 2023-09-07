
class __:

    import dataclasses

    from icon_theme_builder.lib import (
        IconThemeBuilder,
        Icon,
        ColorTheme,
        IconTheme,
        IconThemeBuilderArgs,
    )

    from ._icon_theme import ProductIconTheme
    from ._icon import ProductIconThemeIcon

# *****************************************************************************

@__.dataclasses.dataclass(kw_only=True)
class ProductIconThemeArgs (__.IconThemeBuilderArgs):
    pass

# *****************************************************************************

class ProductIconThemeBuilder (__.IconThemeBuilder):

    # :: PRIVATE ATTRIBUTES :: #

    _product_icon_theme_args : ProductIconThemeArgs


    # :: CONSTRUCTOR :: #

    def __init__(self, args: ProductIconThemeArgs) -> None:
        super().__init__(args)
        self._product_icon_theme_args = args
        return


    # :: INTERFACE METHODS :: #

    def is_correct_icon_type(self, icon: __.Icon) -> bool:
        return isinstance(icon, __.ProductIconThemeIcon)


    # :: PUBLIC METHODS :: #

    def on_export(self) -> list[__.IconTheme]:

        themes: list[__.IconTheme] = []

        for color_theme in __.ColorTheme:
            theme = __.ProductIconTheme(self._icon_theme_builder_args.get_icon_base_path())

            color_theme_name = {
                __.ColorTheme.DEFAULT_DARK: 'dark',
                __.ColorTheme.LIGHT       : 'light',
                __.ColorTheme.CONTRAST    : 'contrast',
            }[color_theme]
            theme.theme_name = f'{self._icon_theme_builder_args.theme_name} [{color_theme_name}]'

            for icon in self._icons:
                icon.add_to_theme(theme, color_theme)

            if (theme.is_unique()):
                themes.append(theme)

        # If no specific color theme variants, then just remove the title specifier
        if (len(themes) == 1):
            themes[0].theme_name = self._icon_theme_builder_args.theme_name

        # Return only unique themes
        return themes
