
class __:

    import abc
    import pathlib as path

    from .._icon_properties import IconProperties

# *****************************************************************************

class Exporter (__.abc.ABC):

    # :: PRIVATE ATTRIBUTES :: #

    _icon_base_dir : __.path.Path | None
    _has_icons : bool


    # :: CONSTRUCTOR :: #

    def __init__(self) -> None:
        self._icon_base_dir = None
        self._has_icons = False
        return


    # :: PUBLIC METHODS :: #

    @__.abc.abstractmethod
    def add_icon(self, icon_fp: str, properties: __.IconProperties) -> None:
        ...


    def set_icon_base_dir(self, dir: __.path.Path) -> None:
        self._icon_base_dir = dir
        return


    @__.abc.abstractmethod
    def consolidate(self, dist_dir: __.path.Path) -> dict:
        ...


    def has_icons(self) -> bool:
        return self._has_icons


    # :: PROTECTED METHODS :: #

    def _fp(self, fp: str | __.path.Path) -> __.path.Path:
        self._has_icons = True # Bit of a cheat to set it here, but whatever
        if (isinstance(fp, str)):
            fp = __.path.Path(fp)
        if (self._icon_base_dir is None):
            raise RuntimeError("Icon base directory not set!")
        fp = self._icon_base_dir / str(fp).lstrip('/')
        if (not fp.exists()):
            raise RuntimeError(f"The filepath \"{fp}\" does not exist!")
        return fp
