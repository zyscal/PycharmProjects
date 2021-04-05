import os
import sys

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from datetime import datetime
import pandas as pd

fig, axes = plt.subplots(1, 2, sharey=True, figsize=(15, 5), dpi=300)

value_bc26_20201231_20210101 = []
value_UpLink_bc26_20201231_20210101 = []
value_DownLink_bc26_20201231_20210101 = []

value_bc26_20210101_20210102 = []
value_UpLink_bc26_20210101_20210102 = []
value_DownLink_bc26_20210101_20210102 = []


with open('20210118-20210119_bc26_goodcard/RTT_bc26_goodcard_20210118-20210119.txt', 'r') as f:
    value_str = f.read().split(',', -1)
for i in value_str:
    value_bc26_20201231_20210101.append(int(i))

with open('20210118-20210119_bc26_goodcard/bc26_212h_UpLink_value.txt', 'r') as f:
    value_str = f.read().split(',', -1)
for i in value_str:
    value_UpLink_bc26_20201231_20210101.append(int(i))

with open('20210118-20210119_bc26_goodcard/bc26_12h_DownLink_value.txt', 'r') as f:
    value_str = f.read().split(',', -1)
for i in value_str:
    value_DownLink_bc26_20201231_20210101.append(int(i))

with open('20210117-22_20210118-10/RTT_bc26_badcard_20210117-22_20210118-10.txt', 'r') as f:
    value_str = f.read().split(',', -1)
for i in value_str:
    value_bc26_20210101_20210102.append(int(i))

with open('20210117-22_20210118-10/bc26_24h_UpLink_value.txt', 'r') as f:
    value_str = f.read().split(',', -1)
for i in value_str:
    value_UpLink_bc26_20210101_20210102.append(int(i))

with open('20210117-22_20210118-10/bc26_24h_DownLink_value.txt', 'r') as f:
    value_str = f.read().split(',', -1)
for i in value_str:
    value_DownLink_bc26_20210101_20210102.append(int(i))







ax1 = axes[0]
sum_RTT_20201231 = 0
for i in value_bc26_20201231_20210101:
    sum_RTT_20201231 += i
print("avg() bad_card: ", sum_RTT_20201231 / len(value_bc26_20201231_20210101))

sum_UL_BAD = 0
big_UL_BAD = 0
for i in value_UpLink_bc26_20201231_20210101:
    sum_UL_BAD += i
    if i >= 10000:
        big_UL_BAD += 1
print("avg() bad_card UL : ", sum_UL_BAD / len(value_UpLink_bc26_20201231_20210101))
print("rate of big_UL_bad : ", big_UL_BAD / len(value_UpLink_bc26_20201231_20210101))
sum_DL_BAD = 0
for i in value_DownLink_bc26_20201231_20210101:
    sum_DL_BAD += i
print("avg() bad_card DL : ", sum_DL_BAD / len(value_DownLink_bc26_20201231_20210101))

value_bc26_20201231_20210101.sort()
#print(value_bc26_20201231_20210101)
#print("len of value_bc26_20201231_20210101 : ", len(value_bc26_20201231_20210101))
CDF_20201231 = []
cha_20201231_RTT = 1 / len(value_bc26_20201231_20210101)
#print("cha", cha_20201231_RTT)
for i in range(1, len(value_bc26_20201231_20210101) + 1):
    CDF_20201231.append(i * cha_20201231_RTT)
#print("len of CDF : ", len(CDF_20201231))
#print("CDF_20201231 : ", CDF_20201231)

value_UpLink_bc26_20201231_20210101.sort()
sum_20210101_UpLink_value = 0
for i in value_UpLink_bc26_20201231_20210101:
    sum_20210101_UpLink_value += i
CDF_20210101_UpLink = []
cha_20201231_UL = 1 / len(value_UpLink_bc26_20201231_20210101)
for i in range(1, len(value_UpLink_bc26_20201231_20210101) + 1):
    CDF_20210101_UpLink.append(i * cha_20201231_UL)


value_DownLink_bc26_20201231_20210101.sort()
sum_20201231_DownLink_value = 0
for i in value_DownLink_bc26_20201231_20210101:
    sum_20201231_DownLink_value += i
CDF_20201231_DownLink = []
cha_20201231_DL = 1 / len(value_DownLink_bc26_20201231_20210101)
for i in range(1, len(value_DownLink_bc26_20201231_20210101) + 1):
    CDF_20201231_DownLink.append(i * cha_20201231_DL)

value_UpLink_bc26_20201231_20210101_lg = []
value_DownLink_bc26_20201231_20210101_lg = []
value_RTT_20201231_lg = []
for i in value_bc26_20201231_20210101:
    value_RTT_20201231_lg.append(np.math.log(i, 10))
for i in value_UpLink_bc26_20201231_20210101:
    value_UpLink_bc26_20201231_20210101_lg.append(np.math.log(i, 10))
for i in value_DownLink_bc26_20201231_20210101:
    value_DownLink_bc26_20201231_20210101_lg.append(np.math.log(i, 10))

plt.locator_params('y', nbins=10)
plt.locator_params('x', nbins=10)
zhong = 0
for i in range(0, len(CDF_20201231) + 1):
    if CDF_20201231[i] >= 0.5:
        zhong = i
        break
zhong_line = []
zhong_line.append(value_RTT_20201231_lg[zhong])
ax1.vlines(zhong_line, 0, 1, color='r', linewidths=0.8)


zhong = 0
for i in range(0, len(CDF_20201231_DownLink) + 1):
    if CDF_20201231_DownLink[i] >= 0.5:
        zhong = i
        break
