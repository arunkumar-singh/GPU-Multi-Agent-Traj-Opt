#!/usr/bin/env python

# import rospy
# from std_msgs.msg import String
# from nav_msgs.msg import Path


import numpy as np
from scipy.io import loadmat
import matplotlib.pyplot as plt
from scipy.io import loadmat
import scipy.io
from scipy import interpolate


robot_1_temp = loadmat('robot_1.mat')
robot_1 = robot_1_temp['robot_1'].squeeze()

robot_2_temp = loadmat('robot_2.mat')
robot_2 = robot_2_temp['robot_2'].squeeze()

robot_3_temp = loadmat('robot_3.mat')
robot_3 = robot_3_temp['robot_3'].squeeze()


robot_4_temp = loadmat('robot_4.mat')
robot_4 = robot_4_temp['robot_4'].squeeze()


robot_5_temp = loadmat('robot_5.mat')
robot_5 = robot_5_temp['robot_5'].squeeze()


robot_6_temp = loadmat('robot_6.mat')
robot_6 = robot_6_temp['robot_6'].squeeze()


robot_7_temp = loadmat('robot_7.mat')
robot_7 = robot_7_temp['robot_7'].squeeze()


robot_8_temp = loadmat('robot_8.mat')
robot_8 = robot_8_temp['robot_8'].squeeze()

robot_9_temp = loadmat('robot_9.mat')
robot_9 = robot_9_temp['robot_9'].squeeze()

robot_10_temp = loadmat('robot_10.mat')
robot_10 = robot_10_temp['robot_10'].squeeze()

robot_11_temp = loadmat('robot_11.mat')
robot_11 = robot_11_temp['robot_11'].squeeze()

robot_12_temp = loadmat('robot_12.mat')
robot_12 = robot_12_temp['robot_12'].squeeze()

robot_13_temp = loadmat('robot_13.mat')
robot_13 = robot_13_temp['robot_13'].squeeze()

robot_14_temp = loadmat('robot_14.mat')
robot_14 = robot_14_temp['robot_14'].squeeze()

robot_15_temp = loadmat('robot_15.mat')
robot_15 = robot_15_temp['robot_15'].squeeze()

robot_16_temp = loadmat('robot_16.mat')
robot_16 = robot_16_temp['robot_16'].squeeze()

robot_17_temp = loadmat('robot_17.mat')
robot_17 = robot_17_temp['robot_17'].squeeze()

robot_18_temp = loadmat('robot_18.mat')
robot_18 = robot_18_temp['robot_18'].squeeze()

robot_19_temp = loadmat('robot_19.mat')
robot_19 = robot_19_temp['robot_19'].squeeze()


robot_20_temp = loadmat('robot_20.mat')
robot_20 = robot_20_temp['robot_20'].squeeze()


robot_21_temp = loadmat('robot_21.mat')
robot_21 = robot_21_temp['robot_21'].squeeze()


robot_22_temp = loadmat('robot_22.mat')
robot_22 = robot_22_temp['robot_22'].squeeze()


robot_23_temp = loadmat('robot_23.mat')
robot_23 = robot_23_temp['robot_23'].squeeze()


robot_24_temp = loadmat('robot_24.mat')
robot_24 = robot_24_temp['robot_24'].squeeze()

robot_25_temp = loadmat('robot_25.mat')
robot_25 = robot_25_temp['robot_25'].squeeze()

robot_26_temp = loadmat('robot_26.mat')
robot_26 = robot_26_temp['robot_26'].squeeze()

robot_27_temp = loadmat('robot_27.mat')
robot_27 = robot_27_temp['robot_27'].squeeze()

robot_28_temp = loadmat('robot_28.mat')
robot_28 = robot_28_temp['robot_28'].squeeze()

robot_29_temp = loadmat('robot_29.mat')
robot_29 = robot_29_temp['robot_29'].squeeze()

robot_30_temp = loadmat('robot_30.mat')
robot_30 = robot_30_temp['robot_30'].squeeze()

robot_31_temp = loadmat('robot_31.mat')
robot_31 = robot_31_temp['robot_31'].squeeze()

robot_32_temp = loadmat('robot_32.mat')
robot_32 = robot_32_temp['robot_32'].squeeze()



############################## Loadng the trajectories from the proposed code



x_temp = scipy.io.loadmat('x_1.mat')
x = x_temp['x_1'].squeeze()

y_temp = scipy.io.loadmat('y_1.mat')
y = y_temp['y_1'].squeeze()

z_temp = scipy.io.loadmat('z_1.mat')
z = z_temp['z_1'].squeeze()



#################################smoothness comparison############
t_fin =  10.0
num_horizon = 100
tot_time = np.linspace(0.0, t_fin, num_horizon)
new_num_horizon = 681
tot_time_interp = np.linspace(0.0, t_fin, new_num_horizon)


f_x = interpolate.interp1d(tot_time, x)
f_y = interpolate.interp1d(tot_time, y)
f_z = interpolate.interp1d(tot_time, z)

x_smoothness = f_x(tot_time_interp)
y_smoothness = f_y(tot_time_interp)
z_smoothness = f_z(tot_time_interp)

#print(np.shape(x_smoothness))

