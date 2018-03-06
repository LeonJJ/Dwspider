# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import re,os
from Dwspider.items import DwspiderItem
from urllib import parse


class DwspiderSpider(scrapy.Spider):
    '''爬取多维图片网站图片'''
    name = 'dwspider'
    allowed_domains = ['mmonly.cc']
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)"
                                 " Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"}
    save_file_path = r"D:/qqwwee/"
    def start_requests(self):
        yield Request(url="http://www.mmonly.cc/ktmh/qbrw/list_33_8.html",headers=self.headers,callback=self.parse)

    def parse(self, response):
        #获取列表页图片url和title,并构建以title命名的文件夹存储图片
        url_titile = re.findall(r'.*?div class="ABox".*?href="(.*?)"><img.*?alt="(.*?)" src',response.text)
        for i in url_titile:
            item = DwspiderItem()
            item["file_path"]= self.save_file_path+i[1]
            if not os.path.exists(item["file_path"]):
                os.makedirs(item["file_path"])
            yield Request(url=i[0],headers=self.headers,callback=self.parse_one,meta={"item1":item})

        #获取列表页下一页
        next_pageurl = response.css('#pageNum a::attr(href)').extract()[-2]
        next_text = response.css('#pageNum a::text').extract()[-2]
        if next_text == "下一页":
            yield Request(url=parse.urljoin(response.url,next_pageurl),headers=self.headers,callback=self.parse)

    def parse_one(self,response):
        #构造图片的url，并设置图片名和存储地址
        item2 = response.meta["item1"]
        pagenum = response.css('.totalpage::text').extract_first("")
        for x in range(1,int(pagenum)+1):
            last_url = response.url[:-5]+"_"+str(x)+".html"
            item = DwspiderItem()
            item["path"] = item2["file_path"]+"/"+str(x)+".jpg"
            yield Request(url=last_url,headers=self.headers,callback=self.parse_two,meta={"item2":item})

    def parse_two(self,response):
        # 提取图片的下载地址
        item3 = response.meta["item2"]
        item = DwspiderItem()
        item["path"] = item3["path"]
        item["pic_url"]= response.css('.big-pic img::attr(src)').extract_first("")

        yield item

