#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xml.dom.minidom

# https://www.cnblogs.com/chenjianhong/p/4144762.html
# 使用minidom解析器打开 XML 文档
DOMTree = xml.dom.minidom.parse("./movies.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
    print("Root element : %s" % collection.getAttribute("shelf"))

# 在集合中获取所有电影
movies = collection.getElementsByTagName("movie")

# 打印每部电影的详细信息
for movie in movies:
    if movie.hasAttribute("title"):
        print("Title: %s" % movie.getAttribute("title"))
        type = movie.getElementsByTagName('type')[0]
        print("Type: %s" % type.childNodes[0].data)
        print("Type", type.nodeName, type.nodeValue)
        format = movie.getElementsByTagName('format')[0]
        print("Format: %s" % format.childNodes[0].data)
        rating = movie.getElementsByTagName('rating')[0]
        print("Rating: %s" % rating.childNodes[0].data)
        description = movie.getElementsByTagName('description')[0]
        print("Description: %s" % description.childNodes[0].data)
        comments = movie.getElementsByTagName("comments")
        if comments:
            print("comments: %s" % comments[0].childNodes[0].data)