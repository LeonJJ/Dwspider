# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import requests
class DwspiderPipeline(object):
    #图片下载
    def process_item(self, item, spider):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)"
                                 " Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"}
        pic_path = item["path"]
        pic = requests.get(item["pic_url"],headers=headers).content
        with open(pic_path,"wb") as f:
            f.write(pic)

        return item
