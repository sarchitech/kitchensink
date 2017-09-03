#!/usr/bin/env python

import os
import sys
from xml.etree import ElementTree

repo_path = os.getenv('NEVERCODE_BUILD_DIR')
build_number = os.getenv('NEVERCODE_BUILD_NUMBER')

if not build_number:
    print "Missing build number, skip updating"
    sys.exit()

config_xml_path = os.path.join(repo_path, 'config.xml')

ElementTree.register_namespace('', 'http://www.w3.org/ns/widgets')
tree = ElementTree.parse(config_xml_path)
root = tree.getroot()

root.attrib['android-versionCode'] = build_number
root.attrib['ios-CFBundleVersion'] = build_number

tree.write(config_xml_path)

print "Updated versionCode and CFBundleVersion to %s" % build_number
