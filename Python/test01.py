#test01.py

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn-darkgrid')

#ここに必要な記述をしましょう

fig = plt.figure()


df = pd.read_csv('test01.csv')
#左
ax = fig.add_subplot(1, 2, 1)
ax.plot(df['Date'], df['OfficeWork'],label = "Time")
ax.set_title("新屋の直近3日間の勤務時間",fontname='IPAexGothic')

#右
bx = fig.add_subplot(1, 2, 2)
bx.plot(df['Date'], df['Study'],label = "Time")
bx.set_title("新屋の直近3日間の勉強時間",fontname='IPAexGothic')

plt.tight_layout()
plt.show()
