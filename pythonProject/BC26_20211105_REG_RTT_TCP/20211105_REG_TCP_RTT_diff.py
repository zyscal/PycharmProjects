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

def find_diff(RTT_Client, RTT_Server):
    if len(RTT_Client) != len(RTT_Server) :
        print("there is something wrong , length of Clinet RTT != length of Server")
        return []
    RTT_diff = []
    j = 0
    while j < len(RTT_Client) :
        RTT_diff.append(RTT_Client[j] - RTT_Server[j])
        j += 1
    return RTT_diff

n = 6
fig, axes = plt.subplots(n,1,figsize=(30,10))
size_of_legend = 10
size_of_rtt_point = 3
size_of_retransmission_point = 30


datetime_list = read_datetimes("BC26_20211105_REG_RTT_TCP_datas/ClientRegDateTime_without_retransmission.txt")
RTT_list = read_delay("BC26_20211105_REG_RTT_TCP_datas/ClientRegRTT_without_retransmission.txt")

RTT_lists = split_array_into(RTT_list, n)
datetime_lists = split_array_into(datetime_list, n)

RTT_list_server = read_delay("BC26_20211105_REG_RTT_TCP_datas/ServerRegRTT_without_retransmission.txt")
RTT_lists_server = split_array_into(RTT_list_server, n)


for i in range(0, n):
    RTT_diff = find_diff(RTT_lists[i], RTT_lists_server[i])
    print(RTT_diff)
    df = pd.DataFrame({"values": RTT_diff, "datetime": datetime_lists[i]})
    axes[i].plot(df["datetime"], df["values"], label="Server_RTT", color='g', alpha=0.7)
    axes[i].scatter(df["datetime"], df["values"], label="Server_RTT", color='g', alpha=0.7, s=size_of_rtt_point)
    axes[i].set_ylim(-1000, 10000)
    axes[i].legend(loc=1, prop={'size': size_of_legend})


axes[0].set_title("20211105 22:00-13:30 LwM2M/CoAP/TCP/NB-IoT BC26 REG RTT diff", fontsize=20)
plt.show()


