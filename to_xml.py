import csv
import xml.etree.ElementTree as ET

root = ET.Element("users")

with open("users.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        user = ET.SubElement(root, "user")
        for field in row:
            child = ET.SubElement(user, field)
            child.text = row[field]

tree = ET.ElementTree(root)
tree.write("users.xml", encoding="utf-8", xml_declaration=True)
