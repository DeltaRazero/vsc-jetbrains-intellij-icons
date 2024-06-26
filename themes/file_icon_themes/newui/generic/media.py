from icon_theme_builder.file_icon_theme import *

icons = [

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/diagram_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/diagram.svg"),
        },
        file_extensions=[
            "dio",
            "drawio",
            "iuml",
            "plantuml",
            "pu",
            "puml",
            "wsd",
        ],
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/csv_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/csv.svg"),
        },
        file_extensions=[
            "csv",
            "tsv",
        ]
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/customico/AllIcons/expui/fileTypes/writer_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/customico/AllIcons/expui/fileTypes/writer.svg"),
        },
        file_extensions=["odt", "fodt"]
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/csv_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/csv.svg"),
        },
        file_extensions=["ods", "fods"]
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/customico/AllIcons/expui/fileTypes/impress_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/customico/AllIcons/expui/fileTypes/impress.svg"),
        },
        file_extensions=["odp", "fopd"]
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/customico/AllIcons/expui/fileTypes/writer_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/customico/AllIcons/expui/fileTypes/writer.svg"),
        },
        file_extensions=[
            "doc",
            "docm",
            "docx",
            "dot",
            "dotm",
            "dotx",
        ]
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/csv_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/csv.svg"),
        },
        file_extensions=[
            "xla",
            "xlam",
            "xls",
            "xlsb",
            "xlsm",
            "xlsx",
            "xlt",
            "xltm",
            "xltx",
            "xlw",
        ]
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/customico/AllIcons/expui/fileTypes/impress_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/customico/AllIcons/expui/fileTypes/impress.svg"),
        },
        file_extensions=[
            "potm",
            "potx",
            "ppa",
            "ppam",
            "ppsx",
            "ppt",
            "pptm",
            "pptx",
        ]
    ),

    icon.FileIcon(
        {
            ColorTheme.DEFAULT_DARK: icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/image_dark.svg"),
            ColorTheme.LIGHT       : icon.FileIconDefinition("/jetbrains/AllIcons/expui/fileTypes/image.svg"),
        },
        file_extensions=[
            # Image types
            "afphoto",
            "ami",
            "apx",
            "ase",
            "aseprite",
            "bmp",
            "bpg",
            "brk",
            "clip",
            "cpt",
            "cur",
            "dds",
            "dng",
            "eps",
            "expr",
            "fpx",
            "gbr",
            "gif",
            "heic",
            "heif",
            "ico",
            "img",
            "jb2",
            "jbig2",
            "jgp",
            "jng",
            "jpeg",
            "jpg",
            "jxl",
            "jxr",
            "kra",
            "mdp",
            "ora",
            "pbm",
            "pdn",
            "pgf",
            "pic",
            "png",
            "psd",
            "psdb",
            "reb",
            "sai",
            "svg",
            "tga",
            "tif",
            "tiff",
            "webp",
            "xcf",

            # Video types
            "avi",
            "flv",
            "gifv",
            "m2v",
            "m4v",
            "mkv",
            "mov",
            "mp4",
            "mpe",
            "mpeg",
            "mpg",
            "mpv",
            "ogv",
            "qt",
            "rm",
            "rmvb",
            "vob",
            "webm",
            "wmv",
            "yuv",

            # Audio types # TODO: Custom icon
            "aiff",
            "ape",
            "flac",
            "m4a",
            "mp3",
            "ogg",
            "opus",
            "wav",
            "wma",
        ],
    ),

    # TODO: Make custom icon
    icon.FolderIcon(
        (
            "/customico/AllIcons/nodes/mediaFolder.svg",
            "/customico/AllIcons/nodes/mediaFolder-open.svg",
        ),
        [
            "image",
            "images",
            "img",
            "imgs",
            "icon",
            "icons",
            "ico",
            "icos",
            "screenshot",
            "screenshots",
            "video",
            "videos",
            "vid",
            "vids",
            "capture",
            "captures",
            "audio",
            "audios",
            "song",
            "songs",
            "wav",
            "wavs",
            "mp3",
            "mp3s",
        ]
    ),

]
