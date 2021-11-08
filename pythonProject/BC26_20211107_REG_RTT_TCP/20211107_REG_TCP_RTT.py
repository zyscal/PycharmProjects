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

def find_RTT_by_datetime(retransmission_datetimes, df) :
    retransmission_rtts = []
    for j in retransmission_datetimes[i] :
        retransmission_rtt = df[df.datetime == j].index.tolist()
        print(retransmission_rtt)
        if len(retransmission_rtt) > 0:
            retransmission_rtts.append(df["values"][retransmission_rtt[len(retransmission_rtt) - 1]])
        else :
            print("not found")
            retransmission_rtts.append(0)
    return retransmission_rtts

n = 6
fig, axes = plt.subplots(n,1,figsize=(30,10))


datetime_list = read_datetimes("BC26_20211107_REG_RTT_TCP_datas/ClientRegDateTime.txt")
RTT_list = read_delay("BC26_20211107_REG_RTT_TCP_datas/ClientRegRTT.txt")

RTT_lists = split_array_into(RTT_list, n)
datetime_lists = split_array_into(datetime_list, n)

size_of_legend = 10
size_of_rtt_point = 3
size_of_retransmission_point = 30

for i in range(0, n):
    df = pd.DataFrame({"values": RTT_lists[i], "datetime": datetime_lists[i]})
    axes[i].plot(df["datetime"], df["values"], label="Client_RTT", color='b', alpha=0.7)
    axes[i].scatter(df["datetime"], df["values"], label="Client_RTT", color='b', s=size_of_rtt_point)

datetime_list = read_datetimes("BC26_20211107_REG_RTT_TCP_datas/ServerRegDateTime.txt")
RTT_list = read_delay("BC26_20211107_REG_RTT_TCP_datas/ServerRegRTT.txt")
RTT_lists = split_array_into(RTT_list, n)
datetime_lists = split_array_into(datetime_list, n)
Server_packet_loss = read_datetimes("BC26_20211107_REG_RTT_TCP_datas/Server_packet_loss.txt")
Server_packet_loss_datetims = split_datetimes_by_datetime(datetime_lists, Server_packet_loss)

for i in range(0, n):
    df = pd.DataFrame({"values": RTT_lists[i], "datetime": datetime_lists[i]})
    axes[i].plot(df["datetime"], df["values"], label="Server_RTT", color='g', alpha=0.7)
    axes[i].scatter(df["datetime"], df["values"], label="Server_RTT", color='g', alpha=0.7, s=size_of_rtt_point)
    axes[i].vlines(Server_packet_loss_datetims[i], 0, 6000, color='r')
    axes[i].set_ylim(0, 10000)
    axes[i].legend(loc=1, prop={'size': size_of_legend})

axes[0].set_title("20211107 21:00-7:00 LwM2M/CoAP/TCP/NB-IoT BC26 REG RTT", fontsize=20)
plt.show()


