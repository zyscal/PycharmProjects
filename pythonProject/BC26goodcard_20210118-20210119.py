import os
import sys

import matplotlib.pyplot as plt
import matplotlib
from datetime import datetime
import pandas as pd


def twenty_two_to_eight(list):
    everylen = len(list) // 2
    list1 = list[0: everylen]
    list2 = list[everylen:]
    return list1, list2


def findmax(item):
    max_value = 0
    for i in item:
        max_value = max(int(i), max_value)
    return max_value

# fig, axes = plt.subplots(6, 1, sharey=True, figsize=(21, 18))
fig, axes = plt.subplots(4, 1, figsize=(42, 18))
datetime_bc26_12h = []
value_bc26_12h = []
datetime_UpLink_bc26_24h = []
value_UpLink_bc26_24h = []
datetime_DownLink_bc26_24h = []
value_DownLink_bc26_24h = []
Packet_loss=[]

with open('20210118-20210119_bc26_goodcard/RTT_datetime_bc26_goodcard_20210118-20210119.txt', 'r') as f:
    datetime_str = f.read().split('\n', -1)
for i in datetime_str:
    every = i.split(',', -1)
    tem_datetime = datetime(year=int(every[0]), month=int(every[1]), day=int(every[2]), hour=int(every[3]),
                            minute=int(every[4]), second=int(every[5]), microsecond=int(every[6]))
    datetime_bc26_12h.append(tem_datetime)

with open('20210118-20210119_bc26_goodcard/RTT_lost_bc26_goodcard_20210118-20210119.txt', 'r') as f:
    datetime_str = f.read().split('\n', -1)
for i in datetime_str:
    every = i.split(',', -1)
    tem_datetime = datetime(year=int(every[0]), month=int(every[1]), day=int(every[2]), hour=int(every[3]),
                            minute=int(every[4]), second=int(every[5]), microsecond=int(every[6]))
    Packet_loss.append(tem_datetime)

with open('20210118-20210119_bc26_goodcard/RTT_bc26_goodcard_20210118-20210119.txt', 'r') as f:
    value_str = f.read().split(',', -1)
for i in value_str:
    value_bc26_12h.append(int(i))




with open('20210118-20210119_bc26_goodcard/bc26_212h_UpLink_value.txt', 'r') as f:
    value_str = f.read().split(',', -1)
for i in value_str:
    value_UpLink_bc26_24h.append(int(i))

with open('20210118-20210119_bc26_goodcard/bc26_12h_DownLink_value.txt', 'r') as f:
    value_str = f.read().split(',', -1)
for i in value_str:
    value_DownLink_bc26_24h.append(int(i))

with open('20210118-20210119_bc26_goodcard/bc26_12h_UpLink_datetime.txt', 'r') as f:
    datetime_str = f.read().split('\n', -1)
for i in datetime_str:
    every = i.split(',', -1)
    tem_datetime = datetime(year=int(every[0]), month=int(every[1]), day=int(every[2]), hour=int(every[3]),
                            minute=int(every[4]), second=int(every[5]), microsecond=int(every[6]))
    datetime_UpLink_bc26_24h.append(tem_datetime)

with open('20210118-20210119_bc26_goodcard/bc26_12h_DownLink_datetime.txt', 'r') as f:
    datetime_str = f.read().split('\n', -1)
for i in datetime_str:
    every = i.split(',', -1)
    tem_datetime = datetime(year=int(every[0]), month=int(every[1]), day=int(every[2]), hour=int(every[3]),
                            minute=int(every[4]), second=int(every[5]), microsecond=int(every[6]))
    datetime_DownLink_bc26_24h.append(tem_datetime)



value_bc26_0h_4h, value_bc26_4h_8h = twenty_two_to_eight(value_bc26_12h)
datetime_bc26_0h_4h, datetime_bc26_4h_8h = twenty_two_to_eight(datetime_bc26_12h)
loss_bc26_0h_4h, loss_bc26_4h_8h = twenty_two_to_eight(Packet_loss)

value_UpLink_bc26_0h_4h, value_UpLink_bc26_4h_8h = twenty_two_to_eight(value_UpLink_bc26_24h)
datetime_UpLink_bc26_0h_4h, datetime_UpLink_bc26_4h_8h = twenty_two_to_eight(datetime_UpLink_bc26_24h)
value_DownLink_bc26_0h_4h, value_DownLink_bc26_4h_8h = twenty_two_to_eight(value_DownLink_bc26_24h)
datetime_DownLink_bc26_0h_4h, datetime_DownLink_bc26_4h_8h = twenty_two_to_eight(datetime_DownLink_bc26_24h)

