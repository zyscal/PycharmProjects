import os
import sys

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import matplotlib
import numpy as np
from datetime import datetime
import pandas as pd


# make functions
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


## import data
observe503_UL_datetime_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_observe503/app_bc26_20210221-20210222_observe503_UL_datetime.txt'
observe503_UL_delay_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_observe503/app_bc26_20210221-20210222_observe503_UL_delay.txt'
observe503_UL_loss_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_observe503/app_bc26_20210221-20210222_observe503_UL_loss.txt'
observe503_DL_datetime_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_observe503/app_bc26_20210221-20210222_observe503_DL_datetime.txt'
observe503_DL_delay_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_observe503/app_bc26_20210221-20210222_observe503_DL_delay.txt'
observe503_DL_loss_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_observe503/app_bc26_20210221-20210222_observe503_DL_loss.txt'

URI_UL_datetime_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_URI/app_bc26_20210221-20210222_URI_UL_datetime.txt'
URI_UL_delay_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_URI/app_bc26_20210221-20210222_URI_UL_delay.txt'
URI_UL_loss_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_URI/app_bc26_20210221-20210222_URI_UL_loss.txt'
URI_DL_datetime_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_URI/app_bc26_20210221-20210222_URI_DL_datetime.txt'
URI_DL_delay_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_URI/app_bc26_20210221-20210222_URI_DL_delay.txt'
URI_DL_loss_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_URI/app_bc26_20210221-20210222_URI_DL_loss.txt'
URI_datetime_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_URI/app_bc26_20210221-20210222_URI_datetime.txt'
URI_RTT_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_URI/app_bc26_20210221-20210222_URI_RTT.txt'

observe34828029272_UL_datetime_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_observe34828029272/app_bc26_20210221-20210222_observe34828029272_UL_datetime.txt'
observe34828029272_UL_delay_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_observe34828029272/app_bc26_20210221-20210222_observe34828029272_UL_delay.txt'
observe34828029272_UL_loss_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_observe34828029272/app_bc26_20210221-20210222_observe34828029272_UL_loss.txt'
observe34828029272_DL_datetime_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_observe34828029272/app_bc26_20210221-20210222_observe34828029272_DL_datetime.txt'
observe34828029272_DL_delay_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_observe34828029272/app_bc26_20210221-20210222_observe34828029272_DL_delay.txt'
observe34828029272_DL_loss_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_observe34828029272/app_bc26_20210221-20210222_observe34828029272_DL_loss.txt'
observe34828029272_datetime_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_observe34828029272/app_bc26_20210221-20210222_observe34828029272_datetime.txt'
observe34828029272_RTT_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_observe34828029272/app_bc26_20210221-20210222_observe34828029272_RTT.txt'

read34828_UL_datetime_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_read34828/app_bc26_20210221-20210222_read34828_UL_datetime.txt'
read34828_UL_delay_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_read34828/app_bc26_20210221-20210222_read34828_UL_delay.txt'
read34828_UL_loss_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_read34828/app_bc26_20210221-20210222_read34828_UL_loss.txt'
read34828_DL_datetime_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_read34828/app_bc26_20210221-20210222_read34828_DL_datetime.txt'
read34828_DL_delay_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_read34828/app_bc26_20210221-20210222_read34828_DL_delay.txt'
read34828_DL_loss_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_read34828/app_bc26_20210221-20210222_read34828_DL_loss.txt'
read34828_datetime_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_read34828/app_bc26_20210221-20210222_read34828_datetime.txt'
read34828_RTT_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_read34828/app_bc26_20210221-20210222_read34828_RTT.txt'

observe503_UL_datetime = []
observe503_UL_delay = []
observe503_DL_datetime = []
observe503_DL_delay = []
observe503_loss = []

URI_UL_datetime = []
URI_UL_delay = []
URI_DL_datetime = []
URI_DL_delay = []
URI_loss = []

observe34828029272_UL_datetime = []
observe34828029272_UL_delay = []
observe34828029272_DL_datetime = []
observe34828029272_DL_delay = []
observe34828029272_loss = []

read34828_UL_datetime = []
read34828_UL_delay = []
read34828_DL_datetime = []
read34828_DL_delay = []
read34828_loss = []
# observe503
observe503_UL_datetime = read_datetimes(observe503_UL_datetime_file)
observe503_UL_delay = read_delay(observe503_UL_delay_file)
observe503_DL_datetime = read_datetimes(observe503_DL_datetime_file)
observe503_DL_delay = read_delay(observe503_DL_delay_file)
observe503_loss = read_datetimes(observe503_UL_loss_file) + read_datetimes(observe503_DL_loss_file)

