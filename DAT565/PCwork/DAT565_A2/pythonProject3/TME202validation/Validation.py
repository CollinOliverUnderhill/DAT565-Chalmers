import scipy.stats as stats
import numpy as np

back_distances = np.array([2350, 2399, 1519, 1752, 1189, 1236, 1552, 2070, 1587, 2129,
                           1324, 1922, 2223, 1282, 1357, 1385, 2527, 1415, 2687, 2195,
                           2469, 2201, 2030])
side_distances = np.array([2521, 2015, 1730, 1729, 2201, 1433, 2130, 1867, 2518, 2168,
                           2320, 1488, 3767, 1741, 3043, 2101, 2030, 1772, 2232, 2001,
                           2058, 2249, 2058, 1600])

no_oncoming_distances = np.array([2350, 2399, 1519, 1752, 1189, 1552, 2070, 2129, 1922,
                                  2223, 1385, 2527, 2195, 2469, 2201, 2030, 2521, 2015,
                                  1730, 1729, 2201, 1433, 2130, 2168, 2320, 1488, 3767,
                                  1741, 3043, 2101, 1772, 2232, 2249, 1600])
yes_oncoming_distances = np.array([1236, 1587, 1324, 1282, 1357, 1415, 2687, 1867, 2518,
                                   2030, 2001, 2058])

t_pos, p_pos = stats.ttest_ind(back_distances, side_distances, equal_var=True)

t_oncoming, p_oncoming = stats.ttest_ind(yes_oncoming_distances, no_oncoming_distances, equal_var=True)

print("Position T-test: t = {:.3f}, p = {:.3f}".format(t_pos, p_pos))
print("Oncoming T-test: t = {:.3f}, p = {:.3f}".format(t_oncoming, p_oncoming))
