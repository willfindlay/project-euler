#! /usr/bin/env python3

import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    score = 0
    for child in node:
        score += get_attr_number(child)
    score += len(node.attrib)
    return score

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
