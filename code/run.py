import datetime
import pandas as pd
from tqdm import tqdm
import matplotlib.pyplot as plt

data = pd.read_csv("data/RECORD.csv")

data["DATE"] = pd.to_datetime(data["DATE"])
data["mDATE"] = data["DATE"].dt.strftime("%Y-%m")
data["dDATE"] = data["DATE"].dt.day
print(data)
print(data.describe())

mth = data.groupby("mDATE").sum("VAL")
mth = [i for i in mth[mth["VAL"] > 0].index]
print(mth)


INSERT = f"Update Time {datetime.datetime.now()}\n"
for imth in tqdm(mth):
    idata = data[data["mDATE"] == imth]

    plt.figure(figsize=(9, 3))
    plt.plot(idata["dDATE"], idata["VAL"], "r-*")
    
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.title(f"{imth}")
    plt.axis([1, 31, 6.0, 12.0])
    plt.savefig(f"outs/DV_{imth}.png")

    plt.close()

    INSERT += f"\n![{imth}](outs/DV_{imth}.png)"


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



