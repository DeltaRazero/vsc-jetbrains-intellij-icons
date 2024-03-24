from icon_theme_builder.product_icon_theme import *

icons = helper.all_as_glyph([

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/toolwindow/bookmarks_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/toolwindow/bookmarks.svg"),
        },
        ["bookmark"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/CidrProjectModelIcons/icons/expui/framework_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/CidrProjectModelIcons/icons/expui/framework.svg"),
        },
        ["briefcase"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/toolwindow/debug_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/toolwindow/debug.svg"),
        },
        ["bug"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/inline/matchCase_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/inline/matchCase.svg"),
        },
        ["case-sensitive"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/FeaturesTrainerIcons/img/expui/checkmark_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/FeaturesTrainerIcons/img/expui/checkmark.svg"),
        },
        ["check"]
    ),

    ProductIcon(
        "/customico/CLionEmbeddedIcons/icons/expui/customGdbRunConfiguration_stroke.svg",
        ["chip"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/windows/close_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/windows/close.svg"),
        },
        ["chrome-close"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/windows/maximize_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/windows/maximize.svg"),
        },
        ["chrome-maximize"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/windows/minimize_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/windows/minimize.svg"),
        },
        ["chrome-minimize"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/windows/restore_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/windows/restore.svg"),
        },
        ["chrome-restore"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/run/showIgnored_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/run/showIgnored.svg"),
        },
        ["circle-slash"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/SettingsSyncIcons/icons/expui/remoteChanges_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/SettingsSyncIcons/icons/expui/remoteChanges.svg"),
        },
        ["cloud"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/TerminalIcons/icons/expui/toolwindow/terminal_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/TerminalIcons/icons/expui/toolwindow/terminal.svg"),
        },
        ["console"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/toolwindow/profiler_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/toolwindow/profiler.svg"),
        },
        ["dashboard"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/DatabaseIcons/icons/expui/dbms_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/DatabaseIcons/icons/expui/dbms.svg"),
        },
        ["database"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/vcs/revert_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/vcs/revert.svg"),
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
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/layout_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/layout.svg"),
        },
        ["editor-layout"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/moreHorizontal_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/moreHorizontal.svg"),
        },
        ["ellipsis"]
    ),

    # TODO: Is this right? Maybe use openNewTab
    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AquaWIIcons/icons/toolwindow/expui/openInNewWindow_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AquaWIIcons/icons/toolwindow/expui/openInNewWindow.svg"),
        },
        ["empty-window"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/status/errorOutline_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/status/errorOutline.svg"),
        },
        ["error"]
    ),

    # TODO: Make outline version
    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/DatabaseIcons/icons/expui/extension_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/DatabaseIcons/icons/expui/extension.svg"),
        },
        ["extensions"]
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
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/settings_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/settings.svg"),
        },
        ["gear", "settings-gear"] # TODO: Report that 'settings' is bugged (CSS rule overrides font-family)
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/toolwindow/web_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/toolwindow/web.svg"),
        },
        ["globe"]
    ),

    # TODO: Maybe use mergeCallees runToCursor smartStepInto
    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/actions/moveToButton_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/actions/moveToButton.svg"),
            # ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/locate_dark.svg"),
            # ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/locate.svg"),
        },
        ["go-to-file"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/history_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/history.svg"),
        },
        ["history"]
    ),

    ProductIcon(
        "/customico/AllIcons/expui/nodes/homeFolder_stroke.svg",
        ["home"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/status/infoOutline_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/status/infoOutline.svg"),
        },
        ["info"]
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

    # TODO: Or use greyKey (aka vertical key instead of horizontal)
    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/DatabaseIcons/icons/expui/collectionKey_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/DatabaseIcons/icons/expui/collectionKey.svg"),
        },
        ["key"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/layout_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/layout.svg"),
        },
        ["layout"]
    ),

    ProductIcon(
        "/customico/AllIcons/expui/nodes/library_outline.svg",
        ["library"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/codeWithMe/cwmInvite_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/codeWithMe/cwmInvite.svg"),
        },
        ["link"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AquaWIIcons/icons/toolwindow/expui/openInNewWindow_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AquaWIIcons/icons/toolwindow/expui/openInNewWindow.svg"),
        },
        ["link-external"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AppcodeIcons/icons/expui/location_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AppcodeIcons/icons/expui/location.svg"),
        },
        ["location"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/locked_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/locked.svg"),
        },
        ["lock"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/moreHorizontal_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/moreHorizontal.svg"),
        },
        ["more"] # TODO: Report issue, isn't being set
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/FeaturesTrainerIcons/img/expui/toolwindow/learn_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/FeaturesTrainerIcons/img/expui/toolwindow/learn.svg"),
        },
        ["mortar-board"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/editorPreview_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/editorPreview.svg"),
        },
        ["open-preview"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/customico/AllIcons/expui/status/successOutline_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/customico/AllIcons/expui/status/successOutline.svg"),
        },
        ["pass"]
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
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/customico/AllIcons/expui/general/pin-action_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/customico/AllIcons/expui/general/pin-action.svg"),
        },
        ["pin"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/pin_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/pin.svg"),
        },
        ["pinned"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/customico/AllIcons/expui/general/pin-modified_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/customico/AllIcons/expui/general/pin-modified.svg"),
        },
        ["pinned-dirty"] # TODO: Report to VSCode issues, not working
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/inline/preserveCase_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/inline/preserveCase.svg"),
        },
        ["preserve-case"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/inline/preserveCase_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/inline/preserveCase.svg"),
        },
        ["preserve-case"]
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
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/customico/AllIcons/expui/status/unknownOutline_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/customico/AllIcons/expui/status/unknownOutline.svg"),
        },
        ["question"]
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
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/inline/regex_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/inline/regex.svg"),
        },
        ["regex"]
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
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/TerminalIcons/icons/expui/toolwindow/terminal_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/TerminalIcons/icons/expui/toolwindow/terminal.svg"),
        },
        ["repl"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/toolwindow/run_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/toolwindow/run.svg"),
        },
        ["run"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/save_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/save.svg"),
        },
        ["save"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/search_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/search.svg"),
        },
        ["search"]
    ),

    # TODO: Make custom icon, VSCode currently reuses the search icon
    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/search_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/search.svg"),
        },
        ["search-save"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/actions/inSelection_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/actions/inSelection.svg"),
        },
        ["selection"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/toolwindow/coverage_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/toolwindow/coverage.svg"),
        },
        ["shield"]
    ),

    # TODO: Move to category file called "tab icons"
    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/vcs/vcs_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/vcs/vcs.svg"),
        },
        ["source-control"]
    ),





    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/inline/exactWords_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/inline/exactWords.svg"),
        },
        ["whole-word"]
    ),

])
