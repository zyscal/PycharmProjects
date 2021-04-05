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
## import data
read1_UL_datetime_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_read1/app_bc26_20210221-20210222_read1_UL_datetime.txt'
read1_UL_delay_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_read1/app_bc26_20210221-20210222_read1_UL_delay.txt'
read1_UL_loss_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_read1/app_bc26_20210221-20210222_read1_UL_loss.txt'
read1_DL_datetime_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_read1/app_bc26_20210221-20210222_read1_DL_datetime.txt'
read1_DL_delay_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_read1/app_bc26_20210221-20210222_read1_DL_delay.txt'
read1_DL_loss_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_read1/app_bc26_20210221-20210222_read1_DL_loss.txt'



read5_UL_datetime_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_read5/app_bc26_20210221-20210222_read5_UL_datetime.txt'
read5_UL_delay_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_read5/app_bc26_20210221-20210222_read5_UL_delay.txt'
read5_UL_loss_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_read5/app_bc26_20210221-20210222_read5_UL_loss.txt'
read5_DL_datetime_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_read5/app_bc26_20210221-20210222_read5_DL_datetime.txt'
read5_DL_delay_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_read5/app_bc26_20210221-20210222_read5_DL_delay.txt'
read5_DL_loss_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_read5/app_bc26_20210221-20210222_read5_DL_loss.txt'
read5_datetime_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_read5/app_bc26_20210221-20210222_read5_datetime.txt'
read5_RTT_fild = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_read5/app_bc26_20210221-20210222_read5_RTT.txt'


read3333_UL_datetime_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_read3333/app_bc26_20210221-20210222_read3333_UL_datetime.txt'
read3333_UL_delay_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_read3333/app_bc26_20210221-20210222_read3333_UL_delay.txt'
read3333_UL_loss_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_read3333/app_bc26_20210221-20210222_read3333_UL_loss.txt'
read3333_DL_datetime_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_read3333/app_bc26_20210221-20210222_read3333_DL_datetime.txt'
read3333_DL_delay_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_read3333/app_bc26_20210221-20210222_read3333_DL_delay.txt'
read3333_DL_loss_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_read3333/app_bc26_20210221-20210222_read3333_DL_loss.txt'
read3333_datetime_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_read3333/app_bc26_20210221-20210222_read3333_datetime.txt'
read3333_RTT_fild = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_read3333/app_bc26_20210221-20210222_read3333_RTT.txt'


read34828_UL_datetime_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_read34828/app_bc26_20210221-20210222_read34828_UL_datetime.txt'
read34828_UL_delay_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_read34828/app_bc26_20210221-20210222_read34828_UL_delay.txt'
read34828_UL_loss_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_read34828/app_bc26_20210221-20210222_read34828_UL_loss.txt'
read34828_DL_datetime_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_read34828/app_bc26_20210221-20210222_read34828_DL_datetime.txt'
read34828_DL_delay_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_read34828/app_bc26_20210221-20210222_read34828_DL_delay.txt'
read34828_DL_loss_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_read34828/app_bc26_20210221-20210222_read34828_DL_loss.txt'
read34828_datetime_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_read34828/app_bc26_20210221-20210222_read34828_datetime.txt'
read34828_RTT_fild = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_read34828/app_bc26_20210221-20210222_read34828_RTT.txt'

read1_UL_datetime = []
read1_UL_delay = []
read1_DL_datetime = []
read1_DL_delay = []
read1_loss = []


read5_UL_datetime = []
read5_UL_delay = []
read5_DL_datetime = []
read5_DL_delay = []
read5_loss = []

read3333_UL_datetime = []
read3333_UL_delay = []
read3333_DL_datetime = []
read3333_DL_delay = []
read3333_loss = []

read34828_UL_datetime = []
read34828_UL_delay = []
read34828_DL_datetime = []
read34828_DL_delay = []
read34828_loss = []
#read1
read1_UL_datetime = read_datetimes(read1_UL_datetime_file)
read1_UL_delay = read_delay(read1_UL_delay_file)
read1_DL_datetime = read_datetimes(read1_DL_datetime_file)
read1_DL_delay = read_delay(read1_DL_delay_file)
read1_loss = read_datetimes(read1_UL_loss_file) + read_datetimes(read1_DL_loss_file)

#read5
read5_UL_datetime = read_datetimes(read5_UL_datetime_file)
read5_UL_delay = read_delay(read5_UL_delay_file)
read5_DL_datetime = read_datetimes(read5_DL_datetime_file)
read5_DL_delay = read_delay(read5_DL_delay_file)
read5_loss = read_datetimes(read5_UL_loss_file) + read_datetimes(read5_DL_loss_file)
#read3333
read3333_UL_datetime = read_datetimes(read3333_UL_datetime_file)
read3333_UL_delay = read_delay(read3333_UL_delay_file)
read3333_DL_datetime = read_datetimes(read3333_DL_datetime_file)
read3333_DL_delay = read_delay(read3333_DL_delay_file)
read3333_loss = read_datetimes(read3333_UL_loss_file) + read_datetimes(read3333_DL_loss_file)
#read34828
read34828_UL_datetime = read_datetimes(read34828_UL_datetime_file)
read34828_UL_delay = read_delay(read34828_UL_delay_file)
read34828_DL_datetime = read_datetimes(read34828_DL_datetime_file)
read34828_DL_delay = read_delay(read34828_DL_delay_file)
read34828_loss = read_datetimes(read34828_UL_loss_file) + read_datetimes(read34828_DL_loss_file)



