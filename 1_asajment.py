import xml.etree.ElementTree as ET




root = ET.Element("Movies")

m1 = ET.Element("Movie")
root.append(m1)

movieName = ET.SubElement(m1,"Ime")
movieName.text = "Maratonci trce pocasni krug"

movieGenre = ET.SubElement(m1,"Zanr")
movieGenre.text="Komedija"

movieYear = ET.SubElement(m1,"Godina premijere")
movieYear.text="1982."



m2 = ET.Element("Movie")
root.append(m2)

movieName = ET.SubElement(m2,"Ime")
movieName.text = "Ko to tamo peva"

movieGenre = ET.SubElement(m2,"Zanr")
movieGenre.text="Komedija"

movieYear = ET.SubElement(m2,"Godina premijere")
movieYear.text="1980."



m3 = ET.Element("Movie")
root.append(m3)

movieName = ET.SubElement(m3,"Ime")
movieName.text = "Boj na Kosovu"

movieGenre = ET.SubElement(m3,"Zanr")
movieGenre.text="Ratni, drama"

movieYear = ET.SubElement(m3,"Godina premijere")
movieYear.text="1989."

tree = ET.ElementTree(root)

print(ET.tostring(root))

with open("movies.xml","wb") as f:
    tree.write(f)