ax1 = axes[0]
df1 = pd.DataFrame({"dates": datetime_bc26_0h_4h, "values": value_bc26_0h_4h})
ax1.plot(df1["dates"], df1["values"], label="BC26 RTT", color="b")
# ax1.vlines(IPchange, 0, 6000, color='#F19EC2', label="IP change", linestyle='-.', linewidths=3)
ax1.vlines(loss_bc26_0h_4h, 0, 10000, color='r', label="BC26 loss")
ax1.set_xlim(datetime_bc26_0h_4h[0], datetime_bc26_0h_4h[len(datetime_bc26_0h_4h) - 1])
ax1.set_ylim(0, 10000)
ax1.locator_params('y', nbins=10)
date_format = matplotlib.dates.DateFormatter('%H:%M:%S')




ax2 = axes[1]
df2_1 = pd.DataFrame({"dates": datetime_UpLink_bc26_0h_4h, "values": value_UpLink_bc26_0h_4h})
df2_2 = pd.DataFrame({"dates": datetime_DownLink_bc26_0h_4h, "values": value_DownLink_bc26_0h_4h})
ax2.plot(df2_2["dates"], df2_2["values"], label="BC26 DownLink", color="g")
ax2.plot(df2_1["dates"], df2_1["values"], label="BC26 UpLink", color="y")
ax2.set_ylim(0,10000)
ax2.set_xlim(datetime_UpLink_bc26_0h_4h[0], datetime_UpLink_bc26_0h_4h[len(datetime_UpLink_bc26_0h_4h) - 1])
ax2.locator_params('y', nbins=10)


ax3 = axes[2]
df3 = pd.DataFrame({"dates": datetime_bc26_4h_8h, "values": value_bc26_4h_8h})
ax3.plot(df3["dates"], df3["values"], label="BC26 RTT", color="b")
ax3.set_xlim(datetime_bc26_4h_8h[0], datetime_bc26_4h_8h[len(datetime_bc26_4h_8h) - 1])
# ax3.vlines(IPchange, 0, 6000, color='#F19EC2', label="IP change", linestyle='-.', linewidths=3)
ax3.vlines(loss_bc26_4h_8h, 0, 10000, color='r', label="BC26 loss")
ax3.set_ylim(0, 10000)
ax3.locator_params('y', nbins=10)

ax4 = axes[3]
df4_1 = pd.DataFrame({"dates": datetime_UpLink_bc26_4h_8h, "values": value_UpLink_bc26_4h_8h})
df4_2 = pd.DataFrame({"dates": datetime_DownLink_bc26_4h_8h, "values": value_DownLink_bc26_4h_8h})
ax4.plot(df4_2["dates"], df4_2["values"], label="BC26 DownLink", color="g")
ax4.plot(df4_1["dates"], df4_1["values"], label="BC26 UpLink", color="y")
ax4.set_ylim(0, 10000)
ax4.locator_params('y', nbins=10)
ax4.set_xlim(datetime_UpLink_bc26_4h_8h[0], datetime_UpLink_bc26_4h_8h[len(datetime_UpLink_bc26_4h_8h) - 1])
ax4.xaxis.set_major_formatter(date_format)


legend_size = 25

ax1.legend(loc=1, prop={'size': legend_size})
ax2.legend(loc=1, prop={'size': legend_size})
ax3.legend(loc=1, prop={'size': legend_size})
ax4.legend(loc=1, prop={'size': legend_size})

x_y_ticks_size = 25

plt.sca(axes[1])
plt.xticks(size=x_y_ticks_size)
plt.yticks(size=x_y_ticks_size)
plt.gca().xaxis.set_major_formatter(date_format)


plt.sca(axes[3])
plt.xticks(size=x_y_ticks_size)
plt.yticks(size=x_y_ticks_size)

plt.sca(axes[0])
plt.xticks([])
plt.yticks(size=x_y_ticks_size)
font2 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 45,
         }
plt.title("BC26 18:00 ~ 7:00", font2)
plt.sca(axes[2])
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
