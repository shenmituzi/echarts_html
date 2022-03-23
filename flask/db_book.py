import requests
from lxml import etree
from fake_useragent import UserAgent
import time
import pymysql
import random

class DoubanBookSpider:
    def __init__(self):
        self.url = 'https://book.douban.com/top250?start={}'
        self.item={}
        self.datalist=[]

    def get_html(self, url):
        """使用随机的User-Agent"""
        headers = {'User-Agent':UserAgent().random}
        # headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'}
        html = requests.get(url=url, headers=headers).text
        self.parse_html(html)

    def parse_html(self, html,):
        """lxml+xpath进行数据解析"""
        parse_obj = etree.HTML(html)
        i=1
        # 1.基准xpath：提取每本书的节点对象列表
        table_list = parse_obj.xpath('//div[@class="indent"]/table')
        for table in table_list:
            # item = {}
            # 书名
            name_list = table.xpath('.//div[@class="pl2"]/a/@title')
            self.item['name'] = name_list[0].strip() if name_list else None
            # 描述
            content_list = table.xpath('.//p[@class="pl"]/text()')
            self.item['content'] = content_list[0].strip() if content_list else None
            # 评分
            score_list = table.xpath('.//span[@class="rating_nums"]/text()')
            self.item['score'] = score_list[0].strip() if score_list else None
            # 评价人数
            nums_list = table.xpath('.//span[@class="pl"]/text()')
            self.item['nums'] = nums_list[0][1:-1].strip() if nums_list else None
            # 类别
            type_list = table.xpath('.//span[@class="inq"]/text()')
            self.item['type'] = type_list[0].strip() if type_list else ' '
            href_list=table.xpath('.//div[@class="pl2"]/a/@href')
            self.item['href']=href_list[0].strip() if href_list else None

            self.item['name']='"'+self.item['name']+'"'

            self.item['type']='"'+self.item['type']+'"'
            self.item['content']='"'+self.item['content']+'"'
            self.item['nums']='"'+self.item['nums']+'"'
            self.item['href']='"'+self.item['href']+'"'


            db = pymysql.connect(host="localhost", user="root",
                             password="123456", db="demo", port=3306)
            datas=[str(self.item['name']),self.item['content'],str(self.item['score']),str(self.item['nums']),self.item['type'],str(self.item['href'])]

            cur = db.cursor()

            sql_insert = '''insert into dbbook values(%s);'''%",".join(datas)
            i+=1
            print(sql_insert)
            print("正在写入%s条"%(i))
            try:
                cur.execute(sql_insert)
        #     # 提交
                db.commit()
            except Exception as e:
        #     # 错误回滚
                db.rollback()
            finally:
                db.close()
    def  create_db(self):
        db = pymysql.connect(host="localhost", user="root",
                             password="123456", db="demo", port=3306)
        sql=''' create table dbbook(
        name text,
        content  text,
        score  int(10),
        nums   text,
        type   text,
        href   text);
        '''
        cur=db.cursor()
        try:
            cur.execute(sql)
            db.commit()
        except Exception as e:
            db.rollback()
        finally:
            db.close()
    def run(self):
        for i in range(0,9):
            start = (i - 1) * 25
            page_url = self.url.format(start)
            self.get_html(page_url)
            time.sleep(random.randint(1,2))
if __name__ == '__main__':
    spider = DoubanBookSpider()
    db=input("是否需要先创建数据库")
    if  db=="是":
        spider.create_db()
        spider.run()
    else:
        spider.run()