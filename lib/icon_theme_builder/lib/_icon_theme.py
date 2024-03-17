from __future__ import annotations as _annotations

class __:

    import abc
    import pathlib as path
    import json
    import typing as t

    import deepmerge

    from . import (
        exporter,
        util,
    )

# *****************************************************************************

class IconTheme (__.abc.ABC):

    # :: PUBLIC ATTRIBUTES :: #

    theme_id   : str
    theme_name : str


    # :: PROTECTED ATTRIBUTES :: #

    _exporters : __.exporter.ExportersType


    # :: PRIVATE ATTRIBUTES :: #

    _package_json_partial : dict
    _theme_json : dict

    _unique : bool


    # :: CONSTRUCTOR :: #

    @__.abc.abstractmethod
    def __init__(self, icon_base_dir: __.path.Path, enabled_exporters: list[__.t.Type[__.exporter.Exporter]]) -> None:
        self.theme_id   = __.util.generate_uid(5)
        self.theme_name = ""

        self._exporters = {}
        for exporter_t in list(set(enabled_exporters)):
            exporter = exporter_t()
            exporter.set_icon_base_dir(icon_base_dir)
            self._exporters |= {
                exporter_t : exporter
            }

        self._theme_json = {}
        self._package_json_partial = {}

        self._unique = False
        return


    # :: ABSTRACT METHODS :: #

    @__.abc.abstractmethod
    def export_contributions(self) -> dict:
        ...


    def on_exporter(self, exporter: __.exporter.Exporter):
        pass


    def on_export(self):
        pass


    # :: PUBLIC METHODS :: #

    def add_to_theme_json(self, json: dict, default_icon_reused: bool) -> None:
        __.deepmerge.always_merger.merge(self._theme_json, json) # TODO: Print warning or throw error if key already exists
        self._unique |= not default_icon_reused
        return


    def export(self, dist_dir: __.path.Path, validate_only: bool):

        theme_dist_dir = (dist_dir / self.theme_id).resolve()
        theme_dist_dir.mkdir(exist_ok=True)

        # Don't export if not unique
        if (not self._unique): return

        for exporter in self._exporters.values():
            if (exporter is None or not exporter.has_icons()):
                continue
            self.on_exporter(exporter)
            if (not validate_only):
                exporter.consolidate(theme_dist_dir)

        self._package_json_partial["contributes"] = __.deepmerge.always_merger.merge(
            self._package_json_partial.get("contributes", {}),
            self.export_contributions()
        )

        self.on_export()

        # Dump the theme json definition file
        with open(theme_dist_dir / f'{self.theme_id}.json', 'w') as f:
            __.json.dump(self._theme_json, f, separators=(',', ':'))

        # Dump the package json partial file, merged by bin/make_dist.py
        with open(theme_dist_dir / "package.partial.json", 'w') as f:
            __.json.dump(self._package_json_partial, f, separators=(',', ':'))

        return


    # :: GETTERS :: #

    def get_exporters(self) -> __.exporter.ExportersType:
        return self._exporters


    def is_unique(self) -> bool:
        return self._unique
