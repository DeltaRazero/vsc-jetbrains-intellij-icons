from icon_theme_builder.product_icon_theme import *

icons = helper.all_as_colr_glyph([

    ProductIcon(
        "/jetbrains/DatabaseIcons/icons/list.svg",
        ["symbol-array"]
    ),

    # TODO: Make custom
    ProductIcon(
        "/jetbrains/NetIcons128/Placeholder(Color).svg",
        ["symbol-boolean"]
    ),

    ProductIcon(
        "/jetbrains/AllIcons/nodes/class.svg",
        ["symbol-class"]
    ),

    ProductIcon(
        {
            ColorTheme.DEFAULT_DARK: ProductIconDefinition("/jetbrains/AllIcons/gutter/colors_dark.svg"),
            ColorTheme.LIGHT       : ProductIconDefinition("/jetbrains/AllIcons/gutter/colors.svg"),
        },
        ["symbol-color"]
    ),

    ProductIcon(
        "/jetbrains/AllIcons/nodes/constant.svg",
        ["symbol-constant"]
    ),

    ProductIcon(
        "/jetbrains/AllIcons/nodes/classInitializer.svg",
        ["symbol-constructor"]
    ),

    ProductIcon(
        "/jetbrains/AllIcons/nodes/enum.svg",
        ["symbol-enum"]
    ),

    ProductIcon(
        "/jetbrains/AllIcons/nodes/constant.svg",
        ["symbol-enum-member"]
    ),

    ProductIcon(
        "/jetbrains/JavaUltimateIcons/icons/cdi/newui/event.svg",
        ["symbol-event"]
    ),

    ProductIcon(
        "/jetbrains/AllIcons/nodes/field.svg",
        ["symbol-field"]
    ),

    ProductIcon(
        "/jetbrains/AllIcons/fileTypes/any_type.svg",
        ["symbol-file"]
    ),

    ProductIcon(
        "/jetbrains/AllIcons/nodes/folder.svg",
        ["symbol-folder"]
    ),

    ProductIcon(
        "/jetbrains/AllIcons/nodes/function.svg",
        ["symbol-function"]
    ),

    ProductIcon(
        "/jetbrains/AllIcons/nodes/interface.svg",
        ["symbol-interface"]
    ),

    ProductIcon(
        "/jetbrains/DatabaseIcons/icons/collectionKey.svg",
        ["symbol-key"]
    ),

    # TODO: Don't know which icon yet
    ProductIcon(
        # "/jetbrains/NetIcons128/Placeholder(Color).svg",
        "/jetbrains/DatabaseIcons/icons/string.svg",
        ["symbol-keyword"]
    ),

    ProductIcon(
        "/customico/AllIcons/nodes/method_centeredfix.svg",
        ["symbol-method"]
    ),

    ProductIcon(
        "/jetbrains/AllIcons/fileTypes/unknown.svg",
        ["symbol-misc"]
    ),

    ProductIcon(
        "/jetbrains/DatabaseIcons/icons/package.svg",
        ["symbol-module, symbol-namespace", "symbol-package"]
    ),

    ProductIcon(
        "/jetbrains/RubyIcons/icons/ruby/nodes/notDefined.svg",
        ["symbol-null"]
    ),

    # TODO: Make custom
    ProductIcon(
        "/jetbrains/NetIcons128/Placeholder(Color).svg",
        ["symbol-number", "symbol-numeric"]
    ),

    ProductIcon(
        "/jetbrains/DatabaseIcons/icons/set.svg",
        ["symbol-object"]
    ),

    ProductIcon(
        "/jetbrains/DatabaseIcons/icons/operator.svg",
        ["symbol-operator"]
    ),

    ProductIcon(
        "/jetbrains/AllIcons/nodes/parameter.svg",
        ["symbol-parameter"]
    ),

    ProductIcon(
        "/jetbrains/AllIcons/nodes/property.svg",
        ["symbol-property"]
    ),

    # TODO: Don't know which icon yet
    ProductIcon(
        "/jetbrains/NetIcons128/Placeholder(Color).svg",
        ["symbol-reference"]
    ),

    # TODO: Don't know which icon yet
    ProductIcon(
        "/jetbrains/NetIcons128/Placeholder(Color).svg",
        ["symbol-ruler"]
    ),

    ProductIcon(
        "/jetbrains/AllIcons/nodes/template.svg",
        ["symbol-snippet"]
    ),

    ProductIcon(
        "/jetbrains/DatabaseIcons/icons/string.svg",
        ["symbol-string"]
    ),

    # TODO: Make custom, use same color as `codeAssistantStruct`
    ProductIcon(
        "/jetbrains/NetIcons128/Placeholder(Color).svg",
        ["symbol-struct", "symbol-structure"]
    ),

    ProductIcon(
        "/jetbrains/AllIcons/fileTypes/text.svg",
        ["symbol-text"]
    ),

    ProductIcon(
        "/jetbrains/AllIcons/nodes/type.svg",
        ["symbol-type-parameter"]
    ),

    # TODO: Don't know which icon yet
    ProductIcon(
        "/jetbrains/NetIcons128/Placeholder(Color).svg",
        ["symbol-unit"]
    ),

    # TODO: Make custom, use same letter and color as Kotlin `value`
    ProductIcon(
        "/jetbrains/NetIcons128/Placeholder(Color).svg",
        ["symbol-value"]
    ),

    ProductIcon(
        "/jetbrains/AllIcons/nodes/variable.svg",
        ["symbol-variable"]
    ),

])
