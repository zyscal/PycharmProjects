import os
import sys

import matplotlib.pyplot as plt

from matplotlib.font_manager import FontProperties
import matplotlib
import numpy as np
from datetime import datetime
import pandas as pd
#make functions
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
        all_delay = f.read().split(',', -1)
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

#根据lista[[]] 将listb分割为对应份数
def split_datetimes_by_datetime(lista, listb) :
    lists = []
    for i in lista :
        min = i[0]
        max = i[len(i) - 1]
        temlist = []
        for j in listb:
            if j >= min and j <= max :
                temlist.append(j)
        lists.append(temlist)
    return lists

## import data
n = 4
RTT_list = read_delay("BC26_20211101_REG_RTT_UDP_datas/ClinetRTT.txt")
datetime_list = read_datetimes("BC26_20211101_REG_RTT_UDP_datas/ClinetRTT_datetime.txt")
retransmission_datetime = read_datetimes("BC26_20211101_REG_RTT_UDP_datas/retransmission_file.txt")
RTT_lists = split_array_into(RTT_list, n)
datetime_lists = split_array_into(datetime_list, n)
retransmission_datetimes = split_datetimes_by_datetime(datetime_lists, retransmission_datetime)

print("Client std : ", np.std(RTT_list))



## make plot
fig, axes = plt.subplots(n, 1, figsize=(30,10))
size_of_rtt_point = 3
size_of_retransmission_point = 15
size_of_legend = 10

for i in range(0, n):
    df = pd.DataFrame({"values": RTT_lists[i], "datetime": datetime_lists[i]})
    retransmission_rtts = []
    for j in retransmission_datetimes[i] :
        retransmission_rtt = df[df.datetime == j].index.tolist()
        if len(retransmission_rtt) > 0:
            retransmission_rtts.append(df["values"][retransmission_rtt[len(retransmission_rtt) - 1]])
        else :
            retransmission_rtts.append(0)
    axes[i].plot(df["datetime"], df["values"], label="Client_RTT", color='b', alpha=0.6)
    axes[i].scatter(df["datetime"], df["values"], color='b', alpha=0.6, s=size_of_rtt_point)
    axes[i].scatter(retransmission_datetimes[i], retransmission_rtts, color='r', s=size_of_retransmission_point)
    axes[i].set_ylim(0, 10000)
    axes[i].set_xlim(datetime_lists[i][0], datetime_lists[i][len(datetime_lists[i]) - 1])
    axes[i].legend(loc=1, prop={'size': size_of_legend})


axes[0].set_title("20211101 22:30 - 13:30 LwM2M/CoAP/UDP/NB-IoT BC26 REG RTT", fontsize=20)
plt.show()