# URI
URI_UL_datetime = read_datetimes(URI_UL_datetime_file)
URI_UL_delay = read_delay(URI_UL_delay_file)
URI_DL_datetime = read_datetimes(URI_DL_datetime_file)
URI_DL_delay = read_delay(URI_DL_delay_file)
URI_loss = read_datetimes(URI_UL_loss_file) + read_datetimes(URI_DL_loss_file)
# observe34828029272
observe34828029272_UL_datetime = read_datetimes(observe34828029272_UL_datetime_file)
observe34828029272_UL_delay = read_delay(observe34828029272_UL_delay_file)
observe34828029272_DL_datetime = read_datetimes(observe34828029272_DL_datetime_file)
observe34828029272_DL_delay = read_delay(observe34828029272_DL_delay_file)
observe34828029272_loss = read_datetimes(observe34828029272_UL_loss_file) + read_datetimes(observe34828029272_DL_loss_file)


## make plot
fig, axes = plt.subplots(3, 1, figsize=(10, 7.5))
size_of_legend = 10
##create plot
ax = axes[0]
ax.set_title("Application-B UL/DL delay", size=20)
ax.vlines(observe503_loss, ymin=0, ymax=9000, color='r', alpha=0.6)
df0 = pd.DataFrame({"values": observe503_UL_delay, "datetime": observe503_UL_datetime})
ax.plot(df0["datetime"], df0["values"], label="read1_UL", color='y')
df0 = pd.DataFrame({"values": observe503_DL_delay, "datetime": observe503_DL_datetime})
ax.plot(df0["datetime"], df0["values"], label="read1_DL", color='g', alpha=0.4)

ax.hlines(y=1689, xmin=observe503_UL_datetime[0], xmax=observe503_UL_datetime[len(observe503_UL_datetime) - 1],
          color='y', linestyles='--', alpha=0.4)
ax.hlines(y=801, xmin=observe503_DL_datetime[0], xmax=observe503_DL_datetime[len(observe503_DL_datetime) - 1],
          color='g', linestyles='--', alpha=0.4)
ax.legend(loc=1, prop={'size': size_of_legend})
ax.set_xlim(xmin=observe503_UL_datetime[0], xmax=observe503_UL_datetime[len(observe503_UL_datetime) - 1])
ax.set_ylim(0, 9000)

ax = axes[1]
ax.vlines(URI_loss, ymin=0, ymax=9000, color='r', alpha=0.6)
df1 = pd.DataFrame({"values": URI_UL_delay, "datetime": URI_UL_datetime})
ax.plot(df1["datetime"], df1["values"], label="read5_UL", color='y')
df1 = pd.DataFrame({"values": URI_DL_delay, "datetime": URI_DL_datetime})
ax.plot(df1["datetime"], df1["values"], label="read5_DL", color='g', alpha=0.4)
ax.hlines(y=1910, xmin=URI_UL_datetime[0], xmax=URI_UL_datetime[len(URI_UL_datetime) - 1], color='y',
          linestyles='--', alpha=0.4)
ax.hlines(y=1121, xmin=URI_DL_datetime[0], xmax=URI_DL_datetime[len(URI_DL_datetime) - 1], color='g',
          linestyles='--', alpha=0.4)
ax.legend(loc=1, prop={'size': size_of_legend})
ax.set_xlim(xmin=URI_UL_datetime[0], xmax=URI_UL_datetime[len(URI_UL_datetime) - 1])
ax.set_ylim(0, 9000)

ax = axes[2]
ax.vlines(observe34828029272_loss, ymin=0, ymax=9000, color='r', alpha=0.6)
df2 = pd.DataFrame({"values": observe34828029272_UL_delay, "datetime": observe34828029272_UL_datetime})
ax.plot(df2["datetime"], df2["values"], label="observe34828029272_UL", color='y')
df2 = pd.DataFrame({"values": observe34828029272_DL_delay, "datetime": observe34828029272_DL_datetime})
ax.plot(df2["datetime"], df2["values"], label="observe34828029272_DL", color='g', alpha=0.4)
ax.hlines(y=1737, xmin=observe34828029272_UL_datetime[0], xmax=observe34828029272_UL_datetime[len(observe34828029272_UL_datetime) - 1], color='y',
          linestyles='--', alpha=0.4)
ax.hlines(y=955, xmin=observe34828029272_DL_datetime[0], xmax=observe34828029272_DL_datetime[len(observe34828029272_DL_datetime) - 1], color='g',
          linestyles='--', alpha=0.4)
ax.legend(loc=1, prop={'size': size_of_legend})
ax.set_xlim(xmin=observe34828029272_UL_datetime[0], xmax=observe34828029272_UL_datetime[len(observe34828029272_UL_datetime) - 1])
ax.set_ylim(0, 9000)


##show plot

str = "../JPG/BC26_20210221-20210222/" + os.path.basename(sys.argv[0]).split(".", -1)[0] + ".jpg"
plt.savefig(str)
plt.show()
