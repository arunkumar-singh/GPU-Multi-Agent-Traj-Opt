import numpy as np
from scipy.io import loadmat
import matplotlib.pyplot as plt
from scipy.io import loadmat
import scipy.io
import matplotlib


matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

plt.rcParams.update({'font.size': 15})



arc_mean_curr_16robot_15_temp = scipy.io.loadmat('../16_robots_square/comparison_data/r_15/arc_mean_curr_16robot_15.mat')
arc_mean_curr_16robot_15 = arc_mean_curr_16robot_15_temp['arc_mean_curr_16robot_15'].squeeze()

arc_mean_prop_16robot_15_temp = scipy.io.loadmat('../16_robots_square/comparison_data/r_15/arc_mean_prop_16robot_15.mat')
arc_mean_prop_16robot_15 = arc_mean_prop_16robot_15_temp['arc_mean_prop_16robot_15'].squeeze()

arc_mean_curr_8robot_15_temp = scipy.io.loadmat('../8_robots_square/comparison_data/arc_mean_curr_8robot_15.mat')
arc_mean_curr_8robot_15 = arc_mean_curr_8robot_15_temp['arc_mean_curr_8robot_15'].squeeze()

arc_mean_prop_8robot_15_temp = scipy.io.loadmat('../8_robots_square/comparison_data/arc_mean_prop_8robot_15.mat')
arc_mean_prop_8robot_15 = arc_mean_prop_8robot_15_temp['arc_mean_prop_8robot_15'].squeeze()


###########################smoothness############
cost_smoothness_curr_16rob_15_temp = scipy.io.loadmat('../16_robots_square/comparison_data/r_15/cost_smoothness_curr_16rob_15.mat')
cost_smoothness_curr_16rob_15 = cost_smoothness_curr_16rob_15_temp['cost_smoothness_curr_16rob_15'].squeeze()

cost_smoothness_curr_8rob_15_temp = scipy.io.loadmat('../8_robots_square/comparison_data/cost_smoothness_curr_8rob_15.mat')
cost_smoothness_curr_8rob_15 = cost_smoothness_curr_8rob_15_temp['cost_smoothness_curr_8rob_15'].squeeze()

cost_smoothness_prop_16rob_15_temp = scipy.io.loadmat('../16_robots_square/comparison_data/r_15/cost_smoothness_prop_16rob_15.mat')
cost_smoothness_prop_16rob_15 = cost_smoothness_prop_16rob_15_temp['cost_smoothness_prop_16rob_15'].squeeze()

cost_smoothness_prop_8rob_15_temp = scipy.io.loadmat('../8_robots_square/comparison_data/cost_smoothness_prop_8rob_15.mat')
cost_smoothness_prop_8rob_15 = cost_smoothness_prop_8rob_15_temp['cost_smoothness_prop_8rob_15'].squeeze()

########################################
cost_mean_curr_16rob_15 = np.mean(cost_smoothness_curr_16rob_15)
cost_mean_curr_8rob_15 = np.mean(cost_smoothness_curr_8rob_15)


cost_mean_prop_16rob_15 = np.mean(cost_smoothness_prop_16rob_15)
cost_mean_prop_8rob_15 = np.mean(cost_smoothness_prop_8rob_15)



arc_curr_16rob_15 = np.mean(arc_mean_curr_16robot_15) 
arc_prop_16rob_15 = np.mean(arc_mean_prop_16robot_15)

arc_curr_8rob_15 = np.mean(arc_mean_curr_8robot_15) 
arc_prop_8rob_15 = np.mean(arc_mean_prop_8robot_15)


cost_std_curr_16rob_15 = np.std(cost_smoothness_curr_16rob_15)
cost_std_curr_8rob_15 = np.std(cost_smoothness_curr_8rob_15)


cost_std_prop_16rob_15 = np.std(cost_smoothness_prop_16rob_15)
cost_std_prop_8rob_15 = np.std(cost_smoothness_prop_8rob_15)

arc_curr_16rob_15_std = np.std(arc_mean_curr_16robot_15)
arc_prop_16rob_15_std = np.std(arc_mean_prop_16robot_15)

arc_curr_8rob_15_std = np.std(arc_mean_curr_8robot_15)
arc_prop_8rob_15_std = np.std(arc_mean_prop_8robot_15)


######################time######################

time_16rob_prpo = 0.2682
time_16rob_curr = 158.383
time_8rob_prpo = 0.2421
time_8rob_curr = 6.94

labels = ['8 agents','16 agents']


x_pos = np.arange(len(labels))

CTEs_1 = [ np.round(arc_curr_8rob_15,3), np.round(arc_curr_16rob_15,3)]
CTEs_2 = [ np.round(arc_prop_8rob_15,3), np.round(arc_prop_16rob_15,3)]
CTEs_3 = [np.round(time_8rob_prpo,3), np.round(time_16rob_prpo,3) ]
CTEs_4 = [np.round(time_8rob_curr,3), np.round(time_16rob_curr,3)]
CTEs_5 = [np.round(cost_mean_curr_8rob_15,3), np.round(cost_mean_curr_16rob_15,3) ]
CTEs_6 = [np.round(cost_mean_prop_8rob_15,3), np.round(cost_mean_prop_16rob_15,3) ]

Error_1 =[ np.round(arc_curr_8rob_15_std,4), np.round(arc_curr_16rob_15_std,4)  ]
Error_2 =[ np.round(arc_prop_8rob_15_std,4), np.round(arc_prop_16rob_15_std,4) ]
Error_3 =[ np.round(cost_std_curr_8rob_15,4), np.round(cost_std_curr_16rob_15,4)]
Error_4 =[ np.round(cost_std_prop_8rob_15,4),  np.round(cost_std_prop_16rob_15,4)]

width =0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x_pos - width/2, CTEs_1, width,  yerr=Error_1, color = 'pink', label='[5]')
rects2 = ax.bar(x_pos + width/2, CTEs_2, width,  yerr=Error_2, color = 'lightskyblue', label='Ours')

ax.set_ylabel('[m]')
ax.set_title('Arc Length')
ax.set_xticks(x_pos)
ax.set_xticklabels(labels,fontsize=15)
ax.legend()


def autolabel(rects):

    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, -105), 
                    textcoords="offset points",
                    ha='center', va='bottom', rotation=90 )


autolabel(rects1)
autolabel(rects2)

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
                    xytext=(10, 0),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom',rotation=90 )


autolabel(rects5)
autolabel(rects6)

fig.tight_layout()

plt.show()