zhong_line = []
zhong_line.append(value_DownLink_bc26_20201231_20210101_lg[zhong])
ax1.vlines(zhong_line, 0, 1, color='r', linewidths=0.8)
ax1.plot(value_RTT_20201231_lg, CDF_20201231, color="b", label="BC26_RTT")
ax1.plot(value_UpLink_bc26_20201231_20210101_lg, CDF_20210101_UpLink, color='y', label="BC26_UpLink")
ax1.plot(value_DownLink_bc26_20201231_20210101_lg, CDF_20201231_DownLink, color='g', label="BC26_DownLink")
ax1.legend(loc=4, prop={'size': 9})

ax2 = axes[1]
sum_RTT_20210101 = 0
for i in value_bc26_20210101_20210102:
    sum_RTT_20210101 += i
print("avg() good_card: ", sum_RTT_20210101 / len(value_bc26_20210101_20210102))

sum_UL_GOOD = 0
big_UL_GOOD = 0
for i in value_UpLink_bc26_20210101_20210102:
    sum_UL_GOOD += i
    if i >= 10000:
        big_UL_GOOD += 1
print("avg() GOOD_card UL : ", sum_UL_GOOD / len(value_UpLink_bc26_20210101_20210102))
print("rate of big_UL_GOOD : ", big_UL_GOOD / len(value_UpLink_bc26_20210101_20210102))
sum_DL_GOOD = 0
for i in value_DownLink_bc26_20210101_20210102:
    sum_DL_GOOD += i
print("avg() GOOD_card DL : ", sum_DL_GOOD / len(value_DownLink_bc26_20210101_20210102))

value_bc26_20210101_20210102.sort()
#print(value_bc26_20210101_20210102)
#print("len of value_bc26_20210101_20210102 : ", len(value_bc26_20210101_20210102))
CDF_20210101 = []
cha_20210101_RTT = 1 / len(value_bc26_20210101_20210102)
#print("cha", cha_20210101_RTT)
for i in range(1, len(value_bc26_20210101_20210102) + 1):
    CDF_20210101.append(i * cha_20210101_RTT)
#print("len of CDF : ", len(CDF_20210101))
#print("CDF_20210101 : ", CDF_20210101)

value_UpLink_bc26_20210101_20210102.sort()
sum_20201231_UpLink_value = 0
for i in value_UpLink_bc26_20210101_20210102:
    sum_20201231_UpLink_value += i
CDF_20201231_UpLink = []
cha_20210101_UL = 1 / len(value_UpLink_bc26_20210101_20210102)
for i in range(1, len(value_UpLink_bc26_20210101_20210102) + 1):
    CDF_20201231_UpLink.append(i * cha_20210101_UL)
value_DownLink_bc26_20210101_20210102.sort()
sum_20210101_DownLink_value = 0
for i in value_DownLink_bc26_20210101_20210102:
    sum_20210101_DownLink_value += i
CDF_20210101_DownLink = []
cha_20210101_DL = 1 / len(value_DownLink_bc26_20210101_20210102)
for i in range(1, len(value_DownLink_bc26_20210101_20210102) + 1):
    CDF_20210101_DownLink.append(i * cha_20210101_DL)
value_UpLink_bc26_20210101_20210102_lg = []
value_DownLink_bc26_20210101_20210102_lg = []
value_RTT_20210101_lg = []
for i in value_bc26_20210101_20210102:
    value_RTT_20210101_lg.append(np.math.log(i, 10))
for i in value_UpLink_bc26_20210101_20210102:
    value_UpLink_bc26_20210101_20210102_lg.append(np.math.log(i, 10))
for i in value_DownLink_bc26_20210101_20210102:
    value_DownLink_bc26_20210101_20210102_lg.append(np.math.log(i, 10))



zhong = 0
for i in range(0, len(CDF_20210101) + 1):
    if CDF_20210101[i] >= 0.5:
        zhong = i
        break
zhong_line = []
zhong_line.append(value_RTT_20210101_lg[zhong])
ax2.vlines(zhong_line, 0, 1, color='r', linewidths=0.8)

zhong = 0
for i in range(0, len(CDF_20210101_DownLink) + 1):
    if CDF_20210101_DownLink[i] >= 0.5:
        zhong = i
        break
zhong_line = []
zhong_line.append(value_DownLink_bc26_20210101_20210102_lg[zhong])
ax2.vlines(zhong_line, 0, 1, color='r', linewidths=0.8)

plt.locator_params('y', nbins=10)
plt.locator_params('x', nbins=20)
ax2.plot(value_RTT_20210101_lg, CDF_20210101, color="b", label="BC26_RTT")
ax2.plot(value_UpLink_bc26_20210101_20210102_lg, CDF_20201231_UpLink, color='y', label="BC26_UpLink")
ax2.plot(value_DownLink_bc26_20210101_20210102_lg, CDF_20210101_DownLink, color='g', label="BC26_DownLink")
ax2.legend(loc=4, prop={'size': 9})

plt.ylim(0, 1.0)
ax1.set_title("BC26_bad_card RTT_UL_DL_CDF")
ax2.set_title("BC26_good_card RTT_UL_DL_CDF")






plt.ylim(0, 1.0)
ax1.set_xlim(2, 5)
ax2.set_xlim(2, 5)


ax1.locator_params('x', nbins=12)
ax2.locator_params('x', nbins=12)


str = "JPG/" + os.path.basename(sys.argv[0]).split(".", -1)[0] + ".jpg"
plt.savefig(str)

plt.show()





