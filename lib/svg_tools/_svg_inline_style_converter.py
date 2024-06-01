import argparse
import traceback
import xml.etree.ElementTree as ElementTree

import css_parser
css_parser.log.enabled = False

# *****************************************************************************

class SvgInlineStyleConverter:

    # :: PRIVATE ATTRIBUTES :: #

    _style_classes : dict[str, dict[str, str]]


    # :: PUBLIC FUNCTIONS :: #

    @staticmethod
    def convert(xml: ElementTree.ElementTree):

        xml_root = xml.getroot()

        converter = SvgInlineStyleConverter()

        converter._parse_style(xml_root)

        for element in xml_root:
            converter._convert_element(element)

        SvgInlineStyleConverter._remove_style(xml_root)

        return


    # :: PRIVATE METHODS :: #

    def _parse_style(self, xml_root: ElementTree.Element) -> None:

        self._style_classes = {}

        style_tag: ElementTree.Element | None = None

        # First find style tag
        for element in xml_root:
            if (SvgInlineStyleConverter._get_tag(element) == "style"):
                style_tag = element
                break

        if (style_tag is None):
            return

        style_classes = css_parser.parseString(element.text)
        for style_class in style_classes.cssRules:

            a = {}
            for style_property in style_class.style.getProperties():
                a[style_property.name] = style_property.value

            for selector_class in style_class.selectorList:
                class_name = selector_class.selectorText.lstrip('.')

                b = self._style_classes.get(class_name, {}) | a
                self._style_classes[class_name] = b

        return


    def _convert_element(self, element: ElementTree.Element):

        element_classes = element.attrib.get("class", "").split()
        for element_class in element_classes:

            style_class = self._style_classes[element_class]
            for style_attribute, style_value in style_class.items():
                # print([style_attribute, style_value])
                element.attrib[style_attribute] = style_value

        # Remove the classes to clean the SVG
        if (element_classes):
            element.attrib.pop("class")

        for sub_element in element:
            self._convert_element(sub_element)

        return


    # :: PRIVATE FUNCTIONS :: #

    @staticmethod
    def _remove_style(xml_root: ElementTree.Element) -> None:

        for element in xml_root:
            if (SvgInlineStyleConverter._get_tag(element) == "style"):
                xml_root.remove(element)
                break

        return


    @staticmethod
    def _get_tag(element: ElementTree.Element) -> str:
        return element.tag.rpartition('}')[-1]