#x_robot = np.vstack((robot_1[0], robot_2[0], robot_3[0], robot_4[0], robot_5[0], robot_6[0], robot_7[0], robot_8[0], robot_9[0], robot_10[0], robot_11[0], robot_12[0], robot_13[0], robot_14[0], robot_15[0], robot_16[0], robot_17[0], robot_18[0], robot_19[0], robot_20[0], robot_21[0], robot_22[0], robot_23[0], robot_24[0], robot_25[0], robot_26[0], robot_27[0], robot_28[0], robot_29[0], robot_30[0], robot_31[0], robot_32[0]))
#y_robot = np.vstack((robot_1[1], robot_2[1], robot_3[1], robot_4[1], robot_5[1], robot_6[1], robot_7[1], robot_8[1], robot_9[1], robot_10[1], robot_11[1], robot_12[1], robot_13[1], robot_14[1], robot_15[1], robot_16[1], robot_17[1], robot_18[1], robot_19[1], robot_20[1], robot_21[1], robot_22[1], robot_23[1], robot_24[1], robot_25[1], robot_26[1], robot_27[1], robot_28[1], robot_29[1], robot_30[1], robot_31[1], robot_32[1]))
#z_robot = np.vstack((robot_1[2], robot_2[2], robot_3[2], robot_4[2], robot_5[2], robot_6[2], robot_7[2], robot_8[2], robot_9[2], robot_10[2], robot_11[2], robot_12[2], robot_13[2], robot_14[2], robot_15[2], robot_16[2], robot_17[2], robot_18[2], robot_19[2], robot_20[2], robot_21[2], robot_22[2], robot_23[2], robot_24[2], robot_25[2], robot_26[2], robot_27[2], robot_28[2], robot_29[2], robot_30[2], robot_31[2], robot_32[2]))

cost_smoothness_prop_1 = np.linalg.norm(np.diff(np.diff(x_smoothness[0])))+np.linalg.norm(np.diff(np.diff(y_smoothness[0])))+np.linalg.norm(np.diff(np.diff(z_smoothness[0])))
cost_smoothness_curr_1 = np.linalg.norm(np.diff(np.diff(robot_1[0])))+np.linalg.norm(np.diff(np.diff(robot_1[1])))+np.linalg.norm(np.diff(np.diff(robot_1[2])))

cost_smoothness_prop_2 = np.linalg.norm(np.diff(np.diff(x_smoothness[1])))+np.linalg.norm(np.diff(np.diff(y_smoothness[1])))+np.linalg.norm(np.diff(np.diff(z_smoothness[1])))
cost_smoothness_curr_2 = np.linalg.norm(np.diff(np.diff(robot_2[0])))+np.linalg.norm(np.diff(np.diff(robot_2[1])))+np.linalg.norm(np.diff(np.diff(robot_2[2])))

cost_smoothness_prop_3 = np.linalg.norm(np.diff(np.diff(x_smoothness[2])))+np.linalg.norm(np.diff(np.diff(y_smoothness[2])))+np.linalg.norm(np.diff(np.diff(z_smoothness[2])))
cost_smoothness_curr_3 = np.linalg.norm(np.diff(np.diff(robot_3[0])))+np.linalg.norm(np.diff(np.diff(robot_3[1])))+np.linalg.norm(np.diff(np.diff(robot_3[2])))

cost_smoothness_prop_4 = np.linalg.norm(np.diff(np.diff(x_smoothness[3])))+np.linalg.norm(np.diff(np.diff(y_smoothness[3])))+np.linalg.norm(np.diff(np.diff(z_smoothness[3])))
cost_smoothness_curr_4 = np.linalg.norm(np.diff(np.diff(robot_4[0])))+np.linalg.norm(np.diff(np.diff(robot_4[1])))+np.linalg.norm(np.diff(np.diff(robot_4[2])))

cost_smoothness_prop_5 = np.linalg.norm(np.diff(np.diff(x_smoothness[4])))+np.linalg.norm(np.diff(np.diff(y_smoothness[4])))+np.linalg.norm(np.diff(np.diff(z_smoothness[4])))
cost_smoothness_curr_5 = np.linalg.norm(np.diff(np.diff(robot_5[0])))+np.linalg.norm(np.diff(np.diff(robot_5[1])))+np.linalg.norm(np.diff(np.diff(robot_5[2])))

cost_smoothness_prop_6 = np.linalg.norm(np.diff(np.diff(x_smoothness[5])))+np.linalg.norm(np.diff(np.diff(y_smoothness[5])))+np.linalg.norm(np.diff(np.diff(z_smoothness[5])))
cost_smoothness_curr_6 = np.linalg.norm(np.diff(np.diff(robot_6[0])))+np.linalg.norm(np.diff(np.diff(robot_6[1])))+np.linalg.norm(np.diff(np.diff(robot_6[2])))

cost_smoothness_prop_7 = np.linalg.norm(np.diff(np.diff(x_smoothness[6])))+np.linalg.norm(np.diff(np.diff(y_smoothness[6])))+np.linalg.norm(np.diff(np.diff(z_smoothness[6])))
cost_smoothness_curr_7 = np.linalg.norm(np.diff(np.diff(robot_7[0])))+np.linalg.norm(np.diff(np.diff(robot_7[1])))+np.linalg.norm(np.diff(np.diff(robot_7[2])))

cost_smoothness_prop_8 = np.linalg.norm(np.diff(np.diff(x_smoothness[7])))+np.linalg.norm(np.diff(np.diff(y_smoothness[7])))+np.linalg.norm(np.diff(np.diff(z_smoothness[7])))
cost_smoothness_curr_8 = np.linalg.norm(np.diff(np.diff(robot_8[0])))+np.linalg.norm(np.diff(np.diff(robot_8[1])))+np.linalg.norm(np.diff(np.diff(robot_8[2])))

cost_smoothness_prop_9 = np.linalg.norm(np.diff(np.diff(x_smoothness[8])))+np.linalg.norm(np.diff(np.diff(y_smoothness[8])))+np.linalg.norm(np.diff(np.diff(z_smoothness[8])))
cost_smoothness_curr_9 = np.linalg.norm(np.diff(np.diff(robot_9[0])))+np.linalg.norm(np.diff(np.diff(robot_9[1])))+np.linalg.norm(np.diff(np.diff(robot_9[2])))

cost_smoothness_prop_10= np.linalg.norm(np.diff(np.diff(x_smoothness[9])))+np.linalg.norm(np.diff(np.diff(y_smoothness[9])))+np.linalg.norm(np.diff(np.diff(z_smoothness[9])))
cost_smoothness_curr_10 = np.linalg.norm(np.diff(np.diff(robot_10[0])))+np.linalg.norm(np.diff(np.diff(robot_10[1])))+np.linalg.norm(np.diff(np.diff(robot_10[2])))

