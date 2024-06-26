import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as ticker

# Numbers
lkh31 = [4386,
1540,
1611,
1296,
1569,
10245,
17448,
3497,
5335,
8261,
30640,
17326,
20617,
7732,
11679,
59422,
16239,
21765,
14413,
23207,
6077,
8110,
2728]
lkh32 = [5373,
2528,
3774,
2267,
2559,
10493,
19623,
4828,
7528,
9427,
32055,
17903,
22839,
9911,
13062,
61733,
17218,
22938,
16652,
25375,
7440,
10289,
3854]
lkh33 = [6562,
1545,
1620,
1294,
1573,
12419,
17490,
4489,
5357,
8269,
30697,
17383,
20657,
7760,
11709,
59524,
17232,
22953,
14439,
25462,
7100,
8131,
3860]
lkh34 = [4388,
1546,
1628,
1297,
1575,
10279,
17485,
3502,
5357,
8277,
30734,
17391,
20676,
7760,
11717,
59530,
16345,
21831,
14449,
23282,
6102,
8133,
2740]
lkh35 = [4448,
1540,
1616,
1298,
1577,
10279,
17502,
3519,
5403,
8268,
30725,
17376,
20672,
7766,
11702,
59549,
16281,
21894,
14456,
23242,
6089,
8143,
2764]

lk3_2phase_1 = [1114,
377,
390,
264,
337,
1281,
1451,
647,
875,
930,
1186,
1497,
1509,
1086,
1380,
2348,
1503,
2365,
1585,
1537,
768,
1111,
1180]
lk3_2phase_2 = [1127,
380,
376,
266,
326,
1287,
1404,
669,
836,
936,
1171,
1436,
1461,
1048,
1390,
2370,
1516,
2393,
1539,
1554,
764,
1101,
1169]
lk3_2phase_3 = [1115,
375,
379,
265,
326,
1281,
1398,
666,
831,
929,
1164,
1437,
1462,
1048,
1373,
2222,
1510,
2355,
1543,
1537,
749,
1091,
1168]
lk3_2phase_4 = [1136,
376,
380,
258,
337,
1263,
1407,
648,
821,
920,
1156,
1446,
1482,
1040,
1367,
2360,
1496,
2429,
1527,
1519,
743,
1096,
1153]
lk3_2phase_5 = [1120,
378,
403,
263,
333,
1270,
1398,
655,
828,
938,
1167,
1435,
1515,
1050,
1381,
2377,
1510,
2388,
1552,
1542,
749,
1103,
1168]

annealer1 = [9089,
28316,
30918,
38408,
44164,
11530,
13122,
51700,
69800,
61330,
42661,
34507,
35470,
79399,
45765,
29998,
51324,
35645,
63372,
74544,
480260,
313046,
1179349]
annealer2 = [9179,
248941,
31193,
38570,
41964,
11569,
12828,
50978,
69393,
260850,
275001,
34183,
231594,
76866,
261776,
42006,
50777,
35554,
283411,
73117,
472057,
306184,
1148520]
annealer3 = [9144,
27607,
31487,
38756,
43718,
11571,
12950,
50952,
71071,
61249,
42901,
34268,
34529,
79482,
46031,
30340,
50187,
35277,
63405,
72987,
478465,
304118,
1139668]
annealer4 = [9071,
27836,
30913,
39443,
44147,
11553,
12903,
50657,
69077,
62661,
41846,
34400,
34938,
77926,
45434,
30439,
50620,
35536,
63152,
73624,
478361,
308772,
1137004]
annealer5 = [9136,
28240,
31151,
39923,
44199,
11641,
12948,
51491,
68852,
61477,
42588,
34319,
35106,
79061,
45841,
30376,
50112,
36056,
63572,
73272,
469204,
307880,
1158056]

qaoa1 = [160275, 343908]
qaoa2 = [184502, 433014]
qaoa3 = [214858, 349862]
qaoa4 = [144650, 292828]
qaoa5 = [178542, 371523]

problems = [
    "p-n16-k8", "p-n19-k2", "p-n20-k2", "p-n21-k2", "p-n22-k2", "p-n22-k8", "p-n23-k8",
    "p-n40-k5", "p-n45-k5", "p-n50-k7", "p-n50-k8", "p-n50-k10", "p-n51-k10", "p-n55-k7",
    "p-n55-k10", "p-n55-k15", "p-n60-k10", "p-n60-k15", "p-n65-k10", "p-n70-k10", "p-n76-k4",
    "p-n76-k5", "p-n101-k4"
]

