from lxml import etree
import xml.etree.ElementTree as ElementTree

CONTENT = """
<process id="process1">
 <log name="name1" device="device1"><![CDATA[timestamp value]]></log>
 <log name="name2" device="device2"><![CDATA[timestamp value, timestamp value, timestamp]]></log>
</process>
"""


def parse_with_lxml():
    root = etree.fromstring(CONTENT)
    for log in root.xpath("//log"):
        print(log.text)


def parse_with_stdlib():
    root = ElementTree.fromstring(CONTENT)
    for log in root.iter('log'):
        print(log.text)


def parse_file():
    element_tree = etree.parse("./movies.xml", etree.XMLParser())
    result = etree.tostring(element_tree)
    # result=etree.tostringlist(html) #解析成列表
    ele_movies = element_tree.xpath("//movie")
    for i in ele_movies:
        attr = i.xpath("./@title")
        v_type = i.xpath("./type/text()")
        print(attr, v_type)


if __name__ == '__main__':
    # parse_with_lxml()
    # parse_with_stdlib()
    parse_file()