cost_smoothness_prop_11 = np.linalg.norm(np.diff(np.diff(x_smoothness[10])))+np.linalg.norm(np.diff(np.diff(y_smoothness[10])))+np.linalg.norm(np.diff(np.diff(z_smoothness[10])))
cost_smoothness_curr_11 = np.linalg.norm(np.diff(np.diff(robot_11[0])))+np.linalg.norm(np.diff(np.diff(robot_11[1])))+np.linalg.norm(np.diff(np.diff(robot_11[2])))

cost_smoothness_prop_12 = np.linalg.norm(np.diff(np.diff(x_smoothness[11])))+np.linalg.norm(np.diff(np.diff(y_smoothness[11])))+np.linalg.norm(np.diff(np.diff(z_smoothness[11])))
cost_smoothness_curr_12 = np.linalg.norm(np.diff(np.diff(robot_12[0])))+np.linalg.norm(np.diff(np.diff(robot_12[1])))+np.linalg.norm(np.diff(np.diff(robot_12[2])))

cost_smoothness_prop_13 = np.linalg.norm(np.diff(np.diff(x_smoothness[12])))+np.linalg.norm(np.diff(np.diff(y_smoothness[12])))+np.linalg.norm(np.diff(np.diff(z_smoothness[12])))
cost_smoothness_curr_13 = np.linalg.norm(np.diff(np.diff(robot_13[0])))+np.linalg.norm(np.diff(np.diff(robot_13[1])))+np.linalg.norm(np.diff(np.diff(robot_13[2])))

cost_smoothness_prop_14 = np.linalg.norm(np.diff(np.diff(x_smoothness[13])))+np.linalg.norm(np.diff(np.diff(y_smoothness[13])))+np.linalg.norm(np.diff(np.diff(z_smoothness[13])))
cost_smoothness_curr_14 = np.linalg.norm(np.diff(np.diff(robot_14[0])))+np.linalg.norm(np.diff(np.diff(robot_14[1])))+np.linalg.norm(np.diff(np.diff(robot_14[2])))

cost_smoothness_prop_15 = np.linalg.norm(np.diff(np.diff(x_smoothness[14])))+np.linalg.norm(np.diff(np.diff(y_smoothness[14])))+np.linalg.norm(np.diff(np.diff(z_smoothness[14])))
cost_smoothness_curr_15 = np.linalg.norm(np.diff(np.diff(robot_15[0])))+np.linalg.norm(np.diff(np.diff(robot_15[1])))+np.linalg.norm(np.diff(np.diff(robot_15[2])))

cost_smoothness_prop_16 = np.linalg.norm(np.diff(np.diff(x_smoothness[15])))+np.linalg.norm(np.diff(np.diff(y_smoothness[15])))+np.linalg.norm(np.diff(np.diff(z_smoothness[15])))
cost_smoothness_curr_16 = np.linalg.norm(np.diff(np.diff(robot_16[0])))+np.linalg.norm(np.diff(np.diff(robot_16[1])))+np.linalg.norm(np.diff(np.diff(robot_16[2])))

cost_smoothness_prop_17 = np.linalg.norm(np.diff(np.diff(x_smoothness[16])))+np.linalg.norm(np.diff(np.diff(y_smoothness[16])))+np.linalg.norm(np.diff(np.diff(z_smoothness[16])))
cost_smoothness_curr_17 = np.linalg.norm(np.diff(np.diff(robot_17[0])))+np.linalg.norm(np.diff(np.diff(robot_17[1])))+np.linalg.norm(np.diff(np.diff(robot_17[2])))

cost_smoothness_prop_18 = np.linalg.norm(np.diff(np.diff(x_smoothness[17])))+np.linalg.norm(np.diff(np.diff(y_smoothness[17])))+np.linalg.norm(np.diff(np.diff(z_smoothness[17])))
cost_smoothness_curr_18 = np.linalg.norm(np.diff(np.diff(robot_18[0])))+np.linalg.norm(np.diff(np.diff(robot_18[1])))+np.linalg.norm(np.diff(np.diff(robot_18[2])))

cost_smoothness_prop_19 = np.linalg.norm(np.diff(np.diff(x_smoothness[18])))+np.linalg.norm(np.diff(np.diff(y_smoothness[18])))+np.linalg.norm(np.diff(np.diff(z_smoothness[18])))
cost_smoothness_curr_19 = np.linalg.norm(np.diff(np.diff(robot_19[0])))+np.linalg.norm(np.diff(np.diff(robot_19[1])))+np.linalg.norm(np.diff(np.diff(robot_19[2])))

cost_smoothness_prop_20 = np.linalg.norm(np.diff(np.diff(x_smoothness[19])))+np.linalg.norm(np.diff(np.diff(y_smoothness[19])))+np.linalg.norm(np.diff(np.diff(z_smoothness[19])))
cost_smoothness_curr_20 = np.linalg.norm(np.diff(np.diff(robot_20[0])))+np.linalg.norm(np.diff(np.diff(robot_20[1])))+np.linalg.norm(np.diff(np.diff(robot_20[2])))

cost_smoothness_prop_21 = np.linalg.norm(np.diff(np.diff(x_smoothness[20])))+np.linalg.norm(np.diff(np.diff(y_smoothness[20])))+np.linalg.norm(np.diff(np.diff(z_smoothness[20])))
cost_smoothness_curr_21 = np.linalg.norm(np.diff(np.diff(robot_21[0])))+np.linalg.norm(np.diff(np.diff(robot_21[1])))+np.linalg.norm(np.diff(np.diff(robot_21[2])))

cost_smoothness_prop_22 = np.linalg.norm(np.diff(np.diff(x_smoothness[21])))+np.linalg.norm(np.diff(np.diff(y_smoothness[21])))+np.linalg.norm(np.diff(np.diff(z_smoothness[21])))
cost_smoothness_curr_22 = np.linalg.norm(np.diff(np.diff(robot_22[0])))+np.linalg.norm(np.diff(np.diff(robot_22[1])))+np.linalg.norm(np.diff(np.diff(robot_22[2])))

