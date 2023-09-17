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
            raise Exception("Only glyph exporters allowed!")

        if (isinstance(exporter, __.exporter.ColrFontExporter)):
            # exporter.add_nanoemoji_args("--upem 1088 --ascender 100 --descender 0")
            # exporter.add_nanoemoji_args("--upem 1135 --transform \"translate(0, -0.5)\"")
            # exporter.add_nanoemoji_args("--upem 1136")
            exporter.add_nanoemoji_args("--upem 1144")
            # exporter.add_nanoemoji_args("--upem 1152")
            # exporter.add_nanoemoji_args("--upem 1184")
            # exporter.add_nanoemoji_args("--upem 1584")
            # pass

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
