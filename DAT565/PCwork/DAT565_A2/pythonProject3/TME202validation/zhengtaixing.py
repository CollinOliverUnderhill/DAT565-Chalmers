import scipy.stats as stats

back_distances = [2350, 2399, 1519, 1752, 1189, 1236, 1552, 2070, 1587, 2129,
                  1324, 1922, 2223, 1282, 1357, 1385, 2527, 1415, 2687, 2195,
                  2469, 2201, 2030]
side_distances = [2521, 2015, 1730, 1729, 2201, 1433, 2130, 1867, 2518, 2168,
                  2320, 1488, 3767, 1741, 3043, 2101, 2030, 1772, 2232, 2001,
                  2058, 2249, 2058, 1600]

no_oncoming_distances = [2350, 2399, 1519, 1752, 1189, 1552, 2070, 2129, 1922,
                         2223, 1385, 2527, 2195, 2469, 2201, 2030, 2521, 2015,
                         1730, 1729, 2201, 1433, 2130, 2168, 2320, 1488, 3767,
                         1741, 3043, 2101, 1772, 2232, 2249, 1600]
yes_oncoming_distances = [1236, 1587, 1324, 1282, 1357, 1415, 2687, 1867, 2518,
                          2030, 2001, 2058]

shapiro_back = stats.shapiro(back_distances)
shapiro_side = stats.shapiro(side_distances)

shapiro_no_oncoming = stats.shapiro(no_oncoming_distances)
shapiro_yes_oncoming = stats.shapiro(yes_oncoming_distances)

print("Shapiro-Wilk Test Results:")
print(f"Back Group: W={shapiro_back.statistic:.3f}, p={shapiro_back.pvalue:.3f}")
print(f"Side Group: W={shapiro_side.statistic:.3f}, p={shapiro_side.pvalue:.3f}")
print(f"No Oncoming Group: W={shapiro_no_oncoming.statistic:.3f}, p={shapiro_no_oncoming.pvalue:.3f}")
print(f"Yes Oncoming Group: W={shapiro_yes_oncoming.statistic:.3f}, p={shapiro_yes_oncoming.pvalue:.3f}")