cost_smoothness_prop_23 = np.linalg.norm(np.diff(np.diff(x_smoothness[22])))+np.linalg.norm(np.diff(np.diff(y_smoothness[22])))+np.linalg.norm(np.diff(np.diff(z_smoothness[22])))
cost_smoothness_curr_23 = np.linalg.norm(np.diff(np.diff(robot_23[0])))+np.linalg.norm(np.diff(np.diff(robot_23[1])))+np.linalg.norm(np.diff(np.diff(robot_23[2])))

cost_smoothness_prop_24 = np.linalg.norm(np.diff(np.diff(x_smoothness[23])))+np.linalg.norm(np.diff(np.diff(y_smoothness[23])))+np.linalg.norm(np.diff(np.diff(z_smoothness[23])))
cost_smoothness_curr_24 = np.linalg.norm(np.diff(np.diff(robot_24[0])))+np.linalg.norm(np.diff(np.diff(robot_24[1])))+np.linalg.norm(np.diff(np.diff(robot_24[2])))

cost_smoothness_prop_25 = np.linalg.norm(np.diff(np.diff(x_smoothness[24])))+np.linalg.norm(np.diff(np.diff(y_smoothness[24])))+np.linalg.norm(np.diff(np.diff(z_smoothness[24])))
cost_smoothness_curr_25 = np.linalg.norm(np.diff(np.diff(robot_25[0])))+np.linalg.norm(np.diff(np.diff(robot_25[1])))+np.linalg.norm(np.diff(np.diff(robot_25[2])))

cost_smoothness_prop_26 = np.linalg.norm(np.diff(np.diff(x_smoothness[25])))+np.linalg.norm(np.diff(np.diff(y_smoothness[25])))+np.linalg.norm(np.diff(np.diff(z_smoothness[25])))
cost_smoothness_curr_26 = np.linalg.norm(np.diff(np.diff(robot_26[0])))+np.linalg.norm(np.diff(np.diff(robot_26[1])))+np.linalg.norm(np.diff(np.diff(robot_26[2])))

cost_smoothness_prop_27 = np.linalg.norm(np.diff(np.diff(x_smoothness[26])))+np.linalg.norm(np.diff(np.diff(y_smoothness[26])))+np.linalg.norm(np.diff(np.diff(z_smoothness[26])))
cost_smoothness_curr_27 = np.linalg.norm(np.diff(np.diff(robot_27[0])))+np.linalg.norm(np.diff(np.diff(robot_27[1])))+np.linalg.norm(np.diff(np.diff(robot_27[2])))

cost_smoothness_prop_28 = np.linalg.norm(np.diff(np.diff(x_smoothness[27])))+np.linalg.norm(np.diff(np.diff(y_smoothness[27])))+np.linalg.norm(np.diff(np.diff(z_smoothness[27])))
cost_smoothness_curr_28 = np.linalg.norm(np.diff(np.diff(robot_28[0])))+np.linalg.norm(np.diff(np.diff(robot_28[1])))+np.linalg.norm(np.diff(np.diff(robot_28[2])))

cost_smoothness_prop_29 = np.linalg.norm(np.diff(np.diff(x_smoothness[28])))+np.linalg.norm(np.diff(np.diff(y_smoothness[28])))+np.linalg.norm(np.diff(np.diff(z_smoothness[28])))
cost_smoothness_curr_29 = np.linalg.norm(np.diff(np.diff(robot_29[0])))+np.linalg.norm(np.diff(np.diff(robot_29[1])))+np.linalg.norm(np.diff(np.diff(robot_29[2])))

cost_smoothness_prop_30 = np.linalg.norm(np.diff(np.diff(x_smoothness[29])))+np.linalg.norm(np.diff(np.diff(y_smoothness[29])))+np.linalg.norm(np.diff(np.diff(z_smoothness[29])))
cost_smoothness_curr_30 = np.linalg.norm(np.diff(np.diff(robot_30[0])))+np.linalg.norm(np.diff(np.diff(robot_30[1])))+np.linalg.norm(np.diff(np.diff(robot_30[2])))

cost_smoothness_prop_31 = np.linalg.norm(np.diff(np.diff(x_smoothness[30])))+np.linalg.norm(np.diff(np.diff(y_smoothness[30])))+np.linalg.norm(np.diff(np.diff(z_smoothness[30])))
cost_smoothness_curr_31 = np.linalg.norm(np.diff(np.diff(robot_31[0])))+np.linalg.norm(np.diff(np.diff(robot_31[1])))+np.linalg.norm(np.diff(np.diff(robot_31[2])))

cost_smoothness_prop_32 = np.linalg.norm(np.diff(np.diff(x_smoothness[31])))+np.linalg.norm(np.diff(np.diff(y_smoothness[31])))+np.linalg.norm(np.diff(np.diff(z_smoothness[31])))
cost_smoothness_curr_32 = np.linalg.norm(np.diff(np.diff(robot_32[0])))+np.linalg.norm(np.diff(np.diff(robot_32[1])))+np.linalg.norm(np.diff(np.diff(robot_32[2])))

#cost_smoothness_prop_16rob_30 = np.linalg.norm(np.diff(np.diff(x_smoothness)))+np.linalg.norm(np.diff(np.diff(y_smoothness)))+np.linalg.norm(np.diff(np.diff(z_smoothness)))
#cost_smoothness_curr_16rob_30 = np.linalg.norm(np.diff(np.diff(x_robot)))+np.linalg.norm(np.diff(np.diff(y_robot)))+np.linalg.norm(np.diff(np.diff(z_robot)))

