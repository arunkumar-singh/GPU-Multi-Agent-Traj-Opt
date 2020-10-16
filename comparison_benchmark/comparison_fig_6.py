import numpy as np
from scipy.io import loadmat
import matplotlib.pyplot as plt
from scipy.io import loadmat
import scipy.io
import matplotlib


matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

plt.rcParams.update({'font.size': 15})

arc_mean_curr_32robot_12_temp = scipy.io.loadmat('../32_robots_square/comparison_data/r_12/arc_mean_curr_32robot_12.mat')
arc_mean_curr_32robot_12 = arc_mean_curr_32robot_12_temp['arc_mean_curr_32robot_12'].squeeze()

arc_mean_prop_32robot_12_temp = scipy.io.loadmat('../32_robots_square/comparison_data/r_12/arc_mean_prop_32robot_12.mat')
arc_mean_prop_32robot_12 = arc_mean_prop_32robot_12_temp['arc_mean_prop_32robot_12'].squeeze()

arc_mean_curr_32robot_15_temp = scipy.io.loadmat('../32_robots_square/comparison_data/r_15/arc_mean_curr_32robot_15.mat')
arc_mean_curr_32robot_15 = arc_mean_curr_32robot_15_temp['arc_mean_curr_32robot_15'].squeeze()

arc_mean_prop_32robot_15_temp = scipy.io.loadmat('../32_robots_square/comparison_data/r_15/arc_mean_prop_32robot_15.mat')
arc_mean_prop_32robot_15 = arc_mean_prop_32robot_15_temp['arc_mean_prop_32robot_15'].squeeze()


arc_mean_curr_16robot_30_temp = scipy.io.loadmat('../16_robots_square/comparison_data/r_30/arc_mean_curr_16robot_30.mat')
arc_mean_curr_16robot_30 = arc_mean_curr_16robot_30_temp['arc_mean_curr_16robot_30'].squeeze()

arc_mean_prop_16robot_30_temp = scipy.io.loadmat('../16_robots_square/comparison_data/r_30/arc_mean_prop_16robot_30.mat')
arc_mean_prop_16robot_30 = arc_mean_prop_16robot_30_temp['arc_mean_prop_16robot_30'].squeeze()

arc_mean_curr_16robot_25_temp = scipy.io.loadmat('../16_robots_square/comparison_data/r_25/arc_mean_curr_16robot_25.mat')
arc_mean_curr_16robot_25 = arc_mean_curr_16robot_25_temp['arc_mean_curr_16robot_25'].squeeze()

arc_mean_prop_16robot_25_temp = scipy.io.loadmat('../16_robots_square/comparison_data/r_25/arc_mean_prop_16robot_25.mat')
arc_mean_prop_16robot_25 = arc_mean_prop_16robot_25_temp['arc_mean_prop_16robot_25'].squeeze()

arc_mean_curr_64robot_12_temp = scipy.io.loadmat('../64_robots_square/comparison_data/r_12/arc_mean_curr_64robot_12.mat')
arc_mean_curr_64robot_12 = arc_mean_curr_64robot_12_temp['arc_mean_curr_64robot_12'].squeeze()

arc_mean_prop_64robot_12_temp = scipy.io.loadmat('../64_robots_square/comparison_data/r_12/arc_mean_prop_64robot_12.mat')
arc_mean_prop_64robot_12 = arc_mean_prop_64robot_12_temp['arc_mean_prop_64robot_12'].squeeze()

arc_mean_curr_64robot_15_temp = scipy.io.loadmat('../64_robots_square/comparison_data/r_15/arc_mean_curr_64robot_15.mat')
arc_mean_curr_64robot_15 = arc_mean_curr_64robot_15_temp['arc_mean_curr_64robot_15'].squeeze()

arc_mean_prop_64robot_15_temp = scipy.io.loadmat('../64_robots_square/comparison_data/r_15/arc_mean_prop_64robot_15.mat')
arc_mean_prop_64robot_15 = arc_mean_prop_64robot_15_temp['arc_mean_prop_64robot_15'].squeeze()

###########################smoothness############
cost_smoothness_curr_16rob_30_temp = scipy.io.loadmat('../16_robots_square/comparison_data/r_30/cost_smoothness_curr_16rob_30.mat')
cost_smoothness_curr_16rob_30 = cost_smoothness_curr_16rob_30_temp['cost_smoothness_curr_16rob_30'].squeeze()

cost_smoothness_curr_16rob_25_temp = scipy.io.loadmat('../16_robots_square/comparison_data/r_25/cost_smoothness_curr_16rob_25.mat')
cost_smoothness_curr_16rob_25 = cost_smoothness_curr_16rob_25_temp['cost_smoothness_curr_16rob_25'].squeeze()

cost_smoothness_curr_32rob_12_temp = scipy.io.loadmat('../32_robots_square/comparison_data/r_12/cost_smoothness_curr_32rob_12.mat')
cost_smoothness_curr_32rob_12 = cost_smoothness_curr_32rob_12_temp['cost_smoothness_curr_32rob_12'].squeeze()

