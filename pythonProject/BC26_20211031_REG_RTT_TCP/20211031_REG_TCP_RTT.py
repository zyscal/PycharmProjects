import os
import sys

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import matplotlib
import numpy as np
from datetime import datetime
import pandas as pd


def read_datetimes(datetime_file):
    datetime_list = []
    with open(datetime_file, 'r') as f:
        all_datetime = f.read().split('\n', -1)
    for i in all_datetime:
        if i == '':
            break;
        single_datetime = i.split(',', -1)
        tem_datetime = datetime(year=int(single_datetime[0]), month=int(single_datetime[1]),
                                day=int(single_datetime[2]),
                                hour=int(single_datetime[3]), minute=int(single_datetime[4]),
                                second=int(single_datetime[5])
                                , microsecond=int(single_datetime[6]))
        datetime_list.append(tem_datetime)
    return datetime_list

def read_delay(delay_file):
    delay_list = []
    with open(delay_file, 'r') as f:
        all_delay = f.read().split('\n', -1)
    for i in all_delay:
        if i == '':
            break;
        delay_list.append(int(i))
    return delay_list

def split_array_into(list, n) :
    lists = []
    begin = 0
    step = int(len(list) / n)
    for i in range(0, n):
        lists.append(list[begin : (i + 1) * step])
        begin = (i + 1) * step
    return lists

n = 6
fig, axes = plt.subplots(n,1,figsize=(20,20))


datetime_list = read_datetimes("BC26_20211031_REG_RTT_TCP_datas/ClientRegRTTDateTime.txt")
RTT_list = read_delay("BC26_20211031_REG_RTT_TCP_datas/ClientRegRTT.txt")
RTT_lists = split_array_into(RTT_list, n)
datetime_lists = split_array_into(datetime_list, n)

size_of_legend = 10

for i in range(0, n):
    df = pd.DataFrame({"values": RTT_lists[i], "datetime": datetime_lists[i]})
    axes[i].plot(df["datetime"], df["values"], label="Client_RTT", color='b', alpha=0.7)
    axes[i].legend(loc=1, prop={'size': size_of_legend})

datetime_list = read_datetimes("BC26_20211031_REG_RTT_TCP_datas/ServerRegRTTDateTime.txt")
RTT_list = read_delay("BC26_20211031_REG_RTT_TCP_datas/ServerRegRTT.txt")
RTT_lists = split_array_into(RTT_list, n)
datetime_lists = split_array_into(datetime_list, n)

for i in range(0, n):
    df = pd.DataFrame({"values": RTT_lists[i], "datetime": datetime_lists[i]})
    axes[i].plot(df["datetime"], df["values"], label="Server_RTT", color='g', alpha=0.7)
    axes[i].set_ylim(0, 6000)


plt.show()


