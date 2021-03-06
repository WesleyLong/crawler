from pyecharts import Bar
import pandas as pd
import numpy as np
import pymysql

conn = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='maoyan', charset='utf8mb4')
cursor = conn.cursor()
sql = "select * from films"
db = pd.read_sql(sql, conn)
df = db.sort_values(by="box_office", ascending=False)
dom = df[['name', 'box_office']]

attr = np.array(dom['name'][0:10])
v1 = np.array(dom['box_office'][0:10])
attr = ["{}".format(i.replace('：无限战争', '')) for i in attr]
v1 = ["{}".format(float('%.2f' % (float(i) / 100000000))) for i in v1]

bar = Bar("2018年电影票房TOP10(亿元)", title_pos='center', title_top='18', width=800, height=400)
bar.add("", attr, v1, is_convert=True, xaxis_min=10, yaxis_label_textsize=12, is_yaxis_boundarygap=True, yaxis_interval=0, is_label_show=True, is_legend_show=False, label_pos='right', is_yaxis_inverse=True, is_splitline_show=False)
bar.render("2018年电影票房TOP10.html")

