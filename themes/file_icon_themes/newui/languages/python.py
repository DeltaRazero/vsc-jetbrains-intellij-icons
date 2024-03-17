from icon_theme_builder.file_icon_theme import *

icons = [

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/customico/PythonIcons/icons/com/jetbrains/python/expui/python_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/customico/PythonIcons/icons/com/jetbrains/python/expui/python.svg"),
        },
        file_extensions=["py", "pyx"],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/customico/PythonIcons/icons/com/jetbrains/python/expui/pyCompact_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/customico/PythonIcons/icons/com/jetbrains/python/expui/pyCompact.svg"),
        },
        file_extensions=["pyc"],
    ),

    # TODO: Maybe make a custom icon?
    # icon.FileIcon(
    #     "/jetbrains/PythonIcons/icons/com/jetbrains/",
    #     file_extensions=["pyx"],
    # ),

    # TODO:
    icon.FileIcon(
        "/jetbrains/JupyterCoreIcons/icons/org.jetbrains.plugins.notebooks.jupyter/jupyterNotebook.svg",
        file_extensions=["ipynb"],
    ),

    icon.FolderIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FolderIconDefinition(
                                        "/customico/PythonIcons/icons/com/jetbrains/python/expui/pythonClosed_dark.svg",
                                        "/customico/PythonIcons/icons/com/jetbrains/python/expui/pythonClosed_dark-open.svg",
                                    ),
            ColorTheme.LIGHT       : icon.FolderIconDefinition(
                                        "/customico/PythonIcons/icons/com/jetbrains/python/expui/pythonClosed.svg",
                                        "/customico/PythonIcons/icons/com/jetbrains/python/expui/pythonClosed-open.svg",
                                    ),
        },
        ["python", "__pycache__", ".pytest_cache"]
    ),

]
