import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Provided numbers
lkh3 = [
    451.9470921, 212.6569042, 217.4155833, 212.7115397, 217.8521507,
    601.4237062, 531.5401658, 461.7261718, 513.6566773, 559.8625136,
    635.4899149, 702.9837275, 741.6162095, 570.2697069, 701.8860468,
    991.6962666, 748.726529, 971.5816606, 796.0160077, 831.8228056,
    603.453651, 634.053326, 693.1103373
]

lk3_2phase_1 = [
    511.040441, 252.1941774, 266.069132, 243.704322, 217.8521507,
    721.1636311, 634.5086688, 506.884626, 541.1532448, 635.9007631,
    675.3899198, 748.6835378, 849.7979811, 657.4918835, 750.9872963,
    1032.37268, 835.9070647, 1140.041827, 970.1497663, 915.814095,
    647.5310577, 710.0599785, 796.5297999
]
lk3_2phase_2 = [
    511.040441, 252.1941774, 266.069132, 243.704322, 217.8521507,
    721.1636311, 634.5086688, 506.884626, 541.1532448, 635.9007631,
    675.3899198, 756.8490073, 849.7979811, 657.4918835, 750.9872963,
    1062.059155, 835.9070647, 1151.601203, 970.1497663, 915.814095,
    647.5310577, 710.0599785, 796.5297999
]
lk3_2phase_3 = [
    511.040441, 252.1941774, 266.069132, 243.704322, 217.8521507,
    721.1636311, 634.5086688, 506.884626, 541.1532448, 635.9007631,
    675.3899198, 756.8490073, 849.7979811, 657.4918835, 750.9872963,
    1032.37268, 835.9070647, 1140.041827, 970.1497663, 915.814095,
    647.5310577, 710.0599785, 796.5297999
]
lk3_2phase_4 = [
    511.040441, 252.1941774, 266.069132, 243.704322, 217.8521507,
    721.1636311, 634.5086688, 506.884626, 541.1532448, 635.9007631,
    675.3899198, 772.9648285, 833.9422845, 657.4918835, 750.9872963,
    1062.059155, 835.9070647, 1151.601203, 970.1497663, 915.814095,
    647.5310577, 710.0599785, 796.5297999
]
lk3_2phase_5 = [
    511.040441, 252.1941774, 266.069132, 243.704322, 217.8521507,
    721.1636311, 634.5086688, 506.884626, 541.1532448, 635.9007631,
    675.3899198, 756.8490073, 849.7979811, 657.4918835, 750.9872963,
    1062.059155, 835.9070647, 1140.041827, 970.1497663, 915.814095,
    647.5310577, 710.0599785, 796.5297999
]

annealer1 = [
    511.040441, 293.612489, 351.5413074, 392.4911346, 380.9204509,
    731.8841101, 643.0097523, 672.3465041, 755.9330097, 778.5385507,
    842.2764476, 796.6047068, 920.8288956, 875.9584016, 853.8579374,
    1124.332527, 968.0377786, 1237.299453, 1213.309712, 1143.07738,
    1397.487073, 1251.966782, 1850.861924
]
annealer2 = [
    511.040441, 321.7269463, 371.6665223, 431.1482898, 365.2994028,
    723.3153719, 650.1104082, 695.9767508, 843.0693181, 810.8576132,
    832.5218527, 813.2930085, 904.37612, 895.97792, 849.4785049,
    1068.082256, 978.3081163, 1217.377565, 1192.214582, 1122.066546,
    1327.959247, 1209.401737, 1810.639434
]
annealer3 = [
    511.040441, 362.8029087, 315.002246, 406.4722056, 376.4614634,
    723.9399245, 644.0728523, 681.2092134, 762.8481833, 811.1592319,
    816.0475284, 832.798059, 892.3332505, 916.1801762, 843.4079279,
    1085.669755, 978.7676515, 1195.022044, 1144.614604, 1107.937575,
    1378.46346, 1223.830811, 1818.201427
]
annealer4 = [
    515.6265405, 321.6134093, 371.5427799, 437.4628046, 353.0527978,
    736.3987464, 635.5717689, 663.2889107, 792.9732777, 808.2920145,
    793.813609, 833.1091832, 915.8945049, 894.3188027, 835.7056845,
    1113.271953, 962.4273119, 1192.555472, 1171.716725, 1149.765541,
    1329.12799, 1242.884199, 1791.330554
]
annealer5 = [
    511.040441, 362.0711209, 345.873382, 393.6555982, 346.0305372,
    721.1636311, 640.8980839, 695.1153226, 787.2788359, 872.6892265,
    810.8955849, 846.4693586, 920.9624666, 903.536872, 851.6174064,
    1129.728139, 1021.601641, 1208.606019, 1159.94527, 1179.380498,
    1420.655223, 1211.027224, 1793.713451
]