cost_smoothness_prop_32rob_15 = np.hstack((cost_smoothness_prop_1, cost_smoothness_prop_2, cost_smoothness_prop_3, cost_smoothness_prop_4, cost_smoothness_prop_5, cost_smoothness_prop_6, cost_smoothness_prop_7, cost_smoothness_prop_8, cost_smoothness_prop_9, cost_smoothness_prop_10, cost_smoothness_prop_11, cost_smoothness_prop_12,cost_smoothness_prop_13, cost_smoothness_prop_14, cost_smoothness_prop_15, cost_smoothness_prop_16, cost_smoothness_prop_17, cost_smoothness_prop_18, cost_smoothness_prop_19, cost_smoothness_prop_20, cost_smoothness_prop_21, cost_smoothness_prop_22, cost_smoothness_prop_23, cost_smoothness_prop_24, cost_smoothness_prop_25, cost_smoothness_prop_26, cost_smoothness_prop_27, cost_smoothness_prop_28, cost_smoothness_prop_29, cost_smoothness_prop_30, cost_smoothness_prop_31, cost_smoothness_prop_32))
cost_smoothness_curr_32rob_15 = np.hstack((cost_smoothness_curr_1, cost_smoothness_curr_2, cost_smoothness_curr_3, cost_smoothness_curr_4, cost_smoothness_curr_5, cost_smoothness_curr_6, cost_smoothness_curr_7, cost_smoothness_curr_8, cost_smoothness_curr_9, cost_smoothness_curr_10, cost_smoothness_curr_11, cost_smoothness_curr_12, cost_smoothness_curr_13, cost_smoothness_curr_14, cost_smoothness_curr_15, cost_smoothness_curr_16, cost_smoothness_curr_17, cost_smoothness_curr_18, cost_smoothness_curr_19, cost_smoothness_curr_20, cost_smoothness_curr_21, cost_smoothness_curr_22, cost_smoothness_curr_23, cost_smoothness_curr_24, cost_smoothness_curr_25, cost_smoothness_curr_26, cost_smoothness_curr_27, cost_smoothness_curr_28, cost_smoothness_curr_29, cost_smoothness_curr_30, cost_smoothness_curr_31, cost_smoothness_curr_32))


#print(np.shape(x_robot))
#cost_smoothness_prop_32rob_15 = np.linalg.norm(np.diff(np.diff(x_smoothness)))+np.linalg.norm(np.diff(np.diff(y_smoothness)))+np.linalg.norm(np.diff(np.diff(z_smoothness)))
#cost_smoothness_curr_32rob_15 = np.linalg.norm(np.diff(np.diff(x_robot)))+np.linalg.norm(np.diff(np.diff(y_robot)))+np.linalg.norm(np.diff(np.diff(z_robot)))

scipy.io.savemat('cost_smoothness_prop_32rob_15.mat', {'cost_smoothness_prop_32rob_15': cost_smoothness_prop_32rob_15})
scipy.io.savemat('cost_smoothness_curr_32rob_15.mat', {'cost_smoothness_curr_32rob_15': cost_smoothness_curr_32rob_15})

print(cost_smoothness_prop_32rob_15)
print(cost_smoothness_curr_32rob_15)
#################################################


arc_1_current = np.sum(np.sqrt(np.diff(robot_1[0])**2+np.diff(robot_1[1])**2+np.diff(robot_1[2])**2))
arc_1_proposed = np.sum(np.sqrt(np.diff(x_smoothness[0])**2+np.diff(y_smoothness[0])**2+np.diff(z_smoothness[0])**2))

arc_2_current = np.sum(np.sqrt(np.diff(robot_2[0])**2+np.diff(robot_2[1])**2+np.diff(robot_2[2])**2))
arc_2_proposed = np.sum(np.sqrt(np.diff(x_smoothness[1])**2+np.diff(y_smoothness[1])**2+np.diff(z_smoothness[1])**2))


arc_3_current = np.sum(np.sqrt(np.diff(robot_3[0])**2+np.diff(robot_3[1])**2+np.diff(robot_3[2])**2))
arc_3_proposed = np.sum(np.sqrt(np.diff(x_smoothness[2])**2+np.diff(y_smoothness[2])**2+np.diff(z_smoothness[2])**2))


arc_4_current = np.sum(np.sqrt(np.diff(robot_4[0])**2+np.diff(robot_4[1])**2+np.diff(robot_4[2])**2))
arc_4_proposed = np.sum(np.sqrt(np.diff(x_smoothness[3])**2+np.diff(y_smoothness[3])**2+np.diff(z_smoothness[3])**2))


arc_5_current = np.sum(np.sqrt(np.diff(robot_5[0])**2+np.diff(robot_5[1])**2+np.diff(robot_5[2])**2))
arc_5_proposed = np.sum(np.sqrt(np.diff(x_smoothness[4])**2+np.diff(y_smoothness[4])**2+np.diff(z_smoothness[4])**2))

arc_6_current = np.sum(np.sqrt(np.diff(robot_6[0])**2+np.diff(robot_6[1])**2+np.diff(robot_6[2])**2))
arc_6_proposed = np.sum(np.sqrt(np.diff(x_smoothness[5])**2+np.diff(y_smoothness[5])**2+np.diff(z_smoothness[5])**2))

arc_7_current = np.sum(np.sqrt(np.diff(robot_7[0])**2+np.diff(robot_7[1])**2+np.diff(robot_7[2])**2))
arc_7_proposed = np.sum(np.sqrt(np.diff(x_smoothness[6])**2+np.diff(y_smoothness[6])**2+np.diff(z_smoothness[6])**2))

arc_8_current = np.sum(np.sqrt(np.diff(robot_8[0])**2+np.diff(robot_8[1])**2+np.diff(robot_8[2])**2))
arc_8_proposed = np.sum(np.sqrt(np.diff(x_smoothness[7])**2+np.diff(y_smoothness[7])**2+np.diff(z_smoothness[7])**2))

arc_9_current = np.sum(np.sqrt(np.diff(robot_9[0])**2+np.diff(robot_9[1])**2+np.diff(robot_9[2])**2))
arc_9_proposed = np.sum(np.sqrt(np.diff(x_smoothness[8])**2+np.diff(y_smoothness[8])**2+np.diff(z_smoothness[8])**2))

