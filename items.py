# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DwspiderItem(scrapy.Item):
    # define the fields for your item here like:
    pic_url = scrapy.Field()#图片的下载地址
    file_path =scrapy.Field()#图片存储文件夹地址
    path = scrapy.Field()#图片存储地址
