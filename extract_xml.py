import csv
import sys

from lxml import etree


xpath_balise = sys.argv[1]
xml_file = sys.argv[2]
destination_file = sys.argv[3]

xml = etree.parse(xml_file)

balises = xml.xpath("./{xpath}".format(xpath=xpath_balise))

with open(destination_file, 'w', newline='') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_NONE)
	for element in balises:
		spamwriter.writerow([element.text])
