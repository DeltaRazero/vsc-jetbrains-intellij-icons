
class __:

    import dataclasses

    from icon_theme_builder.lib import (
        IconThemeBuilder,
        Icon,
        ColorTheme,
        IconTheme,
        IconThemeBuilderArgs,
    )

    from ._icon_theme import FileIconTheme
    from ._icon import FileIconThemeIcon

# *****************************************************************************

@__.dataclasses.dataclass(kw_only=True)
class FileIconThemeArgs (__.IconThemeBuilderArgs):

    variant_with_explorer_arrows    : bool=False
    variant_without_explorer_arrows : bool=True

# *****************************************************************************

class FileIconThemeBuilder (__.IconThemeBuilder):

    # :: PRIVATE ATTRIBUTES :: #

    _file_icon_theme_args : FileIconThemeArgs


    # :: CONSTRUCTOR :: #

    def __init__(self, args: FileIconThemeArgs) -> None:
        super().__init__(args)
        self._file_icon_theme_args = args
        return


    # :: INTERFACE METHODS :: #

    def is_correct_icon_type(self, icon: __.Icon) -> bool:
        return isinstance(icon, __.FileIconThemeIcon)


    # :: PUBLIC METHODS :: #

    def on_export(self) -> list[__.IconTheme]:

        themes: list[__.IconTheme] = []
        variants = [
            self._file_icon_theme_args.variant_without_explorer_arrows,
            self._file_icon_theme_args.variant_with_explorer_arrows
        ]
        for is_arrow_variant, enable_variant in enumerate(variants):
            if not (enable_variant): continue

            theme = __.FileIconTheme(self._icon_theme_builder_args.get_icon_base_path())

            append_arrow_postfix = not (variants[0] and variants[1]) and is_arrow_variant
            theme.theme_name = f'{self._file_icon_theme_args.theme_name}{" [exp-arrows]" if append_arrow_postfix else ""}'

            theme.hides_explorer_arrows = not bool(is_arrow_variant)

            for icon in self._icons:
                for color_theme in __.ColorTheme:
                    icon.add_to_theme(theme, color_theme)

            if (theme.is_unique()):
                themes.append(theme)

        return themes