# Create a DataFrame
df = pd.DataFrame({'LKH-3 1': lkh31,
                    'LKH-3 2': lkh32,
                    'LKH-3 3': lkh33,
                    'LKH-3 4': lkh34,
                    'LKH-3 5': lkh35,
                    'LKH-3 + 2 Phase 1': lk3_2phase_1,
                    'LKH-3 + 2 Phase 2': lk3_2phase_2,
                    'LKH-3 + 2 Phase 3': lk3_2phase_3,
                    'LKH-3 + 2 Phase 4': lk3_2phase_4,
                    'LKH-3 + 2 Phase 5': lk3_2phase_5,
                    'Annealer1': annealer1,
                    'Annealer2': annealer2,
                    'Annealer3': annealer3,
                    'Annealer4': annealer4,
                    'Annealer5': annealer5})

# Plot the data
alpha_value = 0.4
#LKH-3
plt.scatter(df.index, df['LKH-3 1'], label='LKH-3', color='red', marker = '.')
plt.scatter(df.index, df['LKH-3 2'], color='red', marker = '.')
plt.scatter(df.index, df['LKH-3 3'], color='red', marker = '.')
plt.scatter(df.index, df['LKH-3 4'], color='red', marker = '.')
plt.scatter(df.index, df['LKH-3 5'], color='red', marker = '.')
#LKH-3 + Clustering
plt.scatter(df.index, df['LKH-3 + 2 Phase 1'], label='LKH-3 + 2 Phase Clustering', color='orange', alpha=alpha_value, marker = '.')
plt.scatter(df.index, df['LKH-3 + 2 Phase 2'], color='orange', alpha=alpha_value, marker = '.')
plt.scatter(df.index, df['LKH-3 + 2 Phase 3'], color='orange', alpha=alpha_value, marker = '.')
plt.scatter(df.index, df['LKH-3 + 2 Phase 4'], color='orange', alpha=alpha_value, marker = '.')
plt.scatter(df.index, df['LKH-3 + 2 Phase 5'], color='orange', alpha=alpha_value, marker = '.')
#Annealer:
plt.scatter(df.index, df['Annealer1'], label='Annealer + 2 Phase Clustering', color='blue', alpha=alpha_value, marker = '.')
plt.scatter(df.index, df['Annealer2'], color='blue', alpha=alpha_value, marker = '.')
plt.scatter(df.index, df['Annealer3'], color='blue', alpha=alpha_value, marker = '.')
plt.scatter(df.index, df['Annealer4'], color='blue', alpha=alpha_value, marker = '.')
plt.scatter(df.index, df['Annealer5'], color='blue', alpha=alpha_value, marker = '.')
plt.scatter(df.index, df['Annealer5'], color='blue', alpha=alpha_value, marker = '.')
#QAOA:
plt.scatter(0, qaoa1[0], label = 'QAOA + 2 Phase Clustering', color = 'darkgreen', marker = '.', alpha=alpha_value)
plt.scatter(5, qaoa1[1], color = 'darkgreen', marker = '.', alpha=alpha_value)
plt.scatter(0, qaoa2[0], color = 'darkgreen', marker = '.', alpha=alpha_value)
plt.scatter(5, qaoa2[1], color = 'darkgreen', marker = '.', alpha=alpha_value)
plt.scatter(0, qaoa3[0], color = 'darkgreen', marker = '.', alpha=alpha_value)
plt.scatter(5, qaoa3[1], color = 'darkgreen', marker = '.', alpha=alpha_value)
plt.scatter(0, qaoa4[0], color = 'darkgreen', marker = '.', alpha=alpha_value)
plt.scatter(5, qaoa4[1], color = 'darkgreen', marker = '.', alpha=alpha_value)
plt.scatter(0, qaoa5[0], color = 'darkgreen', marker = '.', alpha=alpha_value)
plt.scatter(5, qaoa5[1], color = 'darkgreen', marker = '.', alpha=alpha_value)

# Add labels and title
plt.xlabel('Problems')
plt.ylabel('Time in Seconds')
plt.yscale('log')
plt.title('Time Needed to Compute the Solution')

plt.xticks(range(len(problems)), problems, rotation = 45, fontsize = 5)

formatter = ticker.FuncFormatter(lambda x, pos: '{:.0f}'.format(x / 1000))
plt.gca().yaxis.set_major_formatter(formatter)

plt.subplots_adjust(bottom=0.15)

# Add legend
plt.legend()

# plt.show()
plt.savefig('Plots/times.pdf', format='pdf')
plt.close()