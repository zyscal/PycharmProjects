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
# firmware_5700_UL_datetime_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_firmware_5700/app_bc26_20210221-20210222_firmware_5700_UL_datetime.txt'
# firmware_5700_UL_delay_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_firmware_5700/app_bc26_20210221-20210222_firmware_5700_UL_delay.txt'
firmware_5700_UL_loss_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_5700/app_bc26_20210221-20210222_5700_UL_loss.txt'
# firmware_5700_DL_datetime_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_firmware_5700/app_bc26_20210221-20210222_firmware_5700_DL_datetime.txt'
# firmware_5700_DL_delay_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_firmware_5700/app_bc26_20210221-20210222_firmware_5700_DL_delay.txt'
firmware_5700_DL_loss_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_5700/app_bc26_20210221-20210222_5700_DL_loss.txt'
firmware_5700_datetime_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_5700/app_bc26_20210221-20210222_5700_datetime.txt'
firmware_5700_RTT_file = '../app_bc26_20210221-20210222_datas/app_bc26_20210221-20210222_5700/app_bc26_20210221-20210222_5700_RTT.txt'

# firmware_5700_UL_datetime = []
# firmware_5700_UL_delay = []
# firmware_5700_DL_datetime = []
# firmware_5700_DL_delay = []
firmware_5700_loss = []
firmware_5700_datetime = []
firmware_5700_RTT = []


#firmware_5700
# firmware_5700_UL_datetime = read_datetimes(firmware_5700_UL_datetime_file)
# firmware_5700_UL_delay = read_delay(firmware_5700_UL_delay_file)
# firmware_5700_DL_datetime = read_datetimes(firmware_5700_DL_datetime_file)
# firmware_5700_DL_delay = read_delay(firmware_5700_DL_delay_file)
firmware_5700_loss = read_datetimes(firmware_5700_UL_loss_file) + read_datetimes(firmware_5700_DL_loss_file)
firmware_5700_datetime = read_datetimes(firmware_5700_datetime_file)
firmware_5700_RTT = read_delay(firmware_5700_RTT_file)


## make plot
fig, ax = plt.subplots(1, 1, figsize=(10,2.5))
size_of_legend = 10
##create plot
ax.set_title("Application-D RTT",size=20)
ax.vlines(firmware_5700_loss, ymin=0, ymax=9000, color='r', alpha=0.6)
# df0 = pd.DataFrame({"values":firmware_5700_UL_delay, "datetime":firmware_5700_UL_datetime})
# ax.plot(df0["datetime"], df0["values"], label="firmware_5700_UL", color='y')
# df0 = pd.DataFrame({"values":firmware_5700_DL_delay, "datetime":firmware_5700_DL_datetime})
# ax.plot(df0["datetime"], df0["values"], label="firmware_5700_UL", color='g', alpha=0.4)
df0 = pd.DataFrame({"values":firmware_5700_RTT, "datetime":firmware_5700_datetime})
ax.plot(df0["datetime"], df0["values"], label="firmware_5700_RTT", color='b', alpha=0.4)
# ax.hlines(y = 1971, xmin=firmware_5700_UL_datetime[0], xmax=firmware_5700_UL_datetime[len(firmware_5700_UL_datetime) - 1], color='y', linestyles='--', alpha = 0.4)
# ax.hlines(y = 3294, xmin=firmware_5700_DL_datetime[0], xmax=firmware_5700_DL_datetime[len(firmware_5700_DL_datetime) - 1], color='g', linestyles='--', alpha = 0.4)
ax.hlines(y = 2783, xmin=firmware_5700_datetime[0], xmax=firmware_5700_datetime[len(firmware_5700_datetime) - 1], color='b', linestyles='--', alpha = 0.4)
ax.legend(loc=1, prop={'size':size_of_legend})
ax.set_xlim(xmin=firmware_5700_datetime[0], xmax=firmware_5700_datetime[len(firmware_5700_datetime) - 1])
ax.set_ylim(0, 9000)


##show plot

str = "../JPG/BC26_20210221-20210222/" + os.path.basename(sys.argv[0]).split(".", -1)[0] + ".jpg"
plt.savefig(str)
plt.show()