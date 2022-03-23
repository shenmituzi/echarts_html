#-*- coding = utf-8 -*-
#@Time : 2022/3/7 10:08
#@File : ciyun.py
#@Softwore: PyCharm
#@Author: d
import numpy as np
import jieba
from matplotlib import pyplot as plt
from PIL import Image
import pymysql
from wordcloud import WordCloud
db = pymysql.connect(host="localhost", user="root",
                     password="123456", db="demo", port=3306)
cur = db.cursor()
sql_insert = '''
   select type from dbbook ;
   '''
try:
    datalist=""
    cur.execute(sql_insert)
    #     # 提交
    db.commit()
    for i in cur.fetchall():
        datalist=str(i)+datalist

except Exception as e:
    #     # 错误回滚
    db.rollback()
finally:
    db.close()
cut=jieba.cut(datalist)
string=' '.join(datalist)
img=Image.open(r'./static/images/2019.PNG')
# img=Image.open(r'z3.PNG')

img_arr=np.array(img)
wc=WordCloud(
    background_color='white',
    mask=img_arr,
    font_path = 'simhei.ttf',
    # width:int(default=400)
)
wc.generate_from_text(string)
fig=plt.figure(1)
plt.imshow(wc)
plt.axis('off')
plt.show()
# 是否展示
plt.savefig(r'./static/images/wc.jpg',dpi=600)