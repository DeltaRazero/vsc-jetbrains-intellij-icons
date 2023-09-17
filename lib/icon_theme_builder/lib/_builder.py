
class __:

    import abc
    import pathlib as path
    import os
    import importlib.util
    import sys
    import dataclasses

    from ._icon       import Icon
    from ._icon_theme import IconTheme

# *****************************************************************************

@__.dataclasses.dataclass(kw_only=True, init=False)
class IconThemeBuilderArgs (__.abc.ABC):

    theme_module: str # Filepath
    """Filepath to the theme module file. Should be passed as `__file__`."""

    theme_name : str
    """Name of the icon theme."""

    icon_base_dir : str | None=None
    """Absolute or relative path. If not given, is relative to this directory."""


    def get_theme_path(self) -> __.path.Path:
        return __.path.Path(self.theme_module).parent


    def get_icon_base_path(self) -> __.path.Path:
        match self.icon_base_dir:
            case str():
                path = __.path.Path(self.icon_base_dir)
                if (path.is_absolute() and path.exists()):
                    return path
                else:
                    return (self.get_theme_path() / path).resolve()
        return self.get_theme_path()

# *****************************************************************************

class IconThemeBuilder (__.abc.ABC):

    # :: PRIVATE ATTRIBUTES :: #

    _icons  : list[__.Icon]


    # :: PROTECTED ATTRIBUTES :: #

    _icon_theme_builder_args : IconThemeBuilderArgs


    # :: CONSTRUCTOR :: #

    @__.abc.abstractmethod
    def __init__(self, icon_theme_builder_args: IconThemeBuilderArgs) -> None:
        self._icon_theme_builder_args = icon_theme_builder_args

        self._icons  = []
        return


    # :: INTERFACE METHODS :: #

    @__.abc.abstractmethod
    def is_correct_icon_type(self, icon: __.Icon) -> bool:
        ...


    @__.abc.abstractmethod
    def on_export(self) -> list[__.IconTheme]:
        ...


    def export(self, dist_dir: __.path.Path) -> None:
        dist_dir.mkdir(exist_ok=True, parents=True)

        themes = self.on_export()
        if not (themes):
            raise Exception("Expected at least one (1) theme!")

        for theme in themes:
            theme.export(dist_dir)

        return


    # :: PUBLIC METHODS :: #

    def add_icon(self, icon: __.Icon):
        if not (self.is_correct_icon_type(icon)):
            raise Exception("Not correct icon type!")
        self._icons.append(icon)
        return


    def add_icons(self, icons: list[__.Icon]) -> None:
        """Adds icons"""
        for icon in icons:
            self.add_icon(icon)
        return


    def find_icons(self, path: str | __.path.Path) -> list[__.Icon]:
        """Recursively finds icons in modules."""

        if (isinstance(path, str)):
            path = __.path.Path(path) if __.os.path.isabs(path) \
                                      else self._icon_theme_builder_args.get_theme_path() / path

        icons = []

        if (path.is_file() and path.suffix == ".py"):
            icons.extend(self._import_icons_from_module(path))
        elif (path.is_dir()):
            if (path.name.startswith("_")):
                return icons

            for py_file in path.glob("*.py"):
                if (py_file.name.startswith("_")):
                    continue
                icons.extend(self._import_icons_from_module(py_file))

            for sub_dir in [sub_dir for sub_dir in path.iterdir() if sub_dir.is_dir()]:
                if (sub_dir.name == "__pycache__" or sub_dir == self._icon_theme_builder_args.get_theme_path()):
                    continue
                icons += self.find_icons(sub_dir)
        else:
            raise RuntimeError("Not a valid filepath or file does not exist!")

        return icons

    # :: PROTECTED METHODS :: #

    def _as_id(self, string: str) -> str:
        return '-'.join(
            list(filter(
                None, __.re.sub('[^0-9a-zA-Z]+', ' ', string).split(' ')
            ))
        ).lower()


    # :: PRIVATE METHODS :: #

    def _import_icons_from_module(self, py_file: __.path.Path) -> list[__.Icon]:

        spec = __.importlib.util.spec_from_file_location("icons_module", str(py_file))
        if (spec is None):
            raise Exception("Not a Python file!")

        icons_module = __.importlib.util.module_from_spec(spec)
        if (spec.loader is None):
            raise Exception("Not a Python file!")

        __.sys.modules["icons_module"] = icons_module
        spec.loader.exec_module(icons_module)

        icons = []
        for var_name, var_value in vars(icons_module).items():
            if var_name.startswith("_"): continue
            match var_value:
                case __.Icon():
                    icons.append(var_value)
                case list():
                    for value in var_value:
                        if isinstance(value, __.Icon): icons.append(value)

        return icons
