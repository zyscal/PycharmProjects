import os
import sys

import matplotlib.pyplot as plt
import matplotlib
from datetime import datetime
import pandas as pd


def twenty_two_to_eight(list):
    everylen = len(list) // 3
    list1 = list[0: everylen]
    list2 = list[everylen: 2 * everylen]
    list3 = list[2 * everylen:]
    return list1, list2, list3

def twenty_two_to_eight_value(list):
    everylen = len(list) // 3
    list1 = int(list[0: everylen])
    list2 = int(list[everylen: 2 * everylen])
    list3 = int(list[2 * everylen:])
    return list1, list2, list3

def findmax(item):
    max_value = 0
    for i in item:
        max_value = max(int(i), max_value)
    return max_value

# fig, axes = plt.subplots(6, 1, sharey=True, figsize=(21, 18))
fig, axes = plt.subplots(6, 1, figsize=(31.5, 27))
datetime_bc26_24h = []
value_bc26_24h = []
datetime_UpLink_bc26_24h = []
value_UpLink_bc26_24h = []
datetime_DownLink_bc26_24h = []
value_DownLink_bc26_24h = []

with open('20210101-20210102_datas/RTT_datetime_bc26_20210101-20210102.txt', 'r') as f:
    datetime_str = f.read().split('\n', -1)
for i in datetime_str:
    every = i.split(',', -1)
    tem_datetime = datetime(year=int(every[0]), month=int(every[1]), day=int(every[2]), hour=int(every[3]),
                            minute=int(every[4]), second=int(every[5]), microsecond=int(every[6]))
    datetime_bc26_24h.append(tem_datetime)

with open('20210101-20210102_datas/RTT_bc26_20210101-20210102.txt', 'r') as f:
    value_str = f.read().split(',', -1)
for i in value_str:
    value_bc26_24h.append(int(i))

with open('20210101-20210102_datas/bc26_24h_UpLink_value.txt', 'r') as f:
    value_str = f.read().split(',', -1)
for i in value_str:
    value_UpLink_bc26_24h.append(int(i))

with open('20210101-20210102_datas/bc26_24h_DownLink_value.txt', 'r') as f:
    value_str = f.read().split(',', -1)
for i in value_str:
    value_DownLink_bc26_24h.append(int(i))

with open('20210101-20210102_datas/bc26_24h_UpLink_datetime.txt', 'r') as f:
    datetime_str = f.read().split('\n', -1)
for i in datetime_str:
    every = i.split(',', -1)
    tem_datetime = datetime(year=int(every[0]), month=int(every[1]), day=int(every[2]), hour=int(every[3]),
                            minute=int(every[4]), second=int(every[5]), microsecond=int(every[6]))
    datetime_UpLink_bc26_24h.append(tem_datetime)

with open('20210101-20210102_datas/bc26_24h_DownLink_datetime.txt', 'r') as f:
    datetime_str = f.read().split('\n', -1)
for i in datetime_str:
    every = i.split(',', -1)
    tem_datetime = datetime(year=int(every[0]), month=int(every[1]), day=int(every[2]), hour=int(every[3]),
                            minute=int(every[4]), second=int(every[5]), microsecond=int(every[6]))
    datetime_DownLink_bc26_24h.append(tem_datetime)



value_bc26_0h_8h, value_bc26_8h_16h, value_bc26_16h_24h = twenty_two_to_eight(value_bc26_24h)
datetime_bc26_0h_8h, datetime_bc26_8h_16h, datetime_bc26_16h_24h = twenty_two_to_eight(datetime_bc26_24h)


value_UpLink_bc26_0h_8h, value_UpLink_bc26_8h_16h, value_UpLink_bc26_16h_24h = twenty_two_to_eight(value_UpLink_bc26_24h)
datetime_UpLink_bc26_0h_8h, datetime_UpLink_bc26_8h_16h, datetime_UpLink_bc26_16h_24h = twenty_two_to_eight(datetime_UpLink_bc26_24h)
value_DownLink_bc26_0h_8h, value_DownLink_bc26_8h_16h, value_DownLink_bc26_16h_24h = twenty_two_to_eight(value_DownLink_bc26_24h)
datetime_DownLink_bc26_0h_8h, datetime_DownLink_bc26_8h_16h, datetime_DownLink_bc26_16h_24h = twenty_two_to_eight(datetime_DownLink_bc26_24h)
IPchange=[]
Packet_loss=[]
ax1 = axes[0]
df1 = pd.DataFrame({"dates": datetime_bc26_0h_8h, "values": value_bc26_0h_8h})
ax1.plot(df1["dates"], df1["values"], label="BC26 RTT", color="b")
ax1.vlines(IPchange, 0, 6000, color='#F19EC2', label="IP change", linestyle='-.', linewidths=3)
ax1.vlines(Packet_loss, 0, 10000, color='r', label="BC26 loss")
ax1.set_xlim(datetime_bc26_0h_8h[0], datetime_bc26_0h_8h[len(datetime_bc26_0h_8h) - 1])
ax1.set_ylim(0, 6000)
ax1.locator_params('y', nbins=10)