qaoa = [515.6265405, 723.3153719]

# Optimums
optimums = [450, 212, 216, 211, 216, 603, 529, 458, 510, 554, 631, 696, 741, 568, 694, 989, 744, 968, 792, 827, 593, 627, 681]

problems = [
    "p-n16-k8", "p-n19-k2", "p-n20-k2", "p-n21-k2", "p-n22-k2", "p-n22-k8", "p-n23-k8",
    "p-n40-k5", "p-n45-k5", "p-n50-k7", "p-n50-k8", "p-n50-k10", "p-n51-k10", "p-n55-k7",
    "p-n55-k10", "p-n55-k15", "p-n60-k10", "p-n60-k15", "p-n65-k10", "p-n70-k10", "p-n76-k4",
    "p-n76-k5", "p-n101-k4"
]

# Create a DataFrame
df = pd.DataFrame({'LKH-3': lkh3,
                    'LKH-3 + 2 Phase 1': lk3_2phase_1,
                    'LKH-3 + 2 Phase 2': lk3_2phase_2,
                    'LKH-3 + 2 Phase 3': lk3_2phase_3,
                    'LKH-3 + 2 Phase 4': lk3_2phase_4,
                    'LKH-3 + 2 Phase 5': lk3_2phase_5,
                    'Annealer1': annealer1,
                    'Annealer2': annealer2,
                    'Annealer3': annealer3,
                    'Annealer4': annealer4,
                    'Annealer5': annealer5,
                    'Optimums': optimums})

# Plot the data
alpha_value = 0.4
#Optimum:
plt.plot(df['Optimums'], label='Optimal Solution', linestyle='--', marker='.', color = 'black')
#LKH-3
plt.scatter(df.index, df['LKH-3'], label='LKH-3', color='red', marker = 'o')
#LKH-3 + Clustering
plt.scatter(df.index, df['LKH-3 + 2 Phase 1'], label='LKH-3 + 2 Phase Clustering', color='orange', alpha=alpha_value, marker = '<')
plt.scatter(df.index, df['LKH-3 + 2 Phase 2'], color='orange', alpha=alpha_value, marker = '<')
plt.scatter(df.index, df['LKH-3 + 2 Phase 3'], color='orange', alpha=alpha_value, marker = '<')
plt.scatter(df.index, df['LKH-3 + 2 Phase 4'], color='orange', alpha=alpha_value, marker = '<')
plt.scatter(df.index, df['LKH-3 + 2 Phase 5'], color='orange', alpha=alpha_value, marker = '<')
#Annealer:
plt.scatter(df.index, df['Annealer1'], label='Annealer + 2 Phase Clustering', color='blue', alpha=alpha_value, marker = 'v')
plt.scatter(df.index, df['Annealer2'], color='blue', alpha=alpha_value, marker = 'v')
plt.scatter(df.index, df['Annealer3'], color='blue', alpha=alpha_value, marker = 'v')
plt.scatter(df.index, df['Annealer4'], color='blue', alpha=alpha_value, marker = 'v')
plt.scatter(df.index, df['Annealer5'], color='blue', alpha=alpha_value, marker = 'v')
plt.scatter(df.index, df['Annealer5'], color='blue', alpha=alpha_value, marker = 'v')
#QAOA:
plt.scatter(0, qaoa[0], label = 'QAOA + 2 Phase Clustering', color = 'darkgreen', s=90, marker = '^', alpha=alpha_value)
plt.scatter(5, qaoa[1], color = 'darkgreen', s=90, marker = '^', alpha=alpha_value)

# Add labels and title
plt.xlabel('Problems')
plt.ylabel('Value of the Solution')
plt.title('Values of the Vehicle Routing Problem Solutions')
plt.xticks(range(len(problems)), problems, rotation = 45, fontsize = 5)

plt.subplots_adjust(bottom=0.15)

# Add legend
plt.legend()

# plt.show()
plt.savefig('Plots/values.pdf', format='pdf')
plt.close()