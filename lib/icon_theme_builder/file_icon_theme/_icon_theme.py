from __future__ import annotations as _annotations

class __:

    import pathlib as path

    from icon_theme_builder.lib import (
        IconTheme,
        exporter,
    )

# *****************************************************************************

class FileIconTheme (__.IconTheme):

    # :: PUBLIC ATTRIBUTES :: #

    hides_explorer_arrows : bool


    # :: CONSTRUCTOR :: #

    def __init__(self, icon_base_dir: __.path.Path) -> None:
        super().__init__(icon_base_dir, [
            __.exporter.FontExporter, __.exporter.ColrFontExporter
        ])

        self.hides_explorer_arrows = False

        return


    # :: INTERFACE METHODS :: #

    def export_contributions(self) -> dict:
        return {
            "iconThemes": [
                {
                    "id": self.theme_id,
                    "label": self.theme_name,
                    "path": f"./{self.theme_id}/{self.theme_id}.json"
                }
            ]
        }


    def on_export(self):
        self._theme_json["hidesExplorerArrows"] = self.hides_explorer_arrows
        return


    def on_exporter(self, exporter: __.exporter.Exporter):

        if (isinstance(exporter, __.exporter.ColrFontExporter)):
            # exporter.add_nanoemoji_args("--upem 1088 --ascender 100 --descender 0")
            # Upem larger zooms out, smaller zooms in
            # exporter.add_nanoemoji_args("--upem 925")
            # exporter.add_nanoemoji_args("--upem 928")
            exporter.add_nanoemoji_args("--upem 930")

        if (isinstance(exporter, __.exporter.FontExporter)):
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
                "size": "100%"
            }]

        return