ax2 = axes[1]
df2_1 = pd.DataFrame({"dates": datetime_UpLink_bc26_0h_8h, "values": value_UpLink_bc26_0h_8h})
df2_2 = pd.DataFrame({"dates": datetime_DownLink_bc26_0h_8h, "values": value_DownLink_bc26_0h_8h})
ax2.plot(df2_2["dates"], df2_2["values"], label="BC26 DownLink", color="g")
ax2.plot(df2_1["dates"], df2_1["values"], label="BC26 UpLink", color="y")
ax2.set_ylim(0,6000)
ax2.set_xlim(datetime_UpLink_bc26_0h_8h[0], datetime_UpLink_bc26_0h_8h[len(datetime_UpLink_bc26_0h_8h) - 1])


ax3 = axes[2]
df3 = pd.DataFrame({"dates": datetime_bc26_8h_16h, "values": value_bc26_8h_16h})
ax3.plot(df3["dates"], df3["values"], label="BC26 RTT", color="b")
ax3.set_xlim(datetime_bc26_8h_16h[0], datetime_bc26_8h_16h[len(datetime_bc26_8h_16h) - 1])
ax3.vlines(IPchange, 0, 6000, color='#F19EC2', label="IP change", linestyle='-.', linewidths=3)
ax3.vlines(Packet_loss, 0, 10000, color='r', label="BC26 loss")
# ax3.set_ylim(0, 6000)
ax3.locator_params('y', nbins=10)

ax4 = axes[3]
df4_1 = pd.DataFrame({"dates": datetime_UpLink_bc26_8h_16h, "values": value_UpLink_bc26_8h_16h})
df4_2 = pd.DataFrame({"dates": datetime_DownLink_bc26_8h_16h, "values": value_DownLink_bc26_8h_16h})
ax4.plot(df4_2["dates"], df4_2["values"], label="BC26 DownLink", color="g")
ax4.plot(df4_1["dates"], df4_1["values"], label="BC26 UpLink", color="y")
# ax4.set_ylim(0, 6000)
ax4.locator_params('y', nbins=10)
ax4.set_xlim(datetime_UpLink_bc26_8h_16h[0], datetime_UpLink_bc26_8h_16h[len(datetime_UpLink_bc26_8h_16h) - 1])


ax5 = axes[4]
df3 = pd.DataFrame({"dates": datetime_bc26_16h_24h, "values": value_bc26_16h_24h})
ax5.plot(df3["dates"], df3["values"], label="BC26 RTT", color="b")
ax5.vlines(IPchange, 0, 6000, color='#F19EC2', label="IP change", linestyle='-.', linewidths=3)
ax5.vlines(Packet_loss, 0, 10000, color='r', label="BC26 loss")
ax5.set_xlim(datetime_bc26_16h_24h[0], datetime_bc26_16h_24h[len(datetime_bc26_16h_24h) - 1])
ax5.set_ylim(0, 6000)
ax5.locator_params('y', nbins=10)


ax6 = axes[5]
df6_1 = pd.DataFrame({"dates": datetime_UpLink_bc26_16h_24h, "values": value_UpLink_bc26_16h_24h})
df6_2 = pd.DataFrame({"dates": datetime_DownLink_bc26_16h_24h, "values": value_DownLink_bc26_16h_24h})
ax6.plot(df6_2["dates"], df6_2["values"], label="BC26 DownLink", color="g")
ax6.plot(df6_1["dates"], df6_1["values"], label="BC26 UpLink", color="y")
ax6.set_ylim(0, 6000)
ax6.locator_params('y', nbins=10)
ax6.set_xlim(datetime_UpLink_bc26_16h_24h[0], datetime_UpLink_bc26_16h_24h[len(datetime_UpLink_bc26_16h_24h) - 1])


legend_size = 25

ax1.legend(loc=1, prop={'size': legend_size})
ax2.legend(loc=1, prop={'size': legend_size})
ax3.legend(loc=1, prop={'size': legend_size})
ax4.legend(loc=1, prop={'size': legend_size})
ax5.legend(loc=1, prop={'size': legend_size})
ax6.legend(loc=1, prop={'size': legend_size})

x_y_ticks_size = 20

plt.sca(axes[1])
plt.xticks(size=x_y_ticks_size, rotation=15)
plt.yticks(size=x_y_ticks_size)

plt.sca(axes[3])
plt.xticks(size=x_y_ticks_size, rotation=15)
plt.yticks(size=x_y_ticks_size)
plt.sca(axes[5])
plt.xticks(size=x_y_ticks_size, rotation=15)
plt.yticks(size=x_y_ticks_size)
plt.sca(axes[0])
plt.xticks([])
plt.yticks(size=x_y_ticks_size)
font2 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 45,
         }
plt.title("BC26 20210101-20210102", font2)
plt.sca(axes[2])
plt.xticks([])
plt.yticks(size=x_y_ticks_size)
plt.sca(axes[4])
plt.xticks([])
plt.yticks(size=x_y_ticks_size)

font1 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 35,
         }

ax1.set_ylabel("ms", font1, rotation=0, loc='top')


str = "JPG/" + os.path.basename(sys.argv[0]).split(".", -1)[0] + ".jpg"
plt.savefig(str)
plt.show()
