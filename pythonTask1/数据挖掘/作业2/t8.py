from pyecharts.charts import *
from pyecharts.components import Table
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
import random
import datetime

from pyecharts.globals import CurrentConfig

bar = Bar()

x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data = [123, 153, 89, 107, 98, 23]

bar.add_xaxis(x_data)
bar.add_yaxis("销量", y_data)

bar.render("./picture.html")
