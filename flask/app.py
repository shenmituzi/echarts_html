from flask import Flask,render_template,request
import pymysql
from demo import Find
app=Flask(__name__)
@app.route('/book')
# 藏书阁
def db_book():
    datalist=[]
    db = pymysql.connect(host="localhost", user="root",
                         password="123456", db="demo", port=3306)
    cur = db.cursor()
    sql_insert='''
    select * from dbbook limit 13 ;
    '''
    try:
        cur.execute(sql_insert)
        #     # 提交
        db.commit()
        for i in cur.fetchall():
            datalist.append(i)
    except Exception as e:
        #     # 错误回滚
        db.rollback()
    finally:
        db.close()
    return  render_template('blog.html',movie=datalist)


@app.route('/book2')
# 藏书阁
def db_book2():
    datalist=[]
    db = pymysql.connect(host="localhost", user="root",
                         password="123456", db="demo", port=3306)
    cur = db.cursor()
    sql_insert='''
    select * from dbbook limit 13,14 ;
    '''
    try:
        cur.execute(sql_insert)
        #     # 提交
        db.commit()
        for i in cur.fetchall():
            datalist.append(i)
    except Exception as e:
        #     # 错误回滚
        db.rollback()
    finally:
        db.close()
    return  render_template('blog2.html',movie=datalist)


@app.route('/book3')
# 藏书阁
def db_book3():
    datalist=[]
    db = pymysql.connect(host="localhost", user="root",
                         password="123456", db="demo", port=3306)
    cur = db.cursor()
    sql_insert='''
    select * from dbbook limit 14,14 ;
    '''
    try:
        cur.execute(sql_insert)
        #     # 提交
        db.commit()
        for i in cur.fetchall():
            datalist.append(i)
    except Exception as e:
        #     # 错误回滚
        db.rollback()
    finally:
        db.close()
    return  render_template('blog3.html',movie=datalist)


@app.route('/book4')
# 藏书阁
def db_book4():
    datalist=[]
    db = pymysql.connect(host="localhost", user="root",
                         password="123456", db="demo", port=3306)
    cur = db.cursor()
    sql_insert='''
    select * from dbbook limit 15,14 ;
    '''
    try:
        cur.execute(sql_insert)
        #     # 提交
        db.commit()
        for i in cur.fetchall():
            datalist.append(i)
    except Exception as e:
        #     # 错误回滚
        db.rollback()
    finally:
        db.close()
    return  render_template('blog4.html',movie=datalist)

@app.route('/index')
# 展示首页
def index():
    return render_template("index1.html")
@app.route('/')
# 路径调用
def indexs():
    return index()
@app.route('/show')
def show():
    return render_template("indaex.html")
@app.route('/poem')
# 枕边诗书
def poem():
    return render_template("features.html")
@app.route('/better')
# 闲处好
def better():
    return render_template("portfolio.html")
@app.route('/book/ciyun')
# 展示词云
def ciyun():
    return render_template("ciyun.html")
@app.route('/book/keshihua')
# 展示词云
def keshihua():
    datalist=[]
    score=[]
    db = pymysql.connect(host="localhost", user="root",
                         password="123456", db="demo", port=3306)
    cur = db.cursor()
    sql_insert='''
    select score,count(score) from dbbook group by score;
    '''
    try:
        cur.execute(sql_insert)
        #     # 提交
        db.commit()
        for i in cur.fetchall():


            datalist.append(str(i[0]))
            score.append(i[1])
    except Exception as e:
        #     # 错误回滚
        db.rollback()
    finally:
        db.close()
    return render_template("keshihua.html",score=datalist,num=score)
# 实现枕上诗书搜索功能
@app.route('/find',methods=['POST','GET'])
def  find():
    li=[]
    if request.method=='POST':
        # form 是用户填好的表单
        data = request.form
        # 拿到的是一个字典
        data = str(data['tip'])
        # 取出用户在输入框 的小说名字
        # 调用 demo中的 类  并返回一个 列表传送到 html页面中
        try:
            f=Find(data)
            lists=f.find()

            for i in lists:
                li.append(i)
            return render_template('find.html',li=li,data=data)
        except:
                # 如果抱错就执行这一段 说明没有你想要的小说
                data = '你想要的内容暂时还没有更新 看看别的吧'
                return render_template('find.html', data=data)
    # 如果是get请求  就调用else
    else:
        data='你想要的内容暂时还没有更新 看看别的吧'
        return render_template('find.html',data=data)
    # li=[]
    # if request.method=='POST':
    #     data = request.form
    #     # 拿到的是一个字典
    #     data = str(data['tip'])
    #     # 拿到输入的内容
    #     url = search_book(data)
    #     # 包装好url
    #
    #     html = requests.get(url=url, headers=headers, verify=False)
    #     root = etree.HTML(html.content)
    #     text_name = root.xpath('//*[@id="search-main"]/div[1]/ul/li[2]/span[2]/a/@href')
    #     print(text_name)
    #     #
    #     req = requests.get(url=text_name, headers=headers, verify=False)
    #     html = etree.HTML(req.content)
    #     hrefs = html.xpath('//*[@id="list"]/div[3]/ul[2]')
    #     for i in hrefs:
    #         href = i.xpath('./li/a/@href')
    #         # 章节url
    #
    #         for i in href:
    #             href = 'https://www.qu-la.com' + i
    #             res = requests.get(url=href, headers=headers, verify=False)
    #             # 内容url
    #             nov = etree.HTML(res.content)
    #             novel = nov.xpath('// *[ @ id = "txt"]/text()')
    #             li.append(novel)
    #             # 添加内容
    #             break
    #     return render_template("find.html", li=li)

        # if data['tip']=='aa':
        # # data=request.data
        #     return render_template("find.html",data=data)
        # else:
        #     return render_template('features.html')


if __name__ == '__main__':
    app.run(debug=True)
