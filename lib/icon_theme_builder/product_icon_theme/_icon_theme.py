from __future__ import annotations as _annotations

class __:

    import pathlib as path

    from icon_theme_builder.lib import (
        IconTheme,
        exporter,
    )

# *****************************************************************************

class ProductIconTheme (__.IconTheme):

    # :: CONSTRUCTOR :: #

    def __init__(self, icon_base_dir: __.path.Path) -> None:
        super().__init__(icon_base_dir, [
            __.exporter.FontExporter,
            __.exporter.GlyfColrFontExporter,
            __.exporter.CbdtColrFontExporter,
        ])

        return


    # :: INTERFACE METHODS :: #

    def export_contributions(self) -> dict:
        return {
            "productIconThemes": [
                {
                    "id": self.theme_id,
                    "label": self.theme_name,
                    "path": f"./{self.theme_id}/{self.theme_id}.json"
                }
            ]
        }


    def on_exporter(self, exporter: __.exporter.Exporter):

        if (not isinstance(exporter, __.exporter.FontExporter)):
            raise ValueError("Only glyph exporters allowed!")

        # VSCode does some weird scaling and positioning of product icon fonts generated with nanoemoji, so these options fix that
        if (isinstance(exporter, __.exporter.ColrFontExporter)):
            exporter.add_nanoemoji_args("--upem 1792 --ascender=1700 --descender=-100")

        self._theme_json["fonts"] = self._theme_json.get("fonts", []) + [{
            "id": exporter.get_font_id(),
            "src": [
                {
                    "path": f'./{exporter.get_font_id()}.woff2',
                    "format": "woff2"
                }
            ],
            "weight": "normal",
            "style": "normal",
            "size": "100%" # TODO: Not supported?
        }]

        return
