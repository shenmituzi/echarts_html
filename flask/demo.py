#-*- coding = utf-8 -*-
#@Time : 2022/3/8 22:13
#@File : demo.py
#@Softwore: PyCharm
#@Author: d
import os
import requests
from lxml import etree
from urllib import parse
import warnings
warnings.filterwarnings("ignore")
# 防止  verift 的改成 false  之后抱错

class Find():
    def __init__(self,name):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
        self.name=name
        # 在调用类的时候传入一个 小说的名字
    def search_book(self,book):
        url = 'https://so.biqusoso.com/s.php?ie=gbk&siteid=biqugex.com&s=9157106854577873494&q='


        # 对输入的字符进行编码转换为gbk编码,再对其进行url编码操作
        book_name = parse.quote(book.encode('gbk'))
        # 编码操作的意义是 把输入的小说名字转义 然后进行得到一个新的连接
        book_url = url + book_name
        return book_url
    def  find(self):
        li=[]
        num=2
        # 控制爬取得张数
        url = self.search_book(self.name)
        # 得到新的链接   在站点的搜索页面 拿到 想看小说的链接
        html = requests.get(url=url, headers=self.headers, verify=False)
        root = etree.HTML(html.content)
        text_name = root.xpath('//*[@id="search-main"]/div[1]/ul/li[2]/span[2]/a/@href')[0]
        print(text_name)
        # 拿到小说链接

        req = requests.get(url=text_name, headers=self.headers, verify=False)
        html = etree.HTML(req.content)
        hrefs = html.xpath('//*[@id="list"]/div[3]/ul[2]')
        for i in hrefs:
            href = i.xpath('./li/a/@href')
            # 拿到所有章节的url 下面进行拼接
            for i in href:
                num -= 1

                href = 'https://www.qu-la.com' + i
                # 拼接完成拿到 最后一次请求拿到小说内容
                res = requests.get(url=href, headers=self.headers, verify=False)
                nov = etree.HTML(res.content)
                novel = nov.xpath('// *[ @ id = "txt"]/text()')
                # li.append(novel)
                li=''.join(novel)
                li.replace('/r','\n')
                yield li
                # 只拿到第一张的内容 如果想拿到全部 把break注释
                # break
                if num==0:
                    break
