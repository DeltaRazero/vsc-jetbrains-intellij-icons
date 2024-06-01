from icon_theme_builder.product_icon_theme import *

icons = helper.all_as_glyph([

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/add_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/add.svg"),
        },
        ["add", "plus"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/close_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/close.svg"),
        },
        ["close", "remove-close", "x"]
    ),

    ProductIcon(
        "/customico/AllIcons/expui/general/closeAll_stroke.svg",
        ["close-all"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/collapseAll_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/collapseAll.svg"),
        },
        ["collapse-all"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/expandAll_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/expandAll.svg"),
        },
        ["expand-all"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/export_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/export.svg"),
        },
        ["export"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/customico/AllIcons/expui/general/filter_dark-filled.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/customico/AllIcons/expui/general/filter-filled.svg"),
        },
        ["filter-filled"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/filter_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/filter.svg"),
        },
        ["filter"]
    ),

    ProductIcon(
        {
            # ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/vcs/revert_dark.svg"),
            # ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/vcs/revert.svg"),
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/reset_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/reset.svg"),
        },
        ["discard"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/edit_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/edit.svg"),
        },
        ["edit"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/show_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/show.svg"),
        },
        ["inspect"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/previewVertically_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/previewVertically.svg"),
        },
        ["preview"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/editorPreview_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/editorPreview.svg"),
        },
        ["open-preview"]
    ),

    ProductIcon(
        "/customico/UmlIcons/icons/expui/addNote_stroke.svg",
        ["go-to-file"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/redo_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/redo.svg"),
        },
        ["redo"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/refresh_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/refresh.svg"),
        },
        ["refresh"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/remove_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/remove.svg"),
        },
        ["remove"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/save_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/save.svg"),
        },
        ["save"]
    ),

    ProductIcon(
        "/customico/AllIcons/expui/general/saveAll_stroke.svg",
        ["save-all"]
    ),

    ProductIcon(
        "/customico/AllIcons/expui/general/saveAs_stroke.svg",
        ["save-as"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/delete_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/delete.svg"),
        },
        ["trash", "trashcan"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/image/zoomIn_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/image/zoomIn.svg"),
        },
        ["zoom-in"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/image/zoomOut_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/image/zoomOut.svg"),
        },
        ["zoom-out"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/edit_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/edit.svg"),
        },
        ["pencil"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/customico/AllIcons/expui/toolwindow/wrench_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/customico/AllIcons/expui/toolwindow/wrench.svg"),
        },
        ["wrench", "wrench-subaction"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/FeaturesTrainerIcons/img/expui/checkmark_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/FeaturesTrainerIcons/img/expui/checkmark.svg"),
        },
        ["replace"]
    ),

    ProductIcon(
        "/customico/FeaturesTrainerIcons/img/expui/checkmarkAll_stroke.svg",
        ["replace-all"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/moreHorizontal_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/moreHorizontal.svg"),
        },
        ["kebab-horizontal"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/moreVertical_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/moreVertical.svg"),
        },
        ["kebab-vertical"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/moreHorizontal_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/moreHorizontal.svg"),
        },
        ["more", "toolbar-more", "ellipsis"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/gutter/fold_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/gutter/fold.svg"),
        },
        ["fold"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/gutter/fold_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/gutter/fold.svg"),
        },
        ["fold"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/gutter/unfold_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/gutter/unfold.svg"),
        },
        ["unfold"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/toolwindow/run_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/toolwindow/run.svg"),
        },
        ["run", "play"]
    ),

    ProductIcon(
        "/customico/AllIcons/expui/toolwindow/runCircle_stroke.svg",
        ["play-circle"]
    ),

    ProductIcon(
        "/customico/AllIcons/expui/run/runAll_stroke.svg",
        ["run-all"]
    ),

    ProductIcon(
        "/customico/AllIcons/expui/run/runUp_stroke.svg",
        ["run-up"]
    ),

    ProductIcon(
        "/customico/AllIcons/expui/run/runDown_stroke.svg",
        ["run-down"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/show_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/show.svg"),
        },
        ["eye"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/debugger/watch_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/debugger/watch.svg"),
        },
        ["eye-watch"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AquaWIIcons/icons/browser/expui/clearCash_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AquaWIIcons/icons/browser/expui/clearCash.svg"),
        },
        ["clear-all"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/run/showIgnored_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/run/showIgnored.svg"),
        },
        ["exclude"]
    ),

])
