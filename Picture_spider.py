# 静态网页图片爬取
# 网站为二维存储图片 分层爬取
# requests获取网页信息、下载图片，BeautifulSoup获取信息，os构造存储路径
import requests,os
from bs4 import BeautifulSoup
'''
begin_url ="http://www.mzitu.com/all"
headers = {"Referer":"http://www.mzitu.com/115882/2",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4549.400 QQBrowser/9.7.12900.400"}
respons =requests.get(begin_url,headers=headers).text
soup = BeautifulSoup(respons,"html.parser")
data1 = soup.find('p',class_="url").find_all('a')

for i in data1:
    title = i.get_text()
    path = str(title).strip()
    os.makedirs(os.path.join("D:\Ps素材",path))
    os.chdir(r"D:/Ps素材/"+path)
    sectent_url = i["href"]
    respons2 = requests.get(sectent_url, headers=headers).text
    soup2 = BeautifulSoup(respons2, "html.parser")
    data2 = soup2.find('div',class_="pagenavi").find_all('span')[-2].get_text()
    for x in range(1,int(data2)+1):
        third_url = sectent_url+'/'+str(x)
        respons3 = requests.get(third_url, headers=headers).text
        soup3 = BeautifulSoup(respons3, "html.parser")
        data3 = soup3.find('div',class_="main-image").find('img')["src"]
        print(data3)
        page = data3[-9:-4]
        data4 = requests.get(data3,headers=headers).content
        f = open(page+".jpg","ab")
        f.write(data4)
        f.close()
'''

class Photos():
    def __init__(self):
        self.headers = {"Referer": "http://www.mzitu.com/115882/2",
                   "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4549.400 QQBrowser/9.7.12900.400"}

    def requst(self,url):
        resspons = requests.get(url,headers=self.headers)
        return resspons
    #获取第一层网址
    def all_url(self,first_url):
        data1 = self.requst(first_url).text
        soup1 = BeautifulSoup(data1,"html.parser")
        all_data = soup1.find('p',class_="url").find_all("a")
        for i in all_data:
            title = i.get_text()
            print("start save:"+title)
            title1 = str(title).replace("?","").replace(":","")
            self.save_file(title1)
            sectent_url = i["href"]
            self.sectent(sectent_url)


#获取第二层网址
    def sectent(self,url_2):
        data2 = self.requst(url_2).text
        soup2 = BeautifulSoup(data2,"html.parser").find('div',class_="pagenavi").find_all('span')[-2].get_text()
        for x in range(1,int(soup2)+1):
            url_3 = url_2+"/"+str(x)
            self.img_url(url_3)
#获取图片url
    def img_url(self,url_4):
        result_img_url = self.requst(url_4).text
        soup3 = BeautifulSoup(result_img_url,"html.parser").find('div',class_="main-image").find('img')["src"]
        self.save_img(soup3)
#保存图片
    def save_img(self,url_5):
        img_pic = self.requst(url_5).content
        page = url_5[-9:-4]
        f = open(page+".jpg","ab")
        f.write(img_pic)
        f.close()


#下载东西到本地
    def save_file(self,title):
        requst_title = title.strip()#方法用于移除字符串头尾指定的字符（默认为空格）
        file_path = os.path.exists(os.path.join("D:\Ps素材",requst_title))#exists() 检测某个路径是否真实存在  join() 将2个路径合并成一个
        if not file_path:
            print("make a file name:"+title)
            os.makedirs(os.path.join(r"D:/Ps素材",requst_title))
            os.chdir(os.path.join(r"D:/Ps素材",requst_title))#切换到目录
            return True
        else:
            print("have no this file!")
            return False

if __name__ == "__main__":
    input_data = input("your need url:")
    A = Photos()
    A.all_url(input_data)