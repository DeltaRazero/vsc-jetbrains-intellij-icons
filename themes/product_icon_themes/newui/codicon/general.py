from icon_theme_builder.product_icon_theme import *

icons = [

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
        "/customico/CLionEmbeddedIcons/icons/expui/customGdbRunConfiguration_stroke.svg",
        ["chip"]
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
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/toolwindow/web_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/toolwindow/web.svg"),
        },
        ["globe"]
    ),

    ProductIcon(
        "/customico/AllIcons/expui/nodes/library_stroke.svg",
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
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/customico/AllIcons/expui/status/unknownOutline_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/customico/AllIcons/expui/status/unknownOutline.svg"),
        },
        ["question"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/customico/AllIcons/expui/general/shield_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/customico/AllIcons/expui/general/shield.svg"),
        },
        ["shield"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AppcodeIcons/icons/expui/target_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AppcodeIcons/icons/expui/target.svg"),
        },
        ["target"]
    ),

    ProductIcon(
        "/customico/AllIcons/expui/general/listFilter_stroke.svg",
        ["list-filter"]
    ),

    ProductIcon(
        "/customico/AllIcons/expui/general/listFlat_stroke.svg",
        ["list-flat"]
    ),

    ProductIcon(
        "/customico/AllIcons/expui/general/listOrdered_stroke.svg",
        ["list-ordered"]
    ),

    ProductIcon(
        "/customico/AllIcons/expui/general/listSelection_stroke.svg",
        ["list-selection"]
    ),

    ProductIcon(
        "/customico/AllIcons/expui/general/listTree_stroke.svg",
        ["list-tree"]
    ),

    ProductIcon(
        "/customico/AllIcons/expui/general/listUnordered_stroke.svg",
        ["list-unordered"]
    ),

    # TODO: For some reason it's rendered off-center
    ProductIcon(
        "/customico/AllIcons/process/fs/step_stroke.svg",
        ["loading"]
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
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/locked_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/locked.svg"),
        },
        ["lock-small"]
    ).scaled(0.75),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/unlocked_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/unlocked.svg"),
        },
        ["unlock"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/FeaturesTrainerIcons/img/expui/checkmark_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/FeaturesTrainerIcons/img/expui/checkmark.svg"),
        },
        ["check"]
    ),

    ProductIcon(
        "/customico/FeaturesTrainerIcons/img/expui/checkmarkAll_stroke.svg",
        ["check-all"]
    ),

    ProductIcon(
        "/customico/ProfilerLineProfilerIcons/icons/expui/flame_stroke.svg",
        ["flame"]
    ),

    ProductIcon(
        "/customico/AllIcons/expui/run/debug_stroke_fixed.svg",
        ["bug"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/settings_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/settings.svg"),
        },
        ["gear", "settings", "settings-gear"]
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
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/toolwindow/toolWindowInternal_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/toolwindow/toolWindowInternal.svg"),
        },
        ["tools"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/toolwindow/hierarchy_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/toolwindow/hierarchy.svg"),
        },
        ["type-hierarchy", "type-hierarchy-sub"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/customico/AllIcons/expui/toolwindow/hierarchySuper_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/customico/AllIcons/expui/toolwindow/hierarchySuper.svg"),
        },
        ["type-hierarchy-super"]
    ),

    ProductIcon(
        "/customico/JavaUltimateIcons/icons/cdi/newui/event_stroke.svg",
        ["zap"]
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
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/run/showIgnored_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/run/showIgnored.svg"),
        },
        ["circle-slash"]
    ),

    ProductIcon(
        "/customico/AllIcons/expui/nodes/homeFolder_stroke.svg",
        ["home"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/general/history_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/general/history.svg"),
        },
        ["history"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/toolwindow/settingSync_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/toolwindow/settingSync.svg"),
        },
        ["sync"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/SettingsSyncIcons/icons/expui/statusDisabled_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/SettingsSyncIcons/icons/expui/statusDisabled.svg"),
        },
        ["sync-ignored"]
    ),

    # TODO: Make custom vertically centered icon
    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/toolwindow/documentation_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/toolwindow/documentation.svg"),
        },
        ["book"]
    ),

    ProductIcon(
        "/customico/AllIcons/expui/general/user_stroke.svg",
        ["account"]
    ),

]
