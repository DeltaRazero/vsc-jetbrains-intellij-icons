
class __:

    import itertools

    from ._icon import Icon

# *****************************************************************************

def name_combinations(names: list[str], prefixes: list[str] | None=None, suffixes: list[str] | None=None, include_empty: bool=True) -> list[str]:
    """Returns a list of name combinations."""

    prefixes = (prefixes or []) + ([''] if include_empty or not prefixes else [])
    suffixes = (suffixes or []) + ([''] if include_empty or not suffixes else [])

    combinations = [
        f"{prefix}{name}{suffix}" for name, prefix, suffix in __.itertools.product(names, prefixes, suffixes)
    ]
    return combinations

def all_as_glyph(icons: list[__.Icon]) -> list[__.Icon]:
    return [icon.as_glyph() for icon in icons]

def all_as_colr_glyph(icons: list[__.Icon]) -> list[__.Icon]:
    return [icon.as_glyf_colr_glyph() for icon in icons]
