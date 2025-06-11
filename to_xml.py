import csv
import xml.etree.ElementTree as ET
import re

# Validation functions
def is_valid_email(email):
    return "@" in email and len(email) <= 30

def is_valid_password(password):
    return len(password) >= 8 and re.match(r'^[A-Za-z0-9]+$', password)

def is_valid_idnumber(idnum):
    try:
        return int(float(idnum)) > 0
    except:
        return False

# XML root
root = ET.Element("users")

# Read and validate CSV
with open("users.csv", newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if not all(row.values()):
            continue  # Skip rows with any empty field
        if not (is_valid_email(row["email"]) and is_valid_password(row["password"]) and is_valid_idnumber(row["idnumber"])):
            continue  # Skip invalid rows

        user = ET.SubElement(root, "user")
        for field, value in row.items():
            child = ET.SubElement(user, field)
            if field == "idnumber":
                value = str(int(float(value)))  # Remove decimal
            child.text = value.strip()

# Write XML
tree = ET.ElementTree(root)
tree.write("users.xml", encoding="utf-8", xml_declaration=True)