arc_10_current = np.sum(np.sqrt(np.diff(robot_10[0])**2+np.diff(robot_10[1])**2+np.diff(robot_10[2])**2))
arc_10_proposed = np.sum(np.sqrt(np.diff(x_smoothness[9])**2+np.diff(y_smoothness[9])**2+np.diff(z_smoothness[9])**2))

arc_11_current = np.sum(np.sqrt(np.diff(robot_11[0])**2+np.diff(robot_11[1])**2+np.diff(robot_11[2])**2))
arc_11_proposed = np.sum(np.sqrt(np.diff(x_smoothness[10])**2+np.diff(y_smoothness[10])**2+np.diff(z_smoothness[10])**2))

arc_12_current = np.sum(np.sqrt(np.diff(robot_12[0])**2+np.diff(robot_12[1])**2+np.diff(robot_12[2])**2))
arc_12_proposed = np.sum(np.sqrt(np.diff(x_smoothness[11])**2+np.diff(y_smoothness[11])**2+np.diff(z_smoothness[11])**2))

arc_13_current = np.sum(np.sqrt(np.diff(robot_13[0])**2+np.diff(robot_13[1])**2+np.diff(robot_13[2])**2))
arc_13_proposed = np.sum(np.sqrt(np.diff(x_smoothness[12])**2+np.diff(y_smoothness[12])**2+np.diff(z_smoothness[12])**2))

arc_14_current = np.sum(np.sqrt(np.diff(robot_14[0])**2+np.diff(robot_14[1])**2+np.diff(robot_14[2])**2))
arc_14_proposed = np.sum(np.sqrt(np.diff(x_smoothness[13])**2+np.diff(y_smoothness[13])**2+np.diff(z_smoothness[13])**2))

arc_15_current = np.sum(np.sqrt(np.diff(robot_15[0])**2+np.diff(robot_15[1])**2+np.diff(robot_15[2])**2))
arc_15_proposed = np.sum(np.sqrt(np.diff(x_smoothness[14])**2+np.diff(y_smoothness[14])**2+np.diff(z_smoothness[14])**2))

arc_16_current = np.sum(np.sqrt(np.diff(robot_16[0])**2+np.diff(robot_16[1])**2+np.diff(robot_16[2])**2))
arc_16_proposed = np.sum(np.sqrt(np.diff(x_smoothness[15])**2+np.diff(y_smoothness[15])**2+np.diff(z_smoothness[15])**2))

arc_17_current = np.sum(np.sqrt(np.diff(robot_17[0])**2+np.diff(robot_17[1])**2+np.diff(robot_17[2])**2))
arc_17_proposed = np.sum(np.sqrt(np.diff(x_smoothness[16])**2+np.diff(y_smoothness[16])**2+np.diff(z_smoothness[16])**2))

arc_18_current = np.sum(np.sqrt(np.diff(robot_18[0])**2+np.diff(robot_18[1])**2+np.diff(robot_18[2])**2))
arc_18_proposed = np.sum(np.sqrt(np.diff(x_smoothness[17])**2+np.diff(y_smoothness[17])**2+np.diff(z_smoothness[17])**2))

arc_19_current = np.sum(np.sqrt(np.diff(robot_19[0])**2+np.diff(robot_19[1])**2+np.diff(robot_19[2])**2))
arc_19_proposed = np.sum(np.sqrt(np.diff(x_smoothness[18])**2+np.diff(y_smoothness[18])**2+np.diff(z_smoothness[18])**2))

arc_20_current = np.sum(np.sqrt(np.diff(robot_20[0])**2+np.diff(robot_20[1])**2+np.diff(robot_20[2])**2))
arc_20_proposed = np.sum(np.sqrt(np.diff(x_smoothness[19])**2+np.diff(y_smoothness[19])**2+np.diff(z_smoothness[19])**2))

arc_21_current = np.sum(np.sqrt(np.diff(robot_21[0])**2+np.diff(robot_21[1])**2+np.diff(robot_21[2])**2))
arc_21_proposed = np.sum(np.sqrt(np.diff(x_smoothness[20])**2+np.diff(y_smoothness[20])**2+np.diff(z_smoothness[20])**2))

arc_22_current = np.sum(np.sqrt(np.diff(robot_22[0])**2+np.diff(robot_22[1])**2+np.diff(robot_22[2])**2))
arc_22_proposed = np.sum(np.sqrt(np.diff(x_smoothness[21])**2+np.diff(y_smoothness[21])**2+np.diff(z_smoothness[21])**2))

arc_23_current = np.sum(np.sqrt(np.diff(robot_23[0])**2+np.diff(robot_23[1])**2+np.diff(robot_23[2])**2))
arc_23_proposed = np.sum(np.sqrt(np.diff(x_smoothness[22])**2+np.diff(y_smoothness[22])**2+np.diff(z_smoothness[22])**2))

arc_24_current = np.sum(np.sqrt(np.diff(robot_24[0])**2+np.diff(robot_24[1])**2+np.diff(robot_24[2])**2))
arc_24_proposed = np.sum(np.sqrt(np.diff(x_smoothness[23])**2+np.diff(y_smoothness[23])**2+np.diff(z_smoothness[23])**2))

arc_25_current = np.sum(np.sqrt(np.diff(robot_25[0])**2+np.diff(robot_25[1])**2+np.diff(robot_25[2])**2))
arc_25_proposed = np.sum(np.sqrt(np.diff(x_smoothness[24])**2+np.diff(y_smoothness[24])**2+np.diff(z_smoothness[24])**2))

arc_26_current = np.sum(np.sqrt(np.diff(robot_26[0])**2+np.diff(robot_26[1])**2+np.diff(robot_26[2])**2))
arc_26_proposed = np.sum(np.sqrt(np.diff(x_smoothness[25])**2+np.diff(y_smoothness[25])**2+np.diff(z_smoothness[25])**2))

