import os
import sys

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import matplotlib
import numpy as np
from datetime import datetime, timedelta
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

def split_datetime(datetime_list, n) :
    lists = []
    tem_list = []
    step = (datetime_list[len(datetime_list) - 1] - datetime_list[0]) / n
    end = datetime_list[0] + step
    for i in range(0, len(datetime_list)) :
        if datetime_list[i] <= end :
            tem_list.append(datetime_list[i])
            i += 1
            continue
        else :
            lists.append(tem_list)
            tem_list = []
            end += step
            continue
    if len(tem_list) != 0 :
        lists.append(tem_list)
    return lists

def split_rtt_by_datetime(RTT_list, datatime_lists) :
    RTT_lists = []
    j = 0
    for i in datatime_lists:
        length = len(i)
        tem_RTT_lists = []
        for k in range(0, length):
            tem_RTT_lists.append(RTT_list[j])
            j += 1
        RTT_lists.append(tem_RTT_lists)
    return RTT_lists

def split_rtt_by_interval (rtt_list, datetime_list, datetime_change) :
    rtt_lists = []
    datetime_list_iter = 0
    for i in datetime_change :
        tem_rtt_lists = []
        while  datetime_list_iter < len(datetime_list) and  datetime_list[datetime_list_iter] < i:
            tem_rtt_lists.append(rtt_list[datetime_list_iter])
            datetime_list_iter += 1
        rtt_lists.append(tem_rtt_lists)
    return rtt_lists



n = 6
fig, axes = plt.subplots(n,1,figsize=(30,10))


datetime_list = read_datetimes("BC26_20211108_REG_RTT_TCP_datas/ClientRegDateTime.txt")
RTT_list = read_delay("BC26_20211108_REG_RTT_TCP_datas/ClientRegRTT.txt")
datetime_lists = split_datetime(datetime_list, n)
RTT_lists = split_rtt_by_datetime(RTT_list, datetime_lists)

# 创建时间间隔
datetime_change = []
datetime_begin = datetime_list[0]
datetime_interval = timedelta(minutes=50)
for i in range(1, 21):
    datetime_change.append(datetime_begin + datetime_interval * i)
datetime_splited = split_datetimes_by_datetime(datetime_lists, datetime_change)



size_of_legend = 5
size_of_rtt_point = 3
size_of_retransmission_point = 30


RTT_list_server = read_delay("BC26_20211108_REG_RTT_TCP_datas/ServerRegRTT_without_retransmission.txt")
RTT_lists_server = split_rtt_by_datetime(RTT_list_server, datetime_lists)


diff_all = []
diff_datetime = []

for i in range(0, n):
    RTT_diff = find_diff(RTT_lists[i], RTT_lists_server[i])
    for j in RTT_diff :
        diff_all.append(j)
    for j in datetime_lists[i] :
        diff_datetime.append(j)
    df = pd.DataFrame({"values": RTT_diff, "datetime": datetime_lists[i]})
    axes[i].plot(df["datetime"], df["values"], label="Server_Client_RTT_diff", color='y', alpha=0.7)
    axes[i].scatter(df["datetime"], df["values"], label="Server_Client_RTT_diff", color='y', alpha=0.7, s=size_of_rtt_point)
    axes[i].set_ylim(-2000, 10000)
    axes[i].hlines(y=0, xmin=datetime_lists[i][0], xmax=datetime_lists[i][len(datetime_lists[i]) - 1])
    axes[i].vlines(datetime_splited[i], -2000, 10000, color='#A9A9A9', linestyle='-',linewidth=5)
    axes[i].legend(loc=1, prop={'size': size_of_legend})


diff_50 = split_rtt_by_interval(diff_all, diff_datetime, datetime_change)
print("diff_50 len is : ", len(diff_50))
print("基站延时")
for i in diff_50:
    print(int(np.average(i)))
print("标准差")
for i in diff_50:
    print(int(np.std(i)))



axes[0].set_title("20211108 17:00-10:00 LwM2M/CoAP/TCP/NB-IoT BC26 REG RTT diff" , fontsize=20)
plt.show()


