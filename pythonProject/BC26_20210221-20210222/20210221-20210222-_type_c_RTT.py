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
# REG_UL_datetime_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_REG/app_bc26_20210221-20210222_REG_UL_datetime.txt'
# REG_UL_delay_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_REG/app_bc26_20210221-20210222_REG_UL_delay.txt'
REG_UL_loss_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_REG/app_bc26_20210221-20210222_REG_UL_loss.txt'
# REG_DL_datetime_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_REG/app_bc26_20210221-20210222_REG_DL_datetime.txt'
# REG_DL_delay_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_REG/app_bc26_20210221-20210222_REG_DL_delay.txt'
REG_DL_loss_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_REG/app_bc26_20210221-20210222_REG_DL_loss.txt'
REG_datetime_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_REG/app_bc26_20210221-20210222_REG_datetime.txt'
REG_RTT_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_REG/app_bc26_20210221-20210222_REG_RTT.txt'

#
# UPD_UL_datetime_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_UPD/app_bc26_20210221-20210222_UPD_UL_datetime.txt'
# UPD_UL_delay_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_UPD/app_bc26_20210221-20210222_UPD_UL_delay.txt'
UPD_UL_loss_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_UPD/app_bc26_20210221-20210222_UPD_UL_loss.txt'
# UPD_DL_datetime_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_UPD/app_bc26_20210221-20210222_UPD_DL_datetime.txt'
# UPD_DL_delay_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_UPD/app_bc26_20210221-20210222_UPD_DL_delay.txt'
UPD_DL_loss_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_UPD/app_bc26_20210221-20210222_UPD_DL_loss.txt'
UPD_datetime_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_UPD/app_bc26_20210221-20210222_UPD_datetime.txt'
UPD_RTT_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_UPD/app_bc26_20210221-20210222_UPD_RTT.txt'



# REG_UL_datetime = []
# REG_UL_delay = []
# REG_DL_datetime = []
# REG_DL_delay = []
REG_loss = []
REG_datetime = []
REG_RTT = []

# UPD_UL_datetime = []
# UPD_UL_delay = []
# UPD_DL_datetime = []
# UPD_DL_delay = []
UPD_loss = []
UPD_datetime = []
UPD_RTT = []



#REG
# REG_UL_datetime = read_datetimes(REG_UL_datetime_file)
# REG_UL_delay = read_delay(REG_UL_delay_file)
# REG_DL_datetime = read_datetimes(REG_DL_datetime_file)
# REG_DL_delay = read_delay(REG_DL_delay_file)
REG_loss = read_datetimes(REG_UL_loss_file) + read_datetimes(REG_DL_loss_file)
REG_datetime = read_datetimes(REG_datetime_file)
REG_RTT = read_delay(REG_RTT_file)
#UPD
# UPD_UL_datetime = read_datetimes(UPD_UL_datetime_file)
# UPD_UL_delay = read_delay(UPD_UL_delay_file)
# UPD_DL_datetime = read_datetimes(UPD_DL_datetime_file)
# UPD_DL_delay = read_delay(UPD_DL_delay_file)
UPD_loss = read_datetimes(UPD_UL_loss_file) + read_datetimes(UPD_DL_loss_file)
UPD_datetime = read_datetimes(UPD_datetime_file)
UPD_RTT = read_delay(UPD_RTT_file)




## make plot
fig, axes = plt.subplots(2, 1, figsize=(10,5))
size_of_legend = 10
##create plot
ax = axes[0]
ax.set_title("Application-C RTT",size=20)
ax.vlines(REG_loss, ymin=0, ymax=9000, color='r', alpha=0.6)
# df0 = pd.DataFrame({"values":REG_UL_delay, "datetime":REG_UL_datetime})
# ax.plot(df0["datetime"], df0["values"], label="REG_UL", color='y')
# df0 = pd.DataFrame({"values":REG_DL_delay, "datetime":REG_DL_datetime})
# ax.plot(df0["datetime"], df0["values"], label="REG_UL", color='g', alpha=0.4)
df0 = pd.DataFrame({"values":REG_RTT, "datetime":REG_datetime})
ax.plot(df0["datetime"], df0["values"], label="REG_RTT", color='b', alpha=0.4)
# ax.hlines(y = 1971, xmin=REG_UL_datetime[0], xmax=REG_UL_datetime[len(REG_UL_datetime) - 1], color='y', linestyles='--', alpha = 0.4)
# ax.hlines(y = 3294, xmin=REG_DL_datetime[0], xmax=REG_DL_datetime[len(REG_DL_datetime) - 1], color='g', linestyles='--', alpha = 0.4)
ax.hlines(y = 4276, xmin=REG_datetime[0], xmax=REG_datetime[len(REG_datetime) - 1], color='b', linestyles='--', alpha = 0.4)
ax.legend(loc=1, prop={'size':size_of_legend})
ax.set_xlim(xmin=REG_datetime[0], xmax=REG_datetime[len(REG_datetime) - 1])
ax.set_ylim(0, 9000)


ax =axes[1]
ax.vlines(UPD_loss, ymin=0, ymax=9000, color='r', alpha=0.4, linewidth=0.1)
# df1 = pd.DataFrame({"values":UPD_UL_delay, "datetime":UPD_UL_datetime})
# ax.plot(df1["datetime"], df1["values"], label="UPD_UL", color='y')
# df1 = pd.DataFrame({"values":UPD_DL_delay, "datetime":UPD_DL_datetime})
# ax.plot(df1["datetime"], df1["values"], label="UPD_UL", color='g', alpha=0.4)
# ax.hlines(y = 1865, xmin=UPD_UL_datetime[0], xmax=UPD_UL_datetime[len(UPD_UL_datetime) - 1], color='y', linestyles='--', alpha = 0.4)
# ax.hlines(y = 782, xmin=UPD_DL_datetime[0], xmax=UPD_DL_datetime[len(UPD_DL_datetime) - 1], color='g', linestyles='--', alpha = 0.4)
df0 = pd.DataFrame({"values":UPD_RTT, "datetime":UPD_datetime})
ax.plot(df0["datetime"], df0["values"], label="UPD_RTT", color='b', alpha=0.4)
ax.hlines(y = 2712, xmin=UPD_datetime[0], xmax=UPD_datetime[len(UPD_datetime) - 1], color='b', linestyles='--', alpha = 0.4)
ax.legend(loc=1, prop={'size':size_of_legend})
ax.set_xlim(xmin=UPD_datetime[0], xmax=UPD_datetime[len(UPD_datetime) - 1])
ax.set_ylim(0, 9000)



##show plot

str = "../JPG/BC26_20210221-20210222/" + os.path.basename(sys.argv[0]).split(".", -1)[0] + ".jpg"
plt.savefig(str)
plt.show()