arc_27_current = np.sum(np.sqrt(np.diff(robot_27[0])**2+np.diff(robot_27[1])**2+np.diff(robot_27[2])**2))
arc_27_proposed = np.sum(np.sqrt(np.diff(x_smoothness[26])**2+np.diff(y_smoothness[26])**2+np.diff(z_smoothness[26])**2))

arc_28_current = np.sum(np.sqrt(np.diff(robot_28[0])**2+np.diff(robot_28[1])**2+np.diff(robot_28[2])**2))
arc_28_proposed = np.sum(np.sqrt(np.diff(x_smoothness[27])**2+np.diff(y_smoothness[27])**2+np.diff(z_smoothness[27])**2))

arc_29_current = np.sum(np.sqrt(np.diff(robot_29[0])**2+np.diff(robot_29[1])**2+np.diff(robot_29[2])**2))
arc_29_proposed = np.sum(np.sqrt(np.diff(x_smoothness[28])**2+np.diff(y_smoothness[28])**2+np.diff(z_smoothness[28])**2))

arc_30_current = np.sum(np.sqrt(np.diff(robot_30[0])**2+np.diff(robot_30[1])**2+np.diff(robot_30[2])**2))
arc_30_proposed = np.sum(np.sqrt(np.diff(x_smoothness[29])**2+np.diff(y_smoothness[29])**2+np.diff(z_smoothness[29])**2))

arc_31_current = np.sum(np.sqrt(np.diff(robot_31[0])**2+np.diff(robot_31[1])**2+np.diff(robot_31[2])**2))
arc_31_proposed = np.sum(np.sqrt(np.diff(x_smoothness[30])**2+np.diff(y_smoothness[30])**2+np.diff(z_smoothness[30])**2))

arc_32_current = np.sum(np.sqrt(np.diff(robot_32[0])**2+np.diff(robot_32[1])**2+np.diff(robot_32[2])**2))
arc_32_proposed = np.sum(np.sqrt(np.diff(x_smoothness[31])**2+np.diff(y_smoothness[31])**2+np.diff(z_smoothness[31])**2))


# print(arc_1_proposed, arc_1_current)
# print(arc_2_proposed, arc_2_current)
# print(arc_3_proposed, arc_3_current)
# print(arc_4_proposed, arc_4_current)
# print(arc_5_proposed, arc_5_current)
# print(arc_6_proposed, arc_6_current)
# print(arc_7_proposed, arc_7_current)
# print(arc_8_proposed, arc_8_current)
# print(arc_9_proposed, arc_9_current)
# print(arc_10_proposed, arc_10_current)
# print(arc_11_proposed, arc_11_current)
# print(arc_12_proposed, arc_12_current)
# print(arc_13_proposed, arc_13_current)
# print(arc_14_proposed, arc_14_current)
# print(arc_15_proposed, arc_15_current)


arc_mean_proposed =  np.hstack(( arc_1_proposed, arc_2_proposed, arc_3_proposed, arc_4_proposed, arc_5_proposed, arc_6_proposed, arc_7_proposed, arc_8_proposed, arc_9_proposed, arc_10_proposed, arc_11_proposed, arc_12_proposed, arc_13_proposed, arc_14_proposed, arc_15_proposed, arc_16_proposed, arc_17_proposed, arc_18_proposed, arc_19_proposed, arc_20_proposed, arc_21_proposed, arc_22_proposed, arc_23_proposed, arc_24_proposed, arc_25_proposed, arc_26_proposed, arc_27_proposed, arc_28_proposed, arc_29_proposed, arc_30_proposed, arc_31_proposed, arc_32_proposed ))  
arc_mean_current =  np.hstack(( arc_1_current, arc_2_current, arc_3_current, arc_4_current, arc_5_current, arc_6_current, arc_7_current, arc_8_current, arc_9_current, arc_10_current, arc_11_current, arc_12_current, arc_13_current, arc_14_current, arc_15_current, arc_16_current, arc_17_current, arc_18_current, arc_19_current, arc_20_current, arc_21_current, arc_22_current, arc_23_current, arc_24_current, arc_25_current, arc_26_current, arc_27_current, arc_28_current, arc_29_current, arc_30_current, arc_31_current, arc_32_current ))  

arc_mean_prop_32robot_15 = arc_mean_proposed
arc_mean_curr_32robot_15 = arc_mean_current

scipy.io.savemat('arc_mean_prop_32robot_15.mat', {'arc_mean_prop_32robot_15': arc_mean_prop_32robot_15})
scipy.io.savemat('arc_mean_curr_32robot_15.mat', {'arc_mean_curr_32robot_15': arc_mean_curr_32robot_15})

print(arc_mean_proposed, arc_mean_current)

















