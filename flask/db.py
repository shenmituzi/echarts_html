# import os
import requests
import re
from lxml import etree
# from bs4 import BeautifulSoup
# from urllib import parse
# import warnings
# import ssl
# # ssl._create_default_https_context = ssl.create_unverified_context
# warnings.filterwarnings("ignore")
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
# req=requests.get(url='https://www.jav111.com/jav/28.html',headers=headers)
# res=req.text
# r=re.findall(r'<img class="img" thissrc="(.*?)">',res)
# print(r)

import re
import csv
import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.36'
}
# 1.指定url
url = 'https://movie.douban.com/top250'
# 2.发起请求
response = requests.get(url=url,headers=headers)
# 3.获取响应
data = response.text
# print(data)
# 4.数据解析
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                 r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?<span'
                 r'class="rating_num" property="v:average">(?P<score>.*?)</span.*?'
                 r'<span>(?P<num>.*?)人评价</span>',re.S)

result = obj.finditer(data)
print(result)
# f = open('dianying.csv','w')
# csvwriter = csv.writer(f)
for i in result:
   print(i)
    # print(i.group('name'))
    # print(i.group("score"))
    # print(i.group("num"))
    # print(i.group("year").strip())
    # dic = i.groupdict()
    # dic['year']=dic['year'].strip()
    # csvwriter.writerow(dic.values())
# f.close()
print('好了')



# class novel():
#     def search_book(self):
#         url = 'https://so.biqusoso.com/s.php?ie=gbk&siteid=biqugex.com&s=9157106854577873494&q='
#
#         book_name = input('请输入你想要爬取的小说：')
#
#         # 对输入的字符进行编码转换为gbk编码,再对其进行url编码操作
#         book_name = parse.quote(book_name.encode('gbk'))
#
#         book_url = url + book_name
#         return book_url
#     def find_book(self,book_url):
#         # 调用查找search_book()函数 查找跳转至相应界面
#         url = book_url
#
#         # 请求页面
#         html = requests.get(url, headers)
#         root = etree.HTML(html.content.decode('utf-8'))
#
#         # 处理异常 未找到书籍时返回提示
#         if(root.xpath('//div[@class="search-list"]/ul/li/span/a/@href[1]') == []):
#             print('搜索的书不存在，请正确输入书名')
#         else:
#             print('找到了作者为', root.xpath('//div[@class="search-list"]/ul/li/span[@class="s4"]/text()')[0],
#                   ',书名为《', root.xpath('//div[@class="search-list"]/ul/li/span/a/text()')[0], '》,请问是否下载[Y][N]'
#                   , end='')
#
#
#
#     # 获取目录的URL 并调用download_book()函数下载内容
#     def book_content_list(self,url):
#         html = requests.get(url, headers,verify=False)
#         root = etree.HTML(html.content)
#
#         # 获取目录的URL 并传入download_book()函数
#         s_list = root.xpath('//div[@class="listmain"]/dl/dd/a/@href')
#
#
#
#     def download_book(self,url):
#         html = requests.get(url, headers)
#         root = etree.HTML(html.content)
#         text_name = root.xpath('//div[@class="content"]/h1/text()')[0]
#         texts = root.xpath('//div[@class="showtxt"]/text()')
#         for text in texts:
#             print(text)
#         print('《' + text_name + '》已下载完成', end='')
#         file_name = root.xpath('//div[@class="footer"]/p/a/text()')[0]
#
#
#     def main(self):
#         print("----笔趣阁小说爬虫----")
#         print("1-------------搜索小说")
#         print("2----------------退出")
#         flag = int(input("请输入数字选择相应功能："))
#         while 1:
#             if flag == 1:
#                 book_url = self.search_book()
#                 self.find_book(book_url)
#             elif flag == 2:
#                 exit(1)
#             else:
#                 input("请输入正确的命令:")
#             flag = int(input("请重新输入数字选择相应功能："))
#
#         # main()
#         url=search_book()
#         # 拿到拼接好的 想要的书url
#         html=requests.get(url=url,headers=headers,verify=False)
#         root = etree.HTML(html.content)
#         text_name = root.xpath('//*[@id="search-main"]/div[1]/ul/li[2]/span[2]/a/@href')[0]
#         print(text_name)
#         # 拿到想看的书url  需要再一次发送请求  得到章节
#
#         req =requests.get(url=text_name,headers=headers,verify=False)
#         html = etree.HTML(req.content)
#         hrefs = html.xpath('//*[@id="list"]/div[3]/ul[2]')
#         for i in hrefs:
#             href=i.xpath('./li/a/@href')
#
#             # 拿到想看的的书所有章节url  最后对章节的url发起请求拿到内容
#
#             for i in href:
#                 href='https://www.qu-la.com'+i
#                 res= requests.get(url=href, headers=headers, verify=False)
#                 nov=etree.HTML(res.content)
#                 novel=nov.xpath('// *[ @ id = "txt"]/text()')
#                 print(novel)
# novel=novel()
# novel.main()
from demo import Find
# name=input("你想要爬取得小说")
# f=Find('校花')
# lis=[]
# li=f.find()
# for i in li:
#     # print(i)
#     lis.append(i)
# print(lis)
# import pymysql
#
# datalist = []
#
#
# def keshihua():
#     db = pymysql.connect(host="localhost", user="root",
#                          password="123456", db="demo", port=3306)
#     cur = db.cursor()
#     sql_insert='''
#     select score,count(score) from dbbook group by score;
#     '''
#     try:
#         cur.execute(sql_insert)
#         #     # 提交
#         db.commit()
#         for i in cur.fetchall():
#
#             a='"'+str(i[1])+'"'
#             print(a)
#             print(i[0])
#
#     except Exception as e:
#         #     # 错误回滚
#         db.rollback()
#     finally:
#         db.close()
# keshihua()
# print(datalist)