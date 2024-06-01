import re

import xml.etree.ElementTree as ElementTree

# *****************************************************************************

class SvgScaler:

    # :: PUBLIC FUNCTIONS :: #

    @staticmethod
    def scale(xml: ElementTree.ElementTree, scale: float):
        if (scale == 1.0):
            return

        ElementTree.register_namespace('', "http://www.w3.org/2000/svg")

        if (xml):
            xml_root = xml.getroot()

            width  = 0
            height = 0
            min_x  = 0
            min_y  = 0

            if ("width" in xml_root.attrib and "height" in xml_root.attrib):
                width = int( re.sub("[^0-9]*", '', xml_root.attrib["width"]))
                height = int( re.sub("[^0-9]*", '', xml_root.attrib["height"]))
            elif ("viewBox" in xml_root.attrib):
                view_box = [
                    int( re.sub("[^0-9]*", '', value) ) for value in xml_root.attrib["viewBox"].split(' ')
                ]

                if (len(view_box) != 4):
                    return

                min_x  = view_box[0]
                min_y  = view_box[1]
                width  = view_box[2]
                height = view_box[3]
            else:
                return

            scale = 1 / scale

            adjust_x = (width  - (width  * scale)) / 2
            adjust_y = (height - (height * scale)) / 2

            if (adjust_x - int(adjust_x)): adjust_x = int(adjust_x)
            if (adjust_y - int(adjust_y)): adjust_y = int(adjust_y)

            xml_root.attrib["viewBox"] = ' '.join([str(num) for num in [
                min_x + adjust_x,
                min_y + adjust_y,
                width  * scale,
                height * scale,
            ]])

        return


    @staticmethod
    def _get_tag(element: ElementTree.Element) -> str:
        return element.tag.rpartition('}')[-1]
