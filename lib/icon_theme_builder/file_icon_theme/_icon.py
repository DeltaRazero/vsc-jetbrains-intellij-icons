from __future__ import annotations as _annotations

class __:

    from icon_theme_builder.lib import (
        Icon,
        ColorTheme,
        util,
    )

# *****************************************************************************

class FileIconThemeIcon (__.Icon):

    # :: PRIVATE ATTRIBUTES :: #

    _id : str
    _as_default : bool


    # :: CONSTRUCTOR :: #

    def __init__(self, id: str | None) -> None:
        super().__init__()

        self._id = id or __.util.generate_uid(10)
        self._as_default = False
        return


    # :: PUBLIC METHODS :: #

    def get_id(self, color_theme: __.ColorTheme) -> str:
        id = self._id
        match color_theme:
            case __.ColorTheme.DEFAULT_DARK:
                id = f'{id}'
            case __.ColorTheme.LIGHT:
                id = f'{id}-light'
            case __.ColorTheme.CONTRAST:
                id = f'{id}-contrast'
        return id


class DefaultableFileIconThemeIcon (FileIconThemeIcon):

    # :: PUBLIC METHODS :: #

    def as_default(self) -> 'FileIconThemeIcon':
        """Discards any set names."""
        self._as_default = True
        return self
