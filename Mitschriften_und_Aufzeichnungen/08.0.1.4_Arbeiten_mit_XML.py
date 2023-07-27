# Arbeiten mit XML
import xml.etree.ElementTree as ET

# Öffen der Datei zum lesen der XML

f = open('08.0.1.4.1_wunstorf.xml', 'rt', encoding='utf-8')

XML_External = f.read()
XML_Root = ET.fromstring(XML_External)  # Wandelt die Zeichenkette in ein Mini-DOM (Dokument-Object-Model) um.
                                        # Es wird ein XML-Objekt erzeugt

for child in XML_Root.iter('wind'): # Iterieren durch das Root-Element. Filtern nach dem Element Wind
    if child.attrib['interval'] == '3' and child.attrib['runway'] == 'typical':    # Die Attribute "interval" und "runway" nach bestimmten Werten selektieren

        for subchild in child.iter('speed'):    # wir wollen nur das Element "speed" haben
            print(subchild.attrib['value'])