## make plot
fig, axes = plt.subplots(4, 1, figsize=(10,10))
size_of_legend = 10
##create plot
ax = axes[0]
ax.set_title("Application-A UL/DL delay",size=20)
ax.vlines(read1_loss, ymin=0, ymax=9000, color='r', alpha=0.6)
df0 = pd.DataFrame({"values":read1_UL_delay, "datetime":read1_UL_datetime})
ax.plot(df0["datetime"], df0["values"], label="read1_UL", color='y')
df0 = pd.DataFrame({"values":read1_DL_delay, "datetime":read1_DL_datetime})
ax.plot(df0["datetime"], df0["values"], label="read1_DL", color='g', alpha=0.4)

ax.hlines(y = 1971, xmin=read1_UL_datetime[0], xmax=read1_UL_datetime[len(read1_UL_datetime) - 1], color='y', linestyles='--', alpha = 0.4)
ax.hlines(y = 3294, xmin=read1_DL_datetime[0], xmax=read1_DL_datetime[len(read1_DL_datetime) - 1], color='g', linestyles='--', alpha = 0.4)
ax.legend(loc=1, prop={'size':size_of_legend})
ax.set_xlim(xmin=read1_UL_datetime[0], xmax=read1_UL_datetime[len(read1_UL_datetime) - 1])
ax.set_ylim(0, 9000)


ax =axes[1]
ax.vlines(read5_loss, ymin=0, ymax=9000, color='r', alpha=0.6)
df1 = pd.DataFrame({"values":read5_UL_delay, "datetime":read5_UL_datetime})
ax.plot(df1["datetime"], df1["values"], label="read5_UL", color='y')
df1 = pd.DataFrame({"values":read5_DL_delay, "datetime":read5_DL_datetime})
ax.plot(df1["datetime"], df1["values"], label="read5_DL", color='g', alpha=0.4)
ax.hlines(y = 1865, xmin=read5_UL_datetime[0], xmax=read5_UL_datetime[len(read5_UL_datetime) - 1], color='y', linestyles='--', alpha = 0.4)
ax.hlines(y = 782, xmin=read5_DL_datetime[0], xmax=read5_DL_datetime[len(read5_DL_datetime) - 1], color='g', linestyles='--', alpha = 0.4)
ax.legend(loc=1, prop={'size':size_of_legend})
ax.set_xlim(xmin=read5_UL_datetime[0], xmax=read5_UL_datetime[len(read5_UL_datetime) - 1])
ax.set_ylim(0, 9000)



ax =axes[2]
ax.vlines(read3333_loss, ymin=0, ymax=9000, color='r', alpha=0.6)
df2 = pd.DataFrame({"values":read3333_UL_delay, "datetime":read3333_UL_datetime})
ax.plot(df2["datetime"], df2["values"], label="read3333_UL", color='y')
df2 = pd.DataFrame({"values":read3333_DL_delay, "datetime":read3333_DL_datetime})
ax.plot(df2["datetime"], df2["values"], label="read3333_DL", color='g', alpha=0.4)
ax.hlines(y = 2713, xmin=read3333_UL_datetime[0], xmax=read3333_UL_datetime[len(read3333_UL_datetime) - 1], color='y', linestyles='--', alpha = 0.4)
ax.hlines(y = 747, xmin=read3333_DL_datetime[0], xmax=read3333_DL_datetime[len(read3333_DL_datetime) - 1], color='g', linestyles='--', alpha = 0.4)
ax.legend(loc=1, prop={'size':size_of_legend})
ax.set_xlim(xmin=read3333_UL_datetime[0], xmax=read3333_UL_datetime[len(read3333_UL_datetime) - 1])
ax.set_ylim(0, 9000)



ax =axes[3]
print(len(read34828_loss))
ax.vlines(read34828_loss, ymin=0, ymax=9000, color='r', alpha=0.6)
df3 = pd.DataFrame({"values":read34828_UL_delay, "datetime":read34828_UL_datetime})
ax.plot(df3["datetime"], df3["values"], label="read34828_UL", color='y')
df3 = pd.DataFrame({"values":read34828_DL_delay, "datetime":read34828_DL_datetime})
ax.plot(df3["datetime"], df3["values"], label="read34828_DL", color='g', alpha=0.4)
ax.hlines(y = 1695, xmin=read34828_UL_datetime[0], xmax=read34828_UL_datetime[len(read34828_UL_datetime) - 1], color='y', linestyles='--', alpha = 0.4)
ax.hlines(y = 457, xmin=read34828_DL_datetime[0], xmax=read34828_DL_datetime[len(read34828_DL_datetime) - 1], color='g', linestyles='--', alpha = 0.4)
ax.legend(loc=1, prop={'size':size_of_legend})
ax.set_xlim(xmin=read34828_UL_datetime[0], xmax=read34828_UL_datetime[len(read34828_UL_datetime) - 1])
ax.set_ylim(0, 9000)

##show plot

str = "../JPG/BC26_20210221-20210222/" + os.path.basename(sys.argv[0]).split(".", -1)[0] + ".jpg"
plt.savefig(str)
plt.show()