cost_smoothness_curr_32rob_15_temp = scipy.io.loadmat('../32_robots_square/comparison_data/r_15/cost_smoothness_curr_32rob_15.mat')
cost_smoothness_curr_32rob_15 = cost_smoothness_curr_32rob_15_temp['cost_smoothness_curr_32rob_15'].squeeze()

cost_smoothness_curr_64rob_15_temp = scipy.io.loadmat('../64_robots_square/comparison_data/r_15/cost_smoothness_curr_64rob_15.mat')
cost_smoothness_curr_64rob_15 = cost_smoothness_curr_64rob_15_temp['cost_smoothness_curr_64rob_15'].squeeze()

cost_smoothness_curr_64rob_12_temp = scipy.io.loadmat('../64_robots_square/comparison_data/r_12/cost_smoothness_curr_64rob_12.mat')
cost_smoothness_curr_64rob_12 = cost_smoothness_curr_64rob_12_temp['cost_smoothness_curr_64rob_12'].squeeze()

cost_smoothness_prop_16rob_30_temp = scipy.io.loadmat('../16_robots_square/comparison_data/r_30/cost_smoothness_prop_16rob_30.mat')
cost_smoothness_prop_16rob_30 = cost_smoothness_prop_16rob_30_temp['cost_smoothness_prop_16rob_30'].squeeze()

cost_smoothness_prop_16rob_25_temp = scipy.io.loadmat('../16_robots_square/comparison_data/r_25/cost_smoothness_prop_16rob_25.mat')
cost_smoothness_prop_16rob_25 = cost_smoothness_prop_16rob_25_temp['cost_smoothness_prop_16rob_25'].squeeze()

cost_smoothness_prop_32rob_12_temp = scipy.io.loadmat('../32_robots_square/comparison_data/r_12/cost_smoothness_prop_32rob_12.mat')
cost_smoothness_prop_32rob_12 = cost_smoothness_prop_32rob_12_temp['cost_smoothness_prop_32rob_12'].squeeze()

cost_smoothness_prop_32rob_15_temp = scipy.io.loadmat('../32_robots_square/comparison_data/r_15/cost_smoothness_prop_32rob_15.mat')
cost_smoothness_prop_32rob_15 = cost_smoothness_prop_32rob_15_temp['cost_smoothness_prop_32rob_15'].squeeze()

cost_smoothness_prop_64rob_15_temp = scipy.io.loadmat('../64_robots_square/comparison_data/r_15/cost_smoothness_prop_64rob_15.mat')
cost_smoothness_prop_64rob_15 = cost_smoothness_prop_64rob_15_temp['cost_smoothness_prop_64rob_15'].squeeze()

cost_smoothness_prop_64rob_12_temp = scipy.io.loadmat('../64_robots_square/comparison_data/r_12/cost_smoothness_prop_64rob_12.mat')
cost_smoothness_prop_64rob_12 = cost_smoothness_prop_64rob_12_temp['cost_smoothness_prop_64rob_12'].squeeze()



cost_mean_curr_16rob = np.mean(np.hstack((cost_smoothness_curr_16rob_30,cost_smoothness_curr_16rob_25 )))
cost_mean_curr_32rob = np.mean(np.hstack((cost_smoothness_curr_32rob_12,cost_smoothness_curr_32rob_15)))
cost_mean_curr_64rob = np.mean(np.hstack((cost_smoothness_curr_64rob_15,cost_smoothness_curr_64rob_12)))
cost_mean_prop_16rob = np.mean(np.hstack((cost_smoothness_prop_16rob_30,cost_smoothness_prop_16rob_25)))
cost_mean_prop_32rob = np.mean(np.hstack((cost_smoothness_prop_32rob_12,cost_smoothness_prop_32rob_15)))
cost_mean_prop_64rob = np.mean(np.hstack((cost_smoothness_prop_64rob_15,cost_smoothness_prop_64rob_12)))


arc_curr_32rob = np.mean(np.hstack((arc_mean_curr_32robot_12,arc_mean_curr_32robot_15) ))
arc_prop_32rob = np.mean(np.hstack((arc_mean_prop_32robot_12,arc_mean_prop_32robot_15) ))

arc_curr_16rob = np.mean(np.hstack((arc_mean_curr_16robot_30,arc_mean_curr_16robot_25) ))
arc_prop_16rob = np.mean(np.hstack((arc_mean_prop_16robot_30,arc_mean_prop_16robot_25) ))

arc_curr_64rob = np.mean(np.hstack((arc_mean_curr_64robot_12,arc_mean_curr_64robot_15) ))
arc_prop_64rob = np.mean(np.hstack((arc_mean_prop_64robot_12,arc_mean_prop_64robot_15) ))


cost_std_curr_16rob = np.std(np.hstack((cost_smoothness_curr_16rob_30,cost_smoothness_curr_16rob_25)))
cost_std_curr_32rob = np.std(np.hstack((cost_smoothness_curr_32rob_12,cost_smoothness_curr_32rob_15)))
cost_std_curr_64rob = np.std(np.hstack((cost_smoothness_curr_64rob_15,cost_smoothness_curr_64rob_12)))

