import matplotlib.pyplot as plt
import matplotlib
from datetime import datetime
import pandas as pd

list = [1, 2, 3, 4, 5, 6, 7, 8]

def list_split(item, n):
    tmp_len = len(item)
    tmp_list = []
    for i in range(n - 1):
        tmp_list.append(item[i * (tmp_len // n):(i + 1) * (tmp_len // n)])
    tmp_list.append(item[(n - 1) * (tmp_len // n):])
    return tmp_list
ans_list = list_split(list, 3)
for i in ans_list:
    print(i)

fig, axes = plt.subplots(6, 1, sharey=True, figsize=(21, 18))
datetime_bc26_24h = []
value_bc26_24h = []
datetime_UpLink_bc26_24h = []
value_UpLink_bc26_24h = []
datetime_DownLink_bc26_24h = []
value_DownLink_bc26_24h = []

with open('datas/RTT_datetime_bc26_20201231-20210101.txt', 'r') as f:
    datetime_str = f.read().split('\n', -1)
for i in datetime_str:
    every = i.split(',', -1)
    tem_datetime = datetime(year=int(every[0]), month=int(every[1]), day=int(every[2]), hour=int(every[3]),
                            minute=int(every[4]), second=int(every[5]), microsecond=int(every[6]))
    datetime_bc26_24h.append(tem_datetime)

with open('datas/RTT_bc26_20201231-20210101.txt', 'r') as f:
    value_str = f.read().split(',', -1)
for i in value_str:
    value_bc26_24h.append(int(i))

with open('datas/bc26_24h_UpLink_value.txt', 'r') as f:
    value_str = f.read().split(',', -1)
for i in value_str:
    value_UpLink_bc26_24h.append(i)
with open('datas/bc26_24h_DownLink_value.txt.txt', 'r') as f:
    value_str = f.read().split(',', -1)
for i in value_str:
    value_DownLink_bc26_24h.append(i)

with open('datas/bc26_24h_UpLink_datetime.txt', 'r') as f:
    datetime_str = f.read().split('\n', -1)
for i in datetime_str:
    every = i.split(',', -1)
    tem_datetime = datetime(year=int(every[0]), month=int(every[1]), day=int(every[2]), hour=int(every[3]),
                            minute=int(every[4]), second=int(every[5]), microsecond=int(every[6]))
    datetime_UpLink_bc26_24h.append(tem_datetime)

with open('datas/bc26_24h_DownLink_datetime.txt', 'r') as f:
    datetime_str = f.read().split('\n', -1)
for i in datetime_str:
    every = i.split(',', -1)
    tem_datetime = datetime(year=int(every[0]), month=int(every[1]), day=int(every[2]), hour=int(every[3]),
                            minute=int(every[4]), second=int(every[5]), microsecond=int(every[6]))
    datetime_DownLink_bc26_24h.append(tem_datetime)

value_bc26_0h_8h = []
datetime_bc26_0h_8h = []
value_bc26_8h_16h = []
datetime_bc26_8h_16h = []
value_bc26_16h_24h = []
datetime_bc26_16h_24h = []

for i in range(0, int(len(value_bc26_24h) / 3)):
    value_bc26_0h_8h.append(value_bc26_24h[i])
for i in range(0, int(len(datetime_bc26_24h) / 3)):
    datetime_bc26_0h_8h.append(datetime_bc26_24h[i])

for i in range(int(len(value_bc26_24h) / 3), int(2 * len(value_bc26_24h) / 3)):
    value_bc26_8h_16h.append(value_bc26_24h[i])
for i in range(int(len(datetime_bc26_24h) / 3), int(2 * len(datetime_bc26_24h) / 3)):
    datetime_bc26_8h_16h.append(datetime_bc26_24h[i])

for i in range(2 * int(len(value_bc26_24h) / 3), len(value_bc26_24h)):
    value_bc26_16h_24h.append(value_bc26_24h[i])
for i in range(2 * int(len(datetime_bc26_24h) / 3), len(datetime_bc26_24h)):
    datetime_bc26_16h_24h.append(datetime_bc26_24h[i])

value_UpLink_bc26_0h_8h = []
datetime_UpLink_bc26_0h_8h = []
value_UpLink_bc26_8h_16h = []
datetime_UpLink_bc26_8h_16h = []
value_UpLink_bc26_16h_24h = []
datetime_UpLink_bc26_16h_24h = []
value_DownLink_bc26_0h_8h = []
datetime_DownLink_bc26_0h_8h = []
value_DownLink_bc26_8h_16h = []
datetime_DownLink_bc26_8h_16h = []
value_DownLink_bc26_16h_24h = []
datetime_DownLink_bc26_16h_24h = []

ax1 = axes[0]
df1 = pd.DataFrame({"dates": datetime_bc26_0h_8h, "values": value_bc26_0h_8h})
ax1.plot(df1["dates"], df1["values"], label="BC26 RTT", color="b")
ax1.set_xlim(datetime_bc26_0h_8h[0], datetime_bc26_0h_8h[len(datetime_bc26_0h_8h) - 1])

ax3 = axes[2]
df3 = pd.DataFrame({"dates": datetime_bc26_8h_16h, "values": value_bc26_8h_16h})
ax3.plot(df3["dates"], df3["values"], label="BC26 RTT", color="b")
ax3.set_xlim(datetime_bc26_8h_16h[0], datetime_bc26_8h_16h[len(datetime_bc26_8h_16h) - 1])

ax5 = axes[4]
df3 = pd.DataFrame({"dates": datetime_bc26_16h_24h, "values": value_bc26_16h_24h})
ax5.plot(df3["dates"], df3["values"], label="BC26 RTT", color="b")
ax5.set_xlim(datetime_bc26_16h_24h[0], datetime_bc26_16h_24h[len(datetime_bc26_16h_24h) - 1])

ax1.legend(loc=1, prop={'size': 15})
# ax2.legend(loc=1, prop={'size': 15})
ax3.legend(loc=1, prop={'size': 15})
# ax4.legend(loc=1, prop={'size': 15})
ax5.legend(loc=1, prop={'size': 15})
# ax6.legend(loc=1, prop={'size': 15})
plt.show()
