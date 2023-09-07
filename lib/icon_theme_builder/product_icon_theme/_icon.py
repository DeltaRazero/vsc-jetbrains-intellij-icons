from __future__ import annotations as _annotations

class __:

    from icon_theme_builder.lib import (
        Icon,
    )

# *****************************************************************************

class ProductIconThemeIcon (__.Icon):

    # :: CONSTRUCTOR :: #

    def __init__(self) -> None:
        super().__init__()

        # Set icon as a glyph by default as that is what VSCode needs
        self.as_glyph()
        return
