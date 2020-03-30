from lxml import etree
import re

parse = etree.parse("./sql.xml", etree.XMLParser())

ele_config_list = parse.xpath("//config")

biz_email_to = ""
biz_email_cc = ""
tech_email_to = ""
tech_email_cc = ""
for ele_config in ele_config_list:
    config_name = ele_config.xpath("./@name")

    biz_email = ele_config("./biz_email")
    if biz_email:
        biz_email_to = biz_email[0].evaluate("./to/text()")
        biz_email_cc = biz_email[0].xpath("./cc/text()")

    tech_email = ele_config.xpath("./tech_email")
    if tech_email:
        tech_email_to = tech_email[0].xpath("./to/text()")
        tech_email_cc = tech_email[0].xpath("./cc/text()")

    sql = ele_config.xpath("./sql/text()")
    if sql:
        sql = re.sub("[ ]+", " ", sql[0])
    comment = ele_config.xpath("./comment/text()")

    print(config_name, biz_email_to, biz_email_cc, tech_email_to, tech_email_cc, sql, comment, sep="\n")
