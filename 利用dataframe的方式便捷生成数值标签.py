import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from numpy import nan as NA #允许numpy用NA代替nan作为别名
from pandas import DataFrame,Series
import seaborn as sns
from pyecharts import options as opts
from pyecharts.charts import Bar,Grid,Pie
from pyecharts.globals import CurrentConfig, NotebookType
CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_LAB #声明notebook类型

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei'] #显示中文标签
plt.rcParams['axes.unicode_minus'] = False #显示负号
from IPython.core.interactiveshell import InteractiveShell
#InteractiveShell.ast_node_interactivity = "all"
import warnings
warnings.filterwarnings('ignore')

df_sale_line = df_sale.groupby('日期')['销售数'].sum().reset_index()
x = df_sale_line['日期'].astype('str').tolist()
y = df_sale_line['销售数'].tolist()

plt.plot(x,y,color='red',linestyle='--',linewidth=1,marker="o",markersize=5)

plt.xlabel("日期",labelpad = 10) #设置X轴距离，labelpad控制标题到图表的距离
plt.ylabel("电商销售数",labelpad = 10) #设置Y轴距离，labelpad控制标题到图表的距离
plt.title('双十一销售量数据趋势', loc = "center")

plt.xticks(x, ['{}日'.format(i+1) for i in range(30)],rotation=45,fontsize=9,color='k')#设置X坐标轴刻度
plt.yticks(fontsize=9,color='k')#设置Y坐标轴刻度
plt.grid(visible = True,linestyle='dashed')#设置网格线为虚线,axis='y'可只对Y轴打开网格线
#添加数值标签
for a,b in zip(x, y):
    plt.text(a,b,b, ha = "center", va = "bottom", fontsize = 9)

plt.savefig('1.png')
plt.show()


#魔法命令，用于在笔记本内联显示matplotlib图表
%matplotlib inline 
#确保图表以SVG格式显示
%config InlineBackend.figure_format = 'svg' 
plt.rcParams["font.sans-serif"] = 'Microsoft YaHei' #解决中文乱码问题
plt.rcParams['axes.unicode_minus'] = False #解决负号无法显示
psl.use('ggplot')

df_sale_barh = df_sale.groupby('商品品类')['销售数'].sum().reset_index().sort_values(by = '销售数')

x = df_sale_barh['商品品类'].tolist()
y = df_sale_barh['销售数'].tolist()

#绘制柱状图
plt.barh(x, width = y, height = 0.5, align = "center", label = "销售数",color=get_colors(x))

#设置标题
plt.title("不同商品品类销售数", loc="center")
plt.xticks(fontsize=9,color='k')#设置X坐标轴刻度
plt.yticks(fontsize=9,color='k')#设置Y坐标轴刻度

#添加数据标签
for a,b in zip(x, y):
    plt.text(b,a,b,ha = "left", va = "center", fontsize = 10)

plt.xlabel("销售数",labelpad=10,fontsize=9,color='k')#设置X轴距离，labelpad控制标题到图表的距离
plt.ylabel("商品品类",labelpad=10,fontsize=9,color='k')#设置x和y轴的名称

plt.show()

'''
在用matplotlib生成图表时，可以利用pandas先分别指定X的序列和Y的序列，从而去生成柱状图、折线图以及其他图表
用这种方法生成数值标签的时候，仅需用for循环遍历zip(x,u),在利用plt.text方法进行标注即可。
'''