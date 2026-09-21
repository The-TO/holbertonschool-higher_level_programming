#!/usr/bin/env python3
"""Module  for convert XML file into json"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")
    for cle, valeur in dictionary.items():
        child = ET.SubElement(root, cle)
        child.text = str(valeur)
    ET.ElementTree(root).write(filename)


def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    result = {}
    for child in root:
        result[child.tag] = child.text
    return result
