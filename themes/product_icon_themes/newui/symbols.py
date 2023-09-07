from icon_theme_builder.product_icon_theme import *

icons = helper.all_as_colr_glyph([

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/DatabaseIcons/icons/expui/list_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/DatabaseIcons/icons/expui/list.svg"),
        },
        ["symbol-array"]
    ),

    # TODO: Make custom
    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/NetIcons128/Placeholder(Color).svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/NetIcons128/Placeholder(Color).svg"),
        },
        ["symbol-boolean"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/nodes/class_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/nodes/class.svg"),
        },
        ["symbol-class"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/gutter/colors_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/gutter/colors.svg"),
        },
        ["symbol-color"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/nodes/constant_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/nodes/constant.svg"),
        },
        ["symbol-constant"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/nodes/classInitializer_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/nodes/classInitializer.svg"),
        },
        ["symbol-constructor"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/nodes/enum_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/nodes/enum.svg"),
        },
        ["symbol-enum"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/nodes/constant_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/nodes/constant.svg"),
        },
        ["symbol-enum-member"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/JavaUltimateIcons/icons/cdi/newui/event_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/JavaUltimateIcons/icons/cdi/newui/event.svg"),
        },
        ["symbol-event"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/nodes/field_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/nodes/field.svg"),
        },
        ["symbol-field"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/fileTypes/anyType_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/fileTypes/anyType.svg"),
        },
        ["symbol-file"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/nodes/folder_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/nodes/folder.svg"),
        },
        ["symbol-folder"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/nodes/function_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/nodes/function.svg"),
        },
        ["symbol-function"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/nodes/interface_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/nodes/interface.svg"),
        },
        ["symbol-interface"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/DatabaseIcons/icons/expui/collectionKey_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/DatabaseIcons/icons/expui/collectionKey.svg"),
        },
        ["symbol-key"]
    ),

    # TODO: Don't know which icon yet
    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/DatabaseIcons/icons/expui/string_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/DatabaseIcons/icons/expui/string.svg"),
        },
        ["symbol-keyword"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/nodes/method_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/nodes/method.svg"),
        },
        ["symbol-method"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/fileTypes/unknown_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/fileTypes/unknown.svg"),
        },
        ["symbol-misc"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/DatabaseIcons/icons/expui/package_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/DatabaseIcons/icons/expui/package.svg"),
        },
        ["symbol-module, symbol-namespace", "symbol-package"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/RubyIcons/icons/expui/ruby/nodes/notDefined_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/RubyIcons/icons/expui/ruby/nodes/notDefined.svg"),
        },
        ["symbol-null"]
    ),

    # TODO: Make custom
    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/NetIcons128/Placeholder(Color).svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/NetIcons128/Placeholder(Color).svg"),
        },
        ["symbol-number", "symbol-numeric"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/DatabaseIcons/icons/expui/set_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/DatabaseIcons/icons/expui/set.svg"),
        },
        ["symbol-object"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/DatabaseIcons/icons/expui/operator_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/DatabaseIcons/icons/expui/operator.svg"),
        },
        ["symbol-operator"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/nodes/parameter_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/nodes/parameter.svg"),
        },
        ["symbol-parameter"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/nodes/property_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/nodes/property.svg"),
        },
        ["symbol-property"]
    ),

    # TODO: Don't know which icon yet
    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/NetIcons128/Placeholder(Color).svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/NetIcons128/Placeholder(Color).svg"),
        },
        ["symbol-reference"]
    ),

    # TODO: Don't know which icon yet
    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/NetIcons128/Placeholder(Color).svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/NetIcons128/Placeholder(Color).svg"),
        },
        ["symbol-ruler"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/nodes/template_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/nodes/template.svg"),
        },
        ["symbol-snippet"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/DatabaseIcons/icons/expui/string_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/DatabaseIcons/icons/expui/string.svg"),
        },
        ["symbol-string"]
    ),

    # TODO: Make custom, use same color as `codeAssistantStruct`
    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/NetIcons128/Placeholder(Color).svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/NetIcons128/Placeholder(Color).svg"),
        },
        ["symbol-struct", "symbol-structure"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/fileTypes/text_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/fileTypes/text.svg"),
        },
        ["symbol-text"]
    ),

    # TODO: Make custom, use same letter and color as `codeAssistantType`
    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/NetIcons128/Placeholder(Color).svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/NetIcons128/Placeholder(Color).svg"),
        },
        ["symbol-type-parameter"]
    ),

    # TODO: Don't know which icon yet
    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/NetIcons128/Placeholder(Color).svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/NetIcons128/Placeholder(Color).svg"),
        },
        ["symbol-unit"]
    ),

    # TODO: Make custom, use same letter and color as Kotlin `value`
    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/NetIcons128/Placeholder(Color).svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/NetIcons128/Placeholder(Color).svg"),
        },
        ["symbol-value"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/expui/nodes/variable_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/expui/nodes/variable.svg"),
        },
        ["symbol-variable"]
    ),

])
