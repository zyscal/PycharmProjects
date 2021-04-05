import os
import sys

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from datetime import datetime
import pandas as pd

# make figure
fig, axes = plt.subplots(2, 2)


# make functions
def swap(a, b):
    return b, a


def sort(first_par, second_par, third_par, forth_par=None):
    if forth_par is None:
        forth_par = []
    j = 0
    check_order = False
    while True:
        i = j
        while (i + 1 < len(first_par)) and (first_par[i + 1] < first_par[i]):
            first_par[i], first_par[i + 1] = swap(first_par[i], first_par[i + 1])
            second_par[i], second_par[i + 1] = swap(second_par[i], second_par[i + 1])
            third_par[i], third_par[i + 1] = swap(third_par[i], third_par[i + 1])
            if len(forth_par) != 0:
                forth_par[i], forth_par[i + 1] = swap(forth_par[i], forth_par[i + 1])
            check_order = True
            i += 1
        j += 1
        if j == len(first_par) and not check_order:
            break
        elif j == len(first_par):
            check_order = False
            j = 0
    return first_par, second_par, third_par


# handle datas
# UL_packet_size = [37, 43, 260, 28, 24, 20, 24, 88, 34, 25, 25, 25, 40]
# UL_delay = [1971, 1865, 2713, 1695, 1689, 1910, 1737, 2054, 1993, 2082, 1706, 1906, 1757]
# UL_packet_speed_0_1 = [10.03, 10.03, 10.03, 10.03, 10.03, 29.79, 10.62, 10.0, 15.29, 30.0, 10.21, 19.99, 11.27]
# rate_lost_global = [1.30, 0, 0, 0.34, 0, 0.68, 2.04, 3.54, 12.68, 89.93, 1.39, 1.04, 0.11]
#
# DL_packet_size = [24, 24, 27, 28, 27, 77, 35, 34, 20, 92]
# DL_delay = [3294, 782, 747, 457, 801, 1121, 955, 1275, 557, 1063]
# DL_packetspeed_01_ser_send = [19.48, 10.03, 10.03, 10.07, 10.03, 10.00, 10.10, 19.87, 10.06, 10.05]
# rate_lost_no_non = [1.30, 0, 0, 0.34, 0, 0.68, 2.04, 3.54, 12.68, 0.11]

#lead rate
UL_packet_size = [37, 43, 260, 28, 24, 20, 24, 88, 34, 25, 25, 25, 40]
UL_delay = [1971, 1865, 2713, 1695, 1689, 1910, 1737, 2054, 1993, 2082, 1706, 1906, 1757]
UL_packet_speed_0_1 = [10.03, 10.03, 10.03, 10.03, 10.00, 10.00, 10.31, 10.0, 15.28, 29.99, 10.21, 10.01, 10.63]
rate_lost_global = [1.30, 0, 0, 0.34, 0, 0.68, 2.04, 3.54, 12.68, 89.93, 1.39, 1.04, 0.11]

DL_packet_size = [24, 24, 27, 28, 27, 77, 35, 34, 20, 92]
DL_delay = [3294, 782, 747, 457, 801, 1121, 955, 1275, 557, 1063]
DL_packetspeed_01_ser_send = [19.55, 10.07, 10.03, 10.07, 10.03, 10.03, 10.20, 10.10, 10.03, 10.03]
rate_lost_no_non = [1.30, 0, 0, 0.34, 0, 0.68, 2.04, 3.54, 12.68, 0.11]
# the relation between packet size and delay
UL_packet_size, UL_delay, UL_packet_speed_0_1 = sort(UL_packet_size, UL_delay, UL_packet_speed_0_1, rate_lost_global)
DL_packet_size, DL_delay, DL_packetspeed_01_ser_send = sort(DL_packet_size, DL_delay, DL_packetspeed_01_ser_send,
                                                            rate_lost_no_non)
axes[0][0].plot(UL_packet_size, UL_delay, color='y')
axes[0][0].scatter(UL_packet_size, UL_delay, color='y')
axes[0][0].plot(DL_packet_size, DL_delay, color='g')
axes[0][0].scatter(DL_packet_size, DL_delay, color='g')
axes[0][0].set_ylabel("delay")

# the relationship between speed and delay
UL_packet_speed_0_1, UL_packet_size, UL_delay = sort(UL_packet_speed_0_1, UL_packet_size, UL_delay, rate_lost_global)
DL_packetspeed_01_ser_send, DL_packet_size, DL_delay = sort(DL_packetspeed_01_ser_send, DL_packet_size, DL_delay,
                                                            rate_lost_no_non)
axes[0][1].plot(DL_packetspeed_01_ser_send, DL_delay, color='g', label="DL")
axes[0][1].scatter(DL_packetspeed_01_ser_send, DL_delay, color='g')
axes[0][1].plot(UL_packet_speed_0_1, UL_delay, color='y', label="UL")
axes[0][1].scatter(UL_packet_speed_0_1, UL_delay, color='y')
axes[0][1].set_xlabel("")
axes[0][1].legend(loc=1, prop={'size': 10})
# the relationship between speed and lost

axes[1][1].plot(UL_packet_speed_0_1, rate_lost_global, color='y')
axes[1][1].scatter(UL_packet_speed_0_1, rate_lost_global, color='y')
axes[1][1].plot(DL_packetspeed_01_ser_send, rate_lost_no_non, color='g')
axes[1][1].scatter(DL_packetspeed_01_ser_send, rate_lost_no_non, color='g')
axes[1][1].set_xlabel("packets/S")
# the relationship between packet size and lost

UL_packet_size, UL_delay, UL_packet_speed_0_1 = sort(UL_packet_size, UL_delay, UL_packet_speed_0_1, rate_lost_global)
DL_packet_size, DL_delay, DL_packetspeed_01_ser_send = sort(DL_packet_size, DL_delay, DL_packetspeed_01_ser_send,
                                                            rate_lost_no_non)

axes[1][0].plot(UL_packet_size, rate_lost_global, color='y')
axes[1][0].scatter(UL_packet_size, rate_lost_global, color='y')
axes[1][0].plot(DL_packet_size, rate_lost_no_non, color='g')
axes[1][0].scatter(DL_packet_size, rate_lost_no_non, color='g')
axes[1][0].set_xlabel("packet size")
axes[1][0].set_ylabel("rate of loss")
print(UL_packet_speed_0_1)
print(UL_delay)
print()
print(DL_packetspeed_01_ser_send)
print(DL_delay)
# str = "JPG/BC26_20210221-20210222/" + os.path.basename(sys.argv[0]).split(".", -1)[0] + ".jpg"
# print("JPG/BC26_20210221-20210222/packet_size-delay.jpg")
# plt.savefig(str)
plt.show()
