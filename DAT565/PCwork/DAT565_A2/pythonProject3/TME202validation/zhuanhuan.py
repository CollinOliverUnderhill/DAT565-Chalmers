import scipy.stats as stats
import pandas as pd
import numpy as np

data = {
    "Position": ["back"] * 23 + ["side"] * 24,
    "Distance [mm]": [
        2350, 2399, 1519, 1752, 1189, 1236, 1552, 2070, 1587, 2129, 1324, 1922, 2223,
        1282, 1357, 1385, 2527, 1415, 2687, 2195, 2469, 2201, 2030,
        2521, 2015, 1730, 1729, 2201, 1433, 2130, 1867, 2518, 2168, 2320, 1488, 3767,
        1741, 3043, 2101, 2030, 1772, 2232, 2001, 2058, 2249, 2058, 1600
    ],
    "Oncoming": ["no"] * 19 + ["yes"] * 4 + ["no"] * 19 + ["yes"] * 5
}

df = pd.DataFrame(data)

df["Log(Distance)"] = np.log(df["Distance [mm]"])

back_group = df[df["Position"] == "back"]["Log(Distance)"]
side_group = df[df["Position"] == "side"]["Log(Distance)"]

yes_group = df[df["Oncoming"] == "yes"]["Log(Distance)"]
no_group = df[df["Oncoming"] == "no"]["Log(Distance)"]

shapiro_back = stats.shapiro(back_group)
shapiro_side = stats.shapiro(side_group)
shapiro_yes = stats.shapiro(yes_group)
shapiro_no = stats.shapiro(no_group)

print("Shapiro-Wilk Test Results:")
print(f"Back Group: W={shapiro_back.statistic:.3f}, p={shapiro_back.pvalue:.3f}")
print(f"Side Group: W={shapiro_side.statistic:.3f}, p={shapiro_side.pvalue:.3f}")
print(f"Yes Group: W={shapiro_yes.statistic:.3f}, p={shapiro_yes.pvalue:.3f}")
print(f"No Group: W={shapiro_no.statistic:.3f}, p={shapiro_no.pvalue:.3f}")