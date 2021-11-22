import os
import sys

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import matplotlib
import numpy as np

from datetime import datetime,timedelta
import pandas as pd


# # 处理客户端rtt delay/std 与 QPS 关系
datas = []
with open("BC26_20211031-202111110_analyze_datas/datas.txt", 'r') as f:
    datasInFile = f.read().split('\n', -1)
    for i in datasInFile :
        splitByspace = i.split(' ', -1)
        datas.append(splitByspace)
print(datas)

def initarray (QPS_begin, QPS_end):
    array = []
    for i in range(QPS_begin, QPS_end + 1):
        array.append(0)
    return array
Client_RTT_total = initarray(10, 30)
Server_RTT_total = initarray(10, 30)
test_times = initarray(10, 30)
Client_RTT_average = initarray(10, 30)
Server_RTT_average = initarray(10, 30)
Client_RTT_std = []
Server_RTT_std = []

for i in datas:
    index = int(i[0]) - 10
    this_times = int(i[1])
    this_Client_RTT_average = int(i[2])
    this_Server_RTT_average = int(i[3])
    test_times[index] += this_times
    Client_RTT_total[index] += this_times * this_Client_RTT_average
    Server_RTT_total[index] += this_times * this_Server_RTT_average

for i in range(10, 31):
    index = i - 10
    Client_RTT_average[index] = Client_RTT_total[index] / test_times[index]
    Server_RTT_average[index] = Server_RTT_total[index] / test_times[index]

x_tick_label = []
for i in range(10, 31):
    x_tick_label.append(str(i))


data = [Client_RTT_average, Server_RTT_average]

def create_multi_bars(labels, datas, tick_step=1, group_gap=0.2, bar_gap=0):
    '''
    labels : x轴坐标标签序列
    datas ：数据集，二维列表，要求列表每个元素的长度必须与labels的长度一致
    tick_step ：默认x轴刻度步长为1，通过tick_step可调整x轴刻度步长。
    group_gap : 柱子组与组之间的间隙，最好为正值，否则组与组之间重叠
    bar_gap ：每组柱子之间的空隙，默认为0，每组柱子紧挨，正值每组柱子之间有间隙，负值每组柱子之间重叠
    '''
    # ticks为x轴刻度
    ticks = np.arange(len(labels)) * tick_step
    # group_num为数据的组数，即每组柱子的柱子个数
    group_num = len(datas)
    # group_width为每组柱子的总宽度，group_gap 为柱子组与组之间的间隙。
    group_width = tick_step - group_gap
    # bar_span为每组柱子之间在x轴上的距离，即柱子宽度和间隙的总和
    bar_span = group_width / group_num
    # bar_width为每个柱子的实际宽度
    bar_width = bar_span - bar_gap
    # baseline_x为每组柱子第一个柱子的基准x轴位置，随后的柱子依次递增bar_span即可
    baseline_x = ticks - (group_width - bar_span) / 2
    i = 0
    for index, y in enumerate(datas):

        if i == 0:
            plt.bar(baseline_x + index*bar_span, y, bar_width, color='b', label = "Client RTT", alpha=0.7)
        elif i == 1:
            plt.bar(baseline_x + index*bar_span, y, bar_width, color='g', label = "Server RTT",alpha=0.7)
        i += 1
        plt.ylabel('ms')
        plt.xlabel('QPS')
        plt.legend(loc = 'upper left')
        plt.title('LwM2M/TCP/NB-IoT RTT-QPS')
        # x轴刻度标签位置与x轴刻度一致
        plt.xticks(ticks, labels)
    plt.ylim(0, 4500)
    plt.show()

create_multi_bars(x_tick_label, data, bar_gap=0.1)
