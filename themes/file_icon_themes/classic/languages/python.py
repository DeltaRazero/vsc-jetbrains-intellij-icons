from icon_theme_builder.file_icon_theme import *

icons = [

    icon.FileIcon(
        "/jetbrains/PythonPsiApiIcons/icons/com/jetbrains/python/pythonFile.svg",
        file_extensions=["py", "pyx"],
    ),

    icon.FileIcon(
        "/customico/PythonIcons/icons/com/jetbrains/python/pyCompact.svg",
        file_extensions=["pyc"],
    ),

    # TODO: Maybe make a custom icon?
    # icon.FileIcon(
    #     "/jetbrains/PythonIcons/icons/com/jetbrains/",
    #     file_extensions=["pyx"],
    # ),

    icon.FileIcon(
        "/jetbrains/JupyterCoreIcons/icons/org.jetbrains.plugins.notebooks.jupyter/jupyterNotebook.svg",
        file_extensions=["ipynb"],
    ),

    icon.FolderIcon(
        (
            "/jetbrains/PythonIcons/icons/com/jetbrains/python/pythonClosed.svg",
            "/customico/PythonIcons/icons/com/jetbrains/python/pythonClosed-open.svg",
        ),
        ["python", "__pycache__", ".pytest_cache"]
    ),

]
