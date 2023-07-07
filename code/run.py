import datetime
import pandas as pd
from tqdm import tqdm
import matplotlib.pyplot as plt

# from numpy import polyfit, poly1d

data = pd.read_csv("data/RECORD.csv")

data["DATE"] = pd.to_datetime(data["DATE"])
data["yDATE"] = data["DATE"].dt.strftime("%Y")
data["mDATE"] = data["DATE"].dt.strftime("%Y-%m")
data["dyDATE"] = data["DATE"].dt.dayofyear
data["dmDATE"] = data["DATE"].dt.day
print(data)
print(data.describe())

myFig = plt.figure()
data.boxplot(column="VAL")
plt.savefig("outs/Box.png", bbox_inches="tight")
plt.close()

dtL = data.groupby("mDATE").sum("VAL")
dtL = set([i for i in dtL[dtL["VAL"] > 0].index])
dtL |= set([i[:4] for i in dtL])
dtL = sorted(dtL)
print(dtL)
# raise "Test"


INSERT = f"Update Time {datetime.datetime.now()}\n![Box](outs/Box.png)\nDetails\n"
for dt in tqdm(dtL):
    [xname, dtname, dtop, dlabel, dline, dcolor, dmark, dtype] = [
        "dyDATE", "yDATE", 366, False, 1, "blue", "d", "seaborn"
    ] if len(dt) == 4 else [
        "dmDATE", "mDATE", 31, True, 0, "red", "", "bmh"
    ]

    idata = data[data[dtname] == dt]
    x, y = idata[xname], idata["VAL"]

    plt.style.use(dtype)
    plt.figure(figsize=(12, 4))
    plt.plot(x, y, marker=dmark, color=dcolor, linewidth=dline)

    if dlabel:
        for _x, _y in zip(x, y):
            plt.text(_x, _y, _y, ha="center", va="bottom", fontsize=12, color=dcolor)

    plt.xlabel("Days")
    plt.ylabel("mmol/L")
    plt.title(f"{dt}")
    plt.axis([1, dtop, 7.0, 12.0])
    plt.savefig(f"outs/DV_{dt}.png", bbox_inches="tight")

    plt.close()

    INSERT += f"\n![{dt}](outs/DV_{dt}.png)"


BASE = """
# GMAHealth

@_@

<div align=center>

བཀྲ་ཤིས་བདེ་ལེགས་

[![IvanaXu/GMAHealth](https://gitee.com/IvanaXu/GMAHealth/widgets/widget_card.svg?colors=4183c4,ffffff,ffffff,e3e9ed,666666,9b9b9b)](https://gitee.com/IvanaXu/GMAHealth)

https://github.com/IvanaXu/GMAHealth

</div>
"""

with open("README.md", "w") as f:
    f.write(BASE.replace("@_@", INSERT))