fig = plt.figure(figsize=plt.figaspect(1))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x[0],y[0],z[0], '-r', linewidth = 2.0)
ax.plot(x[1],y[1],z[1], color ='pink', linewidth = 2.0)
ax.plot(x[2],y[2],z[2], color ='orange', linewidth = 2.0)
ax.plot(x[3],y[3],z[3], color ='green', linewidth = 2.0)
ax.plot(x[4],y[4],z[4], color ='grey', linewidth = 2.0)
ax.plot(x[5],y[5],z[5], color ='black', linewidth = 2.0)
ax.plot(x[6],y[6],z[6], color ='yellow', linewidth = 2.0)
ax.plot(x[7],y[7],z[7], color ='purple', linewidth = 2.0)
ax.plot(x[8],y[8],z[8], color ='darkgreen', linewidth = 2.0)
ax.plot(x[9],y[9],z[9], color ='teal', linewidth = 2.0)
ax.plot(x[10],y[10],z[10], color ='salmon', linewidth = 2.0)
ax.plot(x[11],y[11],z[11], color ='black', linewidth = 2.0)
ax.plot(x[12],y[12],z[12], color ='cyan', linewidth = 2.0)
ax.plot(x[13],y[13],z[13], color ='brown', linewidth = 2.0)
ax.plot(x[14],y[14],z[14], color ='coral', linewidth = 2.0)
ax.plot(x[15],y[15],z[15], color ='lime', linewidth = 2.0)
ax.plot(x[16],y[16],z[16], '-r', linewidth = 3.0)
ax.plot(x[17],y[17],z[17], color ='pink', linewidth = 3.0)
ax.plot(x[18],y[18],z[18], color ='orange', linewidth = 3.0)
ax.plot(x[19],y[19],z[19], color ='green', linewidth = 3.0)
ax.plot(x[20],y[20],z[20], color ='grey', linewidth = 3.0)
ax.plot(x[21],y[21],z[21], color ='black', linewidth = 3.0)
ax.plot(x[22],y[22],z[22], color ='yellow', linewidth = 3.0)
ax.plot(x[23],y[23],z[23], color ='purple', linewidth = 3.0)
ax.plot(x[24],y[24],z[24], color ='darkgreen', linewidth = 3.0)
ax.plot(x[25],y[25],z[25], color ='teal', linewidth = 3.0)
ax.plot(x[26],y[26],z[26], color ='salmon', linewidth = 3.0)
ax.plot(x[27],y[27],z[27], color ='wheat', linewidth = 3.0)
ax.plot(x[28],y[28],z[28], color ='blue', linewidth = 3.0)
ax.plot(x[29],y[29],z[29], color ='navy', linewidth = 3.0)
ax.plot(x[30],y[30],z[30], color ='gold', linewidth = 3.0)
ax.plot(x[31],y[31],z[31], color ='darkslategrey',linewidth = 3.0)


ax.plot(robot_1[0,:], robot_1[1,:], robot_1[2,:], '--r', linewidth = 2.0)
ax.plot(robot_2[0,:], robot_2[1,:], robot_2[2,:], '--', color = 'pink', linewidth = 2.0)
ax.plot(robot_3[0,:], robot_3[1,:], robot_3[2,:], '--', color = 'orange', linewidth = 2.0)
ax.plot(robot_4[0,:], robot_4[1,:], robot_4[2,:], '--', color = 'green', linewidth = 2.0)
ax.plot(robot_5[0,:], robot_5[1,:], robot_5[2,:], '--', color = 'grey', linewidth = 2.0)
ax.plot(robot_6[0,:], robot_6[1,:], robot_6[2,:], '--', color = 'black', linewidth = 2.0)
ax.plot(robot_7[0,:], robot_7[1,:], robot_7[2,:], '--', color = 'yellow', linewidth = 2.0)
ax.plot(robot_8[0,:], robot_8[1,:], robot_8[2,:], '--', color = 'purple', linewidth = 2.0)
ax.plot(robot_9[0,:], robot_9[1,:], robot_9[2,:], '--', color = 'darkgreen', linewidth = 2.0)
ax.plot(robot_10[0,:], robot_10[1,:], robot_10[2,:], '--', color = 'teal', linewidth = 2.0)
ax.plot(robot_11[0,:], robot_11[1,:], robot_11[2,:], '--', color = 'salmon', linewidth = 2.0)
ax.plot(robot_12[0,:], robot_12[1,:], robot_12[2,:], '--', color = 'black', linewidth = 2.0)
ax.plot(robot_13[0,:], robot_13[1,:], robot_13[2,:], '--', color = 'cyan', linewidth = 2.0)
ax.plot(robot_14[0,:], robot_14[1,:], robot_14[2,:], '--', color = 'brown', linewidth = 2.0)
ax.plot(robot_15[0,:], robot_15[1,:], robot_15[2,:], '--', color = 'coral', linewidth = 2.0)
ax.plot(robot_16[0,:], robot_16[1,:], robot_16[2,:], '--', color = 'lime', linewidth = 2.0)
ax.plot(robot_17[0,:], robot_17[1,:], robot_17[2,:], '--r', linewidth = 2.0)
ax.plot(robot_18[0,:], robot_18[1,:], robot_18[2,:], '--', color = 'pink', linewidth = 2.0)
ax.plot(robot_19[0,:], robot_19[1,:], robot_19[2,:], '--', color = 'orange', linewidth = 2.0)
ax.plot(robot_20[0,:], robot_20[1,:], robot_20[2,:], '--', color = 'green', linewidth = 2.0)
ax.plot(robot_21[0,:], robot_21[1,:], robot_21[2,:], '--', color = 'grey', linewidth = 2.0)
ax.plot(robot_22[0,:], robot_22[1,:], robot_22[2,:], '--', color = 'black', linewidth = 2.0)
ax.plot(robot_23[0,:], robot_23[1,:], robot_23[2,:], '--', color = 'yellow', linewidth = 2.0)
ax.plot(robot_24[0,:], robot_24[1,:], robot_24[2,:], '--', color = 'purple', linewidth = 2.0)
ax.plot(robot_25[0,:], robot_25[1,:], robot_25[2,:], '--', color = 'darkgreen', linewidth = 2.0)
ax.plot(robot_26[0,:], robot_26[1,:], robot_26[2,:], '--', color = 'teal', linewidth = 2.0)
ax.plot(robot_27[0,:], robot_27[1,:], robot_27[2,:], '--', color = 'salmon', linewidth = 2.0)
ax.plot(robot_28[0,:], robot_28[1,:], robot_28[2,:], '--', color = 'black', linewidth = 2.0)
ax.plot(robot_29[0,:], robot_29[1,:], robot_29[2,:], '--', color = 'cyan', linewidth = 2.0)
ax.plot(robot_30[0,:], robot_30[1,:], robot_30[2,:], '--', color = 'brown', linewidth = 2.0)
ax.plot(robot_31[0,:], robot_31[1,:], robot_31[2,:], '--', color = 'coral', linewidth = 2.0)
ax.plot(robot_32[0,:], robot_32[1,:], robot_32[2,:], '--', color = 'lime', linewidth = 2.0)


# plt.axis('equal')

plt.show()
