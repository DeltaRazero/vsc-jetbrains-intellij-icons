#!/usr/local/bin/python

class __:

    import argparse
    import importlib.util
    import json
    import os
    import pathlib as path
    import shutil
    import sys
    import traceback

    import deepmerge

    from icon_theme_builder.lib import IconThemeBuilder

# *****************************************************************************

REPO_ROOT     = __.path.Path(__file__).parent / ".."
THEMES_FOLDER = REPO_ROOT / "themes"
DIST_FOLDER   = REPO_ROOT / "dist"
EXTENSION_DIR = REPO_ROOT / "extension"
TMP_FOLDER    = __.path.Path("/tmp/glyph_fonts")

# *****************************************************************************

def export_theme(py_file: __.path.Path) -> None:

    spec = __.importlib.util.spec_from_file_location("theme_module", str(py_file))
    if (spec is None):
        raise IOError("Not a Python file!")

    theme_module = __.importlib.util.module_from_spec(spec)
    if (spec.loader is None):
        raise IOError("Not a Python file!")

    __.sys.modules["theme_module"] = theme_module
    spec.loader.exec_module(theme_module)

    for var_name, var_value in vars(theme_module).items():
        if var_name.startswith("_"): continue
        match var_value:
            case __.IconThemeBuilder():
                var_value.export(DIST_FOLDER, args.validate_only)

    return


def process_theme_modules(base_folder: __.path.Path) -> None:

    for py_file in base_folder.glob("*theme.py"):
        if py_file.name.startswith("_"): continue
        export_theme(py_file)

    for sub_dir in [sub_dir for sub_dir in base_folder.iterdir() if sub_dir.is_dir()]:
        if (sub_dir.name == "__pycache__" or sub_dir.name.startswith("_")):
            continue
        process_theme_modules(sub_dir)

    return


def consolidate(extension_dir: __.path.Path, dist_folder: __.path.Path) -> None:

    package_json = {}
    for folder in [folder for folder in dist_folder.iterdir() if folder.is_dir()]:
        for file in folder.glob("package.partial.json"):

            with open(file, 'r') as f:
                __.deepmerge.always_merger.merge(package_json, __.json.load(f))

    # Copy all items from extension folder
    for fp in extension_dir.iterdir():
        __.shutil.copy(
            fp,
            dist_folder / fp.name
        )

    # Merge package.json
    with open(extension_dir / "package.json", 'r') as f:
        __.deepmerge.always_merger.merge(package_json, __.json.load(f))
    with open(dist_folder / "package.json", 'w') as f:
        __.json.dump(package_json, f, separators=(',', ':'))

    # Make extension VSIX
    cmd = f'cd "{dist_folder}" && vsce package'
    with __.os.popen(cmd) as vsce_p:
        vsce_p.read()

    return


# *****************************************************************************

def main() -> int:
    global args

    parser = __.argparse.ArgumentParser()
    parser.add_argument("--validate-only", action="store_true")
    args = parser.parse_args()

    try:
        if (TMP_FOLDER.exists()):
            __.shutil.rmtree(TMP_FOLDER)
        if (DIST_FOLDER.exists()):
            __.shutil.rmtree(DIST_FOLDER)
        DIST_FOLDER.mkdir()

        process_theme_modules(THEMES_FOLDER)
        if (args.validate_only):
            if (DIST_FOLDER.exists()):
                __.shutil.rmtree(DIST_FOLDER)
        else:
            consolidate(EXTENSION_DIR, DIST_FOLDER)
    except:
        if (DIST_FOLDER.exists()):
            __.shutil.rmtree(DIST_FOLDER)
        print("Making distribution aborted because of the following error:")
        __.traceback.print_exc()
        return -1

    return 0

# *****************************************************************************

if __name__ == "__main__":
    __.sys.exit(main())
