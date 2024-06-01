import re

import xml.etree.ElementTree as ElementTree

# *****************************************************************************

class SvgFrameAdder:

    @staticmethod
    def add_frame(xml: ElementTree.ElementTree) -> None:

        xml_root = xml.getroot()

        for element in xml_root:
            if element.attrib.get("id", "").lower() == "frame":
                return

        width  = 0
        height = 0

        if ("width" in xml_root.attrib and "height" in xml_root.attrib):
            width = int( re.sub("[^0-9]*", '', xml_root.attrib["width"]))
            height = int( re.sub("[^0-9]*", '', xml_root.attrib["height"]))
        elif ("viewBox" in xml_root.attrib):
            view_box = [
                int( re.sub("[^0-9]*", '', value) ) for value in xml_root.attrib["viewBox"].split(' ')
            ]

            if (len(view_box) != 4):
                return

            # FIXME: Make adjuster/calculator
            if (view_box[0] != 0 or view_box[1] != 0):
                return

            width  = view_box[2]
            height = view_box[3]
        else:
            return

        frame = ElementTree.Element("rect")
        frame.attrib = {
            "id"     : "frame",
            "fill"   : "none",
            "width"  : str(width),
            "height" : str(height),
        }
        xml_root.insert(0, frame)

        return


    @staticmethod
    def _get_tag(element: ElementTree.Element) -> str:
        return element.tag.rpartition('}')[-1]