cost_std_prop_16rob = np.std(np.hstack((cost_smoothness_prop_16rob_30,cost_smoothness_prop_16rob_25)))
cost_std_prop_32rob = np.std(np.hstack((cost_smoothness_prop_32rob_12,cost_smoothness_prop_32rob_15)))
cost_std_prop_64rob = np.std(np.hstack((cost_smoothness_prop_64rob_15,cost_smoothness_prop_64rob_12)))


arc_curr_32rob_std = np.std(np.hstack((arc_mean_curr_32robot_12,arc_mean_curr_32robot_15)))
arc_prop_32rob_std = np.std(np.hstack((arc_mean_prop_32robot_12,arc_mean_prop_32robot_15)))
arc_curr_16rob_std = np.std(np.hstack((arc_mean_curr_16robot_30,arc_mean_curr_16robot_25)))
arc_prop_16rob_std = np.std(np.hstack((arc_mean_prop_16robot_30,arc_mean_prop_16robot_30)))
arc_curr_64rob_std = np.std(np.hstack((arc_mean_curr_64robot_12,arc_mean_curr_64robot_15)))
arc_prop_64rob_std = np.std(np.hstack((arc_mean_prop_64robot_12,arc_mean_prop_64robot_15)))
######################time######################

time_16rob_prpo = (0.240+ 0.271)/2
time_16rob_curr = (0.750+0.775)/2
time_32rob_prpo = (0.773+0.802)/2
time_32rob_curr = (1.456+1.477)/2
time_64rob_prpo = (9.6294)/2
time_64rob_curr = (4.3900+4.2900)/2

labels = ['16agents','32agents','64agents']


x_pos = np.arange(len(labels))

CTEs_1 = [ np.round(arc_curr_16rob,3), np.round(arc_curr_32rob,3), np.round(arc_curr_64rob,3)]
CTEs_2 = [ np.round(arc_prop_16rob,3), np.round(arc_prop_32rob,3), np.round(arc_prop_64rob,3)]
CTEs_3 = [np.round(time_16rob_prpo,3), np.round(time_32rob_prpo,3), np.round(time_64rob_prpo,3) ]
CTEs_4 = [np.round(time_16rob_curr,3), np.round(time_32rob_curr,3), np.round(time_64rob_curr,3) ]
CTEs_5 = [np.round(cost_mean_curr_16rob,3), np.round(cost_mean_curr_32rob,3), np.round(cost_mean_curr_64rob,3) ]
CTEs_6 = [np.round(cost_mean_prop_16rob,3), np.round(cost_mean_prop_32rob,3), np.round(cost_mean_prop_64rob,3) ]

Error_1 =[ np.round(arc_curr_16rob_std,4), np.round(arc_curr_32rob_std,4), np.round(arc_curr_64rob_std,4)  ]
Error_2 =[ np.round(arc_prop_16rob_std,4), np.round(arc_prop_32rob_std,4), np.round(arc_prop_64rob_std,4) ]
Error_3 =[ np.round(cost_std_curr_16rob,4), np.round(cost_std_curr_32rob,4), np.round(cost_std_curr_64rob,4)]
Error_4 =[ np.round(cost_std_prop_16rob,4),  np.round(cost_std_prop_32rob,4), np.round(cost_std_prop_64rob,4)]


width =0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x_pos - width/2, CTEs_1, width,  yerr=Error_1, color = 'pink', label='[2]')
rects2 = ax.bar(x_pos + width/2, CTEs_2, width,  yerr=Error_2, color = 'lightskyblue', label='Ours')

ax.set_ylabel('[m]')
ax.set_title('Arc Length')
ax.set_xticks(x_pos)
ax.set_xticklabels(labels,fontsize=15)



def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, -105),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', rotation=90 )


autolabel(rects1)
autolabel(rects2)
plt.legend()

fig.tight_layout()


fig, ax = plt.subplots()
rects3 = ax.bar(x_pos - width/2, CTEs_4, width,  color = 'pink', label='Current')
rects4 = ax.bar(x_pos + width/2, CTEs_3, width,  color = 'lightskyblue', label='Proposed')

ax.set_ylabel('[s]')
ax.set_title('Computation Time')
ax.set_xticks(x_pos)
ax.set_xticklabels(labels,fontsize=15)



def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, -5),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom',rotation=90 )


autolabel(rects3)
autolabel(rects4)

fig.tight_layout()



fig, ax = plt.subplots()
rects5 = ax.bar(x_pos - width/2, CTEs_5, width,  yerr=Error_3,  color = 'pink', label='Current')
rects6 = ax.bar(x_pos + width/2, CTEs_6, width,  yerr=Error_4, color = 'lightskyblue', label='Proposed')

ax.set_title('Smoothness Cost')
ax.set_xticks(x_pos)
ax.set_xticklabels(labels,fontsize=15)



def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, -95),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom',rotation=90 )


autolabel(rects5)
autolabel(rects6)

fig.tight_layout()


plt.show()
