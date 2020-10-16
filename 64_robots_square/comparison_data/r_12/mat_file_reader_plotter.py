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

robot_33_temp = loadmat('robot_33.mat')
robot_33 = robot_33_temp['robot_33'].squeeze()

robot_34_temp = loadmat('robot_34.mat')
robot_34 = robot_34_temp['robot_34'].squeeze()

robot_35_temp = loadmat('robot_35.mat')
robot_35 = robot_35_temp['robot_35'].squeeze()


robot_36_temp = loadmat('robot_36.mat')
robot_36 = robot_36_temp['robot_36'].squeeze()


robot_37_temp = loadmat('robot_37.mat')
robot_37 = robot_37_temp['robot_37'].squeeze()


robot_38_temp = loadmat('robot_38.mat')
robot_38 = robot_38_temp['robot_38'].squeeze()


robot_39_temp = loadmat('robot_39.mat')
robot_39 = robot_39_temp['robot_39'].squeeze()


robot_40_temp = loadmat('robot_40.mat')
robot_40 = robot_40_temp['robot_40'].squeeze()

robot_41_temp = loadmat('robot_41.mat')
robot_41 = robot_41_temp['robot_41'].squeeze()

robot_42_temp = loadmat('robot_42.mat')
robot_42 = robot_42_temp['robot_42'].squeeze()

robot_43_temp = loadmat('robot_43.mat')
robot_43 = robot_43_temp['robot_43'].squeeze()

robot_44_temp = loadmat('robot_44.mat')
robot_44 = robot_44_temp['robot_44'].squeeze()

robot_45_temp = loadmat('robot_45.mat')
robot_45 = robot_45_temp['robot_45'].squeeze()

robot_46_temp = loadmat('robot_46.mat')
robot_46 = robot_46_temp['robot_46'].squeeze()

robot_47_temp = loadmat('robot_47.mat')
robot_47 = robot_47_temp['robot_47'].squeeze()

robot_48_temp = loadmat('robot_48.mat')
robot_48 = robot_48_temp['robot_48'].squeeze()

robot_49_temp = loadmat('robot_49.mat')
robot_49 = robot_49_temp['robot_49'].squeeze()

robot_50_temp = loadmat('robot_50.mat')
robot_50 = robot_50_temp['robot_50'].squeeze()

robot_51_temp = loadmat('robot_51.mat')
robot_51 = robot_51_temp['robot_51'].squeeze()

robot_52_temp = loadmat('robot_52.mat')
robot_52 = robot_52_temp['robot_52'].squeeze()

robot_53_temp = loadmat('robot_53.mat')
robot_53 = robot_53_temp['robot_53'].squeeze()

robot_54_temp = loadmat('robot_54.mat')
robot_54 = robot_54_temp['robot_54'].squeeze()

robot_55_temp = loadmat('robot_55.mat')
robot_55 = robot_55_temp['robot_55'].squeeze()

robot_56_temp = loadmat('robot_56.mat')
robot_56 = robot_56_temp['robot_56'].squeeze()

robot_57_temp = loadmat('robot_57.mat')
robot_57 = robot_57_temp['robot_57'].squeeze()

robot_58_temp = loadmat('robot_58.mat')
robot_58 = robot_58_temp['robot_58'].squeeze()

robot_59_temp = loadmat('robot_59.mat')
robot_59 = robot_59_temp['robot_59'].squeeze()

robot_60_temp = loadmat('robot_60.mat')
robot_60 = robot_60_temp['robot_60'].squeeze()

robot_61_temp = loadmat('robot_61.mat')
robot_61 = robot_61_temp['robot_61'].squeeze()

robot_62_temp = loadmat('robot_62.mat')
robot_62 = robot_62_temp['robot_62'].squeeze()

robot_63_temp = loadmat('robot_63.mat')
robot_63 = robot_63_temp['robot_63'].squeeze()

robot_64_temp = loadmat('robot_64.mat')
robot_64 = robot_64_temp['robot_64'].squeeze()



############################## Loadng the trajectories from the proposed code



x_temp = scipy.io.loadmat('x_2.mat')
x = x_temp['x_2'].squeeze()

y_temp = scipy.io.loadmat('y_2.mat')
y = y_temp['y_2'].squeeze()

z_temp = scipy.io.loadmat('z_2.mat')
z = z_temp['z_2'].squeeze()

#################################smoothness comparison############
t_fin =  10.0
num_horizon = 100
tot_time = np.linspace(0.0, t_fin, num_horizon)
new_num_horizon = 721
tot_time_interp = np.linspace(0.0, t_fin, new_num_horizon)


f_x = interpolate.interp1d(tot_time, x)
f_y = interpolate.interp1d(tot_time, y)
f_z = interpolate.interp1d(tot_time, z)

x_smoothness = f_x(tot_time_interp)
y_smoothness = f_y(tot_time_interp)
z_smoothness = f_z(tot_time_interp)

print(np.shape(x_smoothness))

#x_robot_1 = np.vstack((robot_1[0], robot_2[0], robot_3[0], robot_4[0], robot_5[0], robot_6[0], robot_7[0], robot_8[0], robot_9[0], robot_10[0], robot_11[0], robot_12[0], robot_13[0], robot_14[0], robot_15[0], robot_16[0], robot_17[0], robot_18[0], robot_19[0], robot_20[0], robot_21[0], robot_22[0], robot_23[0], robot_24[0], robot_25[0], robot_26[0], robot_27[0], robot_28[0], robot_29[0], robot_30[0], robot_31[0], robot_32[0]))
#x_robot_2 = np.vstack((robot_33[0], robot_34[0], robot_35[0], robot_36[0], robot_37[0], robot_38[0], robot_39[0], robot_40[0], robot_41[0], robot_42[0], robot_43[0], robot_44[0], robot_45[0], robot_46[0], robot_47[0], robot_48[0], robot_49[0], robot_50[0], robot_51[0], robot_52[0], robot_53[0], robot_54[0], robot_55[0], robot_56[0], robot_57[0], robot_58[0], robot_59[0], robot_60[0], robot_61[0], robot_62[0], robot_63[0], robot_64[0]))
#x_robot = np.vstack((x_robot_1,x_robot_2))


#y_robot_1 = np.vstack((robot_1[1], robot_2[1], robot_3[1], robot_4[1], robot_5[1], robot_6[1], robot_7[1], robot_8[1], robot_9[1], robot_10[1], robot_11[1], robot_12[1], robot_13[1], robot_14[1], robot_15[1], robot_16[1], robot_17[1], robot_18[1], robot_19[1], robot_20[1], robot_21[1], robot_22[1], robot_23[1], robot_24[1], robot_25[1], robot_26[1], robot_27[1], robot_28[1], robot_29[1], robot_30[1], robot_31[1], robot_32[1]))
#y_robot_2 = np.vstack((robot_33[1], robot_34[1], robot_35[1], robot_36[1], robot_37[1], robot_38[1], robot_39[1], robot_40[1], robot_41[1], robot_42[1], robot_43[1], robot_44[1], robot_45[1], robot_46[1], robot_47[1], robot_48[1], robot_49[1], robot_50[1], robot_51[1], robot_52[1], robot_53[1], robot_54[1], robot_55[1], robot_56[1], robot_57[1], robot_58[1], robot_59[1], robot_60[1], robot_61[1], robot_62[1], robot_63[1], robot_64[1]))
#y_robot = np.vstack((y_robot_1,y_robot_2))

#z_robot_1 = np.vstack((robot_1[2], robot_2[2], robot_3[2], robot_4[2], robot_5[2], robot_6[2], robot_7[2], robot_8[2], robot_9[2], robot_10[2], robot_11[2], robot_12[2], robot_13[2], robot_14[2], robot_15[2], robot_16[2], robot_17[2], robot_18[2], robot_19[2], robot_20[2], robot_21[2], robot_22[2], robot_23[2], robot_24[2], robot_25[2], robot_26[2], robot_27[2], robot_28[2], robot_29[2], robot_30[2], robot_31[2], robot_32[2]))
#z_robot_2 = np.vstack((robot_33[2], robot_34[2], robot_35[2], robot_36[2], robot_37[2], robot_38[2], robot_39[2], robot_40[2], robot_41[2], robot_42[2], robot_43[2], robot_44[2], robot_45[2], robot_46[2], robot_47[2], robot_48[2], robot_49[2], robot_50[2], robot_51[2], robot_52[2], robot_53[2], robot_54[2], robot_55[2], robot_56[2], robot_57[2], robot_58[2], robot_59[2], robot_60[2], robot_61[2], robot_62[2], robot_63[2], robot_64[2]))
#z_robot = np.vstack((z_robot_1, z_robot_2))

#print(np.shape(x_robot))
#cost_smoothness_prop_64rob_12 = np.linalg.norm(np.diff(np.diff(x_smoothness)))+np.linalg.norm(np.diff(np.diff(y_smoothness)))+np.linalg.norm(np.diff(np.diff(z_smoothness)))
#cost_smoothness_curr_64rob_12 = np.linalg.norm(np.diff(np.diff(x_robot)))+np.linalg.norm(np.diff(np.diff(y_robot)))+np.linalg.norm(np.diff(np.diff(z_robot)))

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


cost_smoothness_prop_33 = np.linalg.norm(np.diff(np.diff(x_smoothness[32])))+np.linalg.norm(np.diff(np.diff(y_smoothness[32])))+np.linalg.norm(np.diff(np.diff(z_smoothness[32])))
cost_smoothness_curr_33 = np.linalg.norm(np.diff(np.diff(robot_33[0])))+np.linalg.norm(np.diff(np.diff(robot_33[1])))+np.linalg.norm(np.diff(np.diff(robot_33[2])))

cost_smoothness_prop_34 = np.linalg.norm(np.diff(np.diff(x_smoothness[33])))+np.linalg.norm(np.diff(np.diff(y_smoothness[33])))+np.linalg.norm(np.diff(np.diff(z_smoothness[33])))
cost_smoothness_curr_34 = np.linalg.norm(np.diff(np.diff(robot_34[0])))+np.linalg.norm(np.diff(np.diff(robot_34[1])))+np.linalg.norm(np.diff(np.diff(robot_34[2])))

cost_smoothness_prop_35 = np.linalg.norm(np.diff(np.diff(x_smoothness[34])))+np.linalg.norm(np.diff(np.diff(y_smoothness[34])))+np.linalg.norm(np.diff(np.diff(z_smoothness[34])))
cost_smoothness_curr_35 = np.linalg.norm(np.diff(np.diff(robot_35[0])))+np.linalg.norm(np.diff(np.diff(robot_35[1])))+np.linalg.norm(np.diff(np.diff(robot_35[2])))

cost_smoothness_prop_36 = np.linalg.norm(np.diff(np.diff(x_smoothness[35])))+np.linalg.norm(np.diff(np.diff(y_smoothness[35])))+np.linalg.norm(np.diff(np.diff(z_smoothness[35])))
cost_smoothness_curr_36 = np.linalg.norm(np.diff(np.diff(robot_36[0])))+np.linalg.norm(np.diff(np.diff(robot_36[1])))+np.linalg.norm(np.diff(np.diff(robot_36[2])))

cost_smoothness_prop_37 = np.linalg.norm(np.diff(np.diff(x_smoothness[36])))+np.linalg.norm(np.diff(np.diff(y_smoothness[36])))+np.linalg.norm(np.diff(np.diff(z_smoothness[36])))
cost_smoothness_curr_37 = np.linalg.norm(np.diff(np.diff(robot_37[0])))+np.linalg.norm(np.diff(np.diff(robot_37[1])))+np.linalg.norm(np.diff(np.diff(robot_37[2])))

cost_smoothness_prop_38 = np.linalg.norm(np.diff(np.diff(x_smoothness[37])))+np.linalg.norm(np.diff(np.diff(y_smoothness[37])))+np.linalg.norm(np.diff(np.diff(z_smoothness[37])))
cost_smoothness_curr_38 = np.linalg.norm(np.diff(np.diff(robot_38[0])))+np.linalg.norm(np.diff(np.diff(robot_38[1])))+np.linalg.norm(np.diff(np.diff(robot_38[2])))

cost_smoothness_prop_39 = np.linalg.norm(np.diff(np.diff(x_smoothness[38])))+np.linalg.norm(np.diff(np.diff(y_smoothness[38])))+np.linalg.norm(np.diff(np.diff(z_smoothness[38])))
cost_smoothness_curr_39 = np.linalg.norm(np.diff(np.diff(robot_39[0])))+np.linalg.norm(np.diff(np.diff(robot_39[1])))+np.linalg.norm(np.diff(np.diff(robot_39[2])))

cost_smoothness_prop_40 = np.linalg.norm(np.diff(np.diff(x_smoothness[39])))+np.linalg.norm(np.diff(np.diff(y_smoothness[39])))+np.linalg.norm(np.diff(np.diff(z_smoothness[39])))
cost_smoothness_curr_40 = np.linalg.norm(np.diff(np.diff(robot_40[0])))+np.linalg.norm(np.diff(np.diff(robot_40[1])))+np.linalg.norm(np.diff(np.diff(robot_40[2])))

cost_smoothness_prop_41 = np.linalg.norm(np.diff(np.diff(x_smoothness[40])))+np.linalg.norm(np.diff(np.diff(y_smoothness[40])))+np.linalg.norm(np.diff(np.diff(z_smoothness[40])))
cost_smoothness_curr_41 = np.linalg.norm(np.diff(np.diff(robot_41[0])))+np.linalg.norm(np.diff(np.diff(robot_41[1])))+np.linalg.norm(np.diff(np.diff(robot_41[2])))

cost_smoothness_prop_42 = np.linalg.norm(np.diff(np.diff(x_smoothness[41])))+np.linalg.norm(np.diff(np.diff(y_smoothness[41])))+np.linalg.norm(np.diff(np.diff(z_smoothness[41])))
cost_smoothness_curr_42 = np.linalg.norm(np.diff(np.diff(robot_42[0])))+np.linalg.norm(np.diff(np.diff(robot_42[1])))+np.linalg.norm(np.diff(np.diff(robot_42[2])))

cost_smoothness_prop_43 = np.linalg.norm(np.diff(np.diff(x_smoothness[42])))+np.linalg.norm(np.diff(np.diff(y_smoothness[42])))+np.linalg.norm(np.diff(np.diff(z_smoothness[42])))
cost_smoothness_curr_43 = np.linalg.norm(np.diff(np.diff(robot_43[0])))+np.linalg.norm(np.diff(np.diff(robot_43[1])))+np.linalg.norm(np.diff(np.diff(robot_43[2])))

cost_smoothness_prop_44 = np.linalg.norm(np.diff(np.diff(x_smoothness[43])))+np.linalg.norm(np.diff(np.diff(y_smoothness[43])))+np.linalg.norm(np.diff(np.diff(z_smoothness[43])))
cost_smoothness_curr_44 = np.linalg.norm(np.diff(np.diff(robot_44[0])))+np.linalg.norm(np.diff(np.diff(robot_44[1])))+np.linalg.norm(np.diff(np.diff(robot_44[2])))

cost_smoothness_prop_45 = np.linalg.norm(np.diff(np.diff(x_smoothness[44])))+np.linalg.norm(np.diff(np.diff(y_smoothness[44])))+np.linalg.norm(np.diff(np.diff(z_smoothness[44])))
cost_smoothness_curr_45 = np.linalg.norm(np.diff(np.diff(robot_45[0])))+np.linalg.norm(np.diff(np.diff(robot_45[1])))+np.linalg.norm(np.diff(np.diff(robot_45[2])))

cost_smoothness_prop_46 = np.linalg.norm(np.diff(np.diff(x_smoothness[45])))+np.linalg.norm(np.diff(np.diff(y_smoothness[45])))+np.linalg.norm(np.diff(np.diff(z_smoothness[45])))
cost_smoothness_curr_46 = np.linalg.norm(np.diff(np.diff(robot_46[0])))+np.linalg.norm(np.diff(np.diff(robot_46[1])))+np.linalg.norm(np.diff(np.diff(robot_46[2])))

cost_smoothness_prop_47 = np.linalg.norm(np.diff(np.diff(x_smoothness[46])))+np.linalg.norm(np.diff(np.diff(y_smoothness[46])))+np.linalg.norm(np.diff(np.diff(z_smoothness[46])))
cost_smoothness_curr_47 = np.linalg.norm(np.diff(np.diff(robot_47[0])))+np.linalg.norm(np.diff(np.diff(robot_47[1])))+np.linalg.norm(np.diff(np.diff(robot_47[2])))

cost_smoothness_prop_48 = np.linalg.norm(np.diff(np.diff(x_smoothness[47])))+np.linalg.norm(np.diff(np.diff(y_smoothness[47])))+np.linalg.norm(np.diff(np.diff(z_smoothness[47])))
cost_smoothness_curr_48 = np.linalg.norm(np.diff(np.diff(robot_48[0])))+np.linalg.norm(np.diff(np.diff(robot_48[1])))+np.linalg.norm(np.diff(np.diff(robot_48[2])))

cost_smoothness_prop_49 = np.linalg.norm(np.diff(np.diff(x_smoothness[48])))+np.linalg.norm(np.diff(np.diff(y_smoothness[48])))+np.linalg.norm(np.diff(np.diff(z_smoothness[48])))
cost_smoothness_curr_49 = np.linalg.norm(np.diff(np.diff(robot_49[0])))+np.linalg.norm(np.diff(np.diff(robot_49[1])))+np.linalg.norm(np.diff(np.diff(robot_49[2])))

cost_smoothness_prop_50 = np.linalg.norm(np.diff(np.diff(x_smoothness[49])))+np.linalg.norm(np.diff(np.diff(y_smoothness[49])))+np.linalg.norm(np.diff(np.diff(z_smoothness[49])))
cost_smoothness_curr_50 = np.linalg.norm(np.diff(np.diff(robot_50[0])))+np.linalg.norm(np.diff(np.diff(robot_50[1])))+np.linalg.norm(np.diff(np.diff(robot_50[2])))

cost_smoothness_prop_51 = np.linalg.norm(np.diff(np.diff(x_smoothness[50])))+np.linalg.norm(np.diff(np.diff(y_smoothness[50])))+np.linalg.norm(np.diff(np.diff(z_smoothness[50])))
cost_smoothness_curr_51 = np.linalg.norm(np.diff(np.diff(robot_51[0])))+np.linalg.norm(np.diff(np.diff(robot_51[1])))+np.linalg.norm(np.diff(np.diff(robot_51[2])))

cost_smoothness_prop_52 = np.linalg.norm(np.diff(np.diff(x_smoothness[51])))+np.linalg.norm(np.diff(np.diff(y_smoothness[51])))+np.linalg.norm(np.diff(np.diff(z_smoothness[51])))
cost_smoothness_curr_52 = np.linalg.norm(np.diff(np.diff(robot_52[0])))+np.linalg.norm(np.diff(np.diff(robot_52[1])))+np.linalg.norm(np.diff(np.diff(robot_52[2])))

cost_smoothness_prop_53 = np.linalg.norm(np.diff(np.diff(x_smoothness[52])))+np.linalg.norm(np.diff(np.diff(y_smoothness[52])))+np.linalg.norm(np.diff(np.diff(z_smoothness[52])))
cost_smoothness_curr_53 = np.linalg.norm(np.diff(np.diff(robot_53[0])))+np.linalg.norm(np.diff(np.diff(robot_53[1])))+np.linalg.norm(np.diff(np.diff(robot_53[2])))

cost_smoothness_prop_54 = np.linalg.norm(np.diff(np.diff(x_smoothness[53])))+np.linalg.norm(np.diff(np.diff(y_smoothness[53])))+np.linalg.norm(np.diff(np.diff(z_smoothness[53])))
cost_smoothness_curr_54 = np.linalg.norm(np.diff(np.diff(robot_54[0])))+np.linalg.norm(np.diff(np.diff(robot_54[1])))+np.linalg.norm(np.diff(np.diff(robot_54[2])))

cost_smoothness_prop_55 = np.linalg.norm(np.diff(np.diff(x_smoothness[54])))+np.linalg.norm(np.diff(np.diff(y_smoothness[54])))+np.linalg.norm(np.diff(np.diff(z_smoothness[54])))
cost_smoothness_curr_55 = np.linalg.norm(np.diff(np.diff(robot_55[0])))+np.linalg.norm(np.diff(np.diff(robot_55[1])))+np.linalg.norm(np.diff(np.diff(robot_55[2])))

cost_smoothness_prop_56 = np.linalg.norm(np.diff(np.diff(x_smoothness[55])))+np.linalg.norm(np.diff(np.diff(y_smoothness[55])))+np.linalg.norm(np.diff(np.diff(z_smoothness[55])))
cost_smoothness_curr_56 = np.linalg.norm(np.diff(np.diff(robot_56[0])))+np.linalg.norm(np.diff(np.diff(robot_56[1])))+np.linalg.norm(np.diff(np.diff(robot_56[2])))

cost_smoothness_prop_57 = np.linalg.norm(np.diff(np.diff(x_smoothness[56])))+np.linalg.norm(np.diff(np.diff(y_smoothness[56])))+np.linalg.norm(np.diff(np.diff(z_smoothness[56])))
cost_smoothness_curr_57 = np.linalg.norm(np.diff(np.diff(robot_57[0])))+np.linalg.norm(np.diff(np.diff(robot_57[1])))+np.linalg.norm(np.diff(np.diff(robot_57[2])))

cost_smoothness_prop_58 = np.linalg.norm(np.diff(np.diff(x_smoothness[57])))+np.linalg.norm(np.diff(np.diff(y_smoothness[57])))+np.linalg.norm(np.diff(np.diff(z_smoothness[57])))
cost_smoothness_curr_58 = np.linalg.norm(np.diff(np.diff(robot_58[0])))+np.linalg.norm(np.diff(np.diff(robot_58[1])))+np.linalg.norm(np.diff(np.diff(robot_58[2])))

cost_smoothness_prop_59 = np.linalg.norm(np.diff(np.diff(x_smoothness[58])))+np.linalg.norm(np.diff(np.diff(y_smoothness[58])))+np.linalg.norm(np.diff(np.diff(z_smoothness[58])))
cost_smoothness_curr_59 = np.linalg.norm(np.diff(np.diff(robot_59[0])))+np.linalg.norm(np.diff(np.diff(robot_59[1])))+np.linalg.norm(np.diff(np.diff(robot_59[2])))

cost_smoothness_prop_60 = np.linalg.norm(np.diff(np.diff(x_smoothness[59])))+np.linalg.norm(np.diff(np.diff(y_smoothness[59])))+np.linalg.norm(np.diff(np.diff(z_smoothness[59])))
cost_smoothness_curr_60 = np.linalg.norm(np.diff(np.diff(robot_60[0])))+np.linalg.norm(np.diff(np.diff(robot_60[1])))+np.linalg.norm(np.diff(np.diff(robot_60[2])))

cost_smoothness_prop_61 = np.linalg.norm(np.diff(np.diff(x_smoothness[60])))+np.linalg.norm(np.diff(np.diff(y_smoothness[60])))+np.linalg.norm(np.diff(np.diff(z_smoothness[60])))
cost_smoothness_curr_61 = np.linalg.norm(np.diff(np.diff(robot_61[0])))+np.linalg.norm(np.diff(np.diff(robot_61[1])))+np.linalg.norm(np.diff(np.diff(robot_61[2])))

cost_smoothness_prop_62 = np.linalg.norm(np.diff(np.diff(x_smoothness[61])))+np.linalg.norm(np.diff(np.diff(y_smoothness[61])))+np.linalg.norm(np.diff(np.diff(z_smoothness[61])))
cost_smoothness_curr_62 = np.linalg.norm(np.diff(np.diff(robot_62[0])))+np.linalg.norm(np.diff(np.diff(robot_62[1])))+np.linalg.norm(np.diff(np.diff(robot_62[2])))

cost_smoothness_prop_63 = np.linalg.norm(np.diff(np.diff(x_smoothness[62])))+np.linalg.norm(np.diff(np.diff(y_smoothness[62])))+np.linalg.norm(np.diff(np.diff(z_smoothness[62])))
cost_smoothness_curr_63 = np.linalg.norm(np.diff(np.diff(robot_63[0])))+np.linalg.norm(np.diff(np.diff(robot_63[1])))+np.linalg.norm(np.diff(np.diff(robot_63[2])))

cost_smoothness_prop_64 = np.linalg.norm(np.diff(np.diff(x_smoothness[63])))+np.linalg.norm(np.diff(np.diff(y_smoothness[63])))+np.linalg.norm(np.diff(np.diff(z_smoothness[63])))
cost_smoothness_curr_64 = np.linalg.norm(np.diff(np.diff(robot_64[0])))+np.linalg.norm(np.diff(np.diff(robot_64[1])))+np.linalg.norm(np.diff(np.diff(robot_64[2])))

cost_smoothness_prop1 = np.hstack((cost_smoothness_prop_1, cost_smoothness_prop_2, cost_smoothness_prop_3, cost_smoothness_prop_4, cost_smoothness_prop_5, cost_smoothness_prop_6, cost_smoothness_prop_7, cost_smoothness_prop_8, cost_smoothness_prop_9, cost_smoothness_prop_10, cost_smoothness_prop_11, cost_smoothness_prop_12,cost_smoothness_prop_13, cost_smoothness_prop_14, cost_smoothness_prop_15, cost_smoothness_prop_16, cost_smoothness_prop_17, cost_smoothness_prop_18, cost_smoothness_prop_19, cost_smoothness_prop_20, cost_smoothness_prop_21, cost_smoothness_prop_22, cost_smoothness_prop_23, cost_smoothness_prop_24, cost_smoothness_prop_25, cost_smoothness_prop_26, cost_smoothness_prop_27, cost_smoothness_prop_28, cost_smoothness_prop_29, cost_smoothness_prop_30, cost_smoothness_prop_31, cost_smoothness_prop_32))
cost_smoothness_curr1 = np.hstack((cost_smoothness_curr_1, cost_smoothness_curr_2, cost_smoothness_curr_3, cost_smoothness_curr_4, cost_smoothness_curr_5, cost_smoothness_curr_6, cost_smoothness_curr_7, cost_smoothness_curr_8, cost_smoothness_curr_9, cost_smoothness_curr_10, cost_smoothness_curr_11, cost_smoothness_curr_12, cost_smoothness_curr_13, cost_smoothness_curr_14, cost_smoothness_curr_15, cost_smoothness_curr_16, cost_smoothness_curr_17, cost_smoothness_curr_18, cost_smoothness_curr_19, cost_smoothness_curr_20, cost_smoothness_curr_21, cost_smoothness_curr_22, cost_smoothness_curr_23, cost_smoothness_curr_24, cost_smoothness_curr_25, cost_smoothness_curr_26, cost_smoothness_curr_27, cost_smoothness_curr_28, cost_smoothness_curr_29, cost_smoothness_curr_30, cost_smoothness_curr_31, cost_smoothness_curr_32))

cost_smoothness_prop2 = np.hstack((cost_smoothness_prop_33, cost_smoothness_prop_34, cost_smoothness_prop_35, cost_smoothness_prop_36, cost_smoothness_prop_37, cost_smoothness_prop_38, cost_smoothness_prop_39, cost_smoothness_prop_40, cost_smoothness_prop_41, cost_smoothness_prop_42, cost_smoothness_prop_43, cost_smoothness_prop_44,cost_smoothness_prop_45, cost_smoothness_prop_46, cost_smoothness_prop_47, cost_smoothness_prop_48, cost_smoothness_prop_49, cost_smoothness_prop_50, cost_smoothness_prop_51, cost_smoothness_prop_52, cost_smoothness_prop_53, cost_smoothness_prop_54, cost_smoothness_prop_55, cost_smoothness_prop_56, cost_smoothness_prop_57, cost_smoothness_prop_58, cost_smoothness_prop_59, cost_smoothness_prop_60, cost_smoothness_prop_61, cost_smoothness_prop_62, cost_smoothness_prop_63, cost_smoothness_prop_64))
cost_smoothness_curr2 = np.hstack((cost_smoothness_curr_33, cost_smoothness_curr_34, cost_smoothness_curr_35, cost_smoothness_curr_36, cost_smoothness_curr_37, cost_smoothness_curr_38, cost_smoothness_curr_39, cost_smoothness_curr_40, cost_smoothness_curr_41, cost_smoothness_curr_42, cost_smoothness_curr_43, cost_smoothness_curr_44, cost_smoothness_curr_45, cost_smoothness_curr_46, cost_smoothness_curr_47, cost_smoothness_curr_48, cost_smoothness_curr_49, cost_smoothness_curr_50, cost_smoothness_curr_51, cost_smoothness_curr_52, cost_smoothness_curr_53, cost_smoothness_curr_54, cost_smoothness_curr_55, cost_smoothness_curr_56, cost_smoothness_curr_57, cost_smoothness_curr_58, cost_smoothness_curr_59, cost_smoothness_curr_60, cost_smoothness_curr_61, cost_smoothness_curr_62, cost_smoothness_curr_63, cost_smoothness_curr_64))

cost_smoothness_prop_64rob_12 = np.hstack((cost_smoothness_prop1, cost_smoothness_prop2 ))
cost_smoothness_curr_64rob_12 = np.hstack((cost_smoothness_curr1, cost_smoothness_curr2 ))

scipy.io.savemat('cost_smoothness_prop_64rob_12.mat', {'cost_smoothness_prop_64rob_12': cost_smoothness_prop_64rob_12})
scipy.io.savemat('cost_smoothness_curr_64rob_12.mat', {'cost_smoothness_curr_64rob_12': cost_smoothness_curr_64rob_12})

print(cost_smoothness_prop_64rob_12)
print(cost_smoothness_curr_64rob_12)
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

arc_33_current = np.sum(np.sqrt(np.diff(robot_33[0])**2+np.diff(robot_33[1])**2+np.diff(robot_33[2])**2))
arc_33_proposed = np.sum(np.sqrt(np.diff(x_smoothness[32])**2+np.diff(y_smoothness[32])**2+np.diff(z_smoothness[32])**2))

arc_34_current = np.sum(np.sqrt(np.diff(robot_34[0])**2+np.diff(robot_34[1])**2+np.diff(robot_34[2])**2))
arc_34_proposed = np.sum(np.sqrt(np.diff(x_smoothness[33])**2+np.diff(y_smoothness[33])**2+np.diff(z_smoothness[33])**2))


arc_35_current = np.sum(np.sqrt(np.diff(robot_35[0])**2+np.diff(robot_35[1])**2+np.diff(robot_35[2])**2))
arc_35_proposed = np.sum(np.sqrt(np.diff(x_smoothness[34])**2+np.diff(y_smoothness[34])**2+np.diff(z_smoothness[34])**2))


arc_36_current = np.sum(np.sqrt(np.diff(robot_36[0])**2+np.diff(robot_36[1])**2+np.diff(robot_36[2])**2))
arc_36_proposed = np.sum(np.sqrt(np.diff(x_smoothness[35])**2+np.diff(y_smoothness[35])**2+np.diff(z_smoothness[35])**2))


arc_37_current = np.sum(np.sqrt(np.diff(robot_37[0])**2+np.diff(robot_37[1])**2+np.diff(robot_37[2])**2))
arc_37_proposed = np.sum(np.sqrt(np.diff(x_smoothness[36])**2+np.diff(y_smoothness[36])**2+np.diff(z_smoothness[36])**2))

arc_38_current = np.sum(np.sqrt(np.diff(robot_38[0])**2+np.diff(robot_38[1])**2+np.diff(robot_38[2])**2))
arc_38_proposed = np.sum(np.sqrt(np.diff(x_smoothness[37])**2+np.diff(y_smoothness[37])**2+np.diff(z_smoothness[37])**2))

arc_39_current = np.sum(np.sqrt(np.diff(robot_39[0])**2+np.diff(robot_39[1])**2+np.diff(robot_39[2])**2))
arc_39_proposed = np.sum(np.sqrt(np.diff(x_smoothness[38])**2+np.diff(y_smoothness[38])**2+np.diff(z_smoothness[38])**2))

arc_40_current = np.sum(np.sqrt(np.diff(robot_40[0])**2+np.diff(robot_40[1])**2+np.diff(robot_40[2])**2))
arc_40_proposed = np.sum(np.sqrt(np.diff(x_smoothness[39])**2+np.diff(y_smoothness[39])**2+np.diff(z_smoothness[39])**2))

arc_41_current = np.sum(np.sqrt(np.diff(robot_41[0])**2+np.diff(robot_41[1])**2+np.diff(robot_41[2])**2))
arc_41_proposed = np.sum(np.sqrt(np.diff(x_smoothness[40])**2+np.diff(y_smoothness[40])**2+np.diff(z_smoothness[40])**2))

arc_42_current = np.sum(np.sqrt(np.diff(robot_42[0])**2+np.diff(robot_42[1])**2+np.diff(robot_42[2])**2))
arc_42_proposed = np.sum(np.sqrt(np.diff(x_smoothness[41])**2+np.diff(y_smoothness[41])**2+np.diff(z_smoothness[41])**2))

arc_43_current = np.sum(np.sqrt(np.diff(robot_43[0])**2+np.diff(robot_43[1])**2+np.diff(robot_43[2])**2))
arc_43_proposed = np.sum(np.sqrt(np.diff(x_smoothness[42])**2+np.diff(y_smoothness[42])**2+np.diff(z_smoothness[42])**2))

arc_44_current = np.sum(np.sqrt(np.diff(robot_44[0])**2+np.diff(robot_44[1])**2+np.diff(robot_44[2])**2))
arc_44_proposed = np.sum(np.sqrt(np.diff(x_smoothness[43])**2+np.diff(y_smoothness[43])**2+np.diff(z_smoothness[43])**2))

arc_45_current = np.sum(np.sqrt(np.diff(robot_45[0])**2+np.diff(robot_45[1])**2+np.diff(robot_45[2])**2))
arc_45_proposed = np.sum(np.sqrt(np.diff(x_smoothness[44])**2+np.diff(y_smoothness[44])**2+np.diff(z_smoothness[44])**2))

arc_46_current = np.sum(np.sqrt(np.diff(robot_46[0])**2+np.diff(robot_46[1])**2+np.diff(robot_46[2])**2))
arc_46_proposed = np.sum(np.sqrt(np.diff(x_smoothness[45])**2+np.diff(y_smoothness[45])**2+np.diff(z_smoothness[45])**2))

arc_47_current = np.sum(np.sqrt(np.diff(robot_47[0])**2+np.diff(robot_47[1])**2+np.diff(robot_47[2])**2))
arc_47_proposed = np.sum(np.sqrt(np.diff(x_smoothness[46])**2+np.diff(y_smoothness[46])**2+np.diff(z_smoothness[46])**2))

arc_48_current = np.sum(np.sqrt(np.diff(robot_48[0])**2+np.diff(robot_48[1])**2+np.diff(robot_48[2])**2))
arc_48_proposed = np.sum(np.sqrt(np.diff(x_smoothness[47])**2+np.diff(y_smoothness[47])**2+np.diff(z_smoothness[47])**2))

arc_49_current = np.sum(np.sqrt(np.diff(robot_49[0])**2+np.diff(robot_49[1])**2+np.diff(robot_49[2])**2))
arc_49_proposed = np.sum(np.sqrt(np.diff(x_smoothness[48])**2+np.diff(y_smoothness[48])**2+np.diff(z_smoothness[48])**2))

arc_50_current = np.sum(np.sqrt(np.diff(robot_50[0])**2+np.diff(robot_50[1])**2+np.diff(robot_50[2])**2))
arc_50_proposed = np.sum(np.sqrt(np.diff(x_smoothness[49])**2+np.diff(y_smoothness[49])**2+np.diff(z_smoothness[49])**2))

arc_51_current = np.sum(np.sqrt(np.diff(robot_51[0])**2+np.diff(robot_51[1])**2+np.diff(robot_51[2])**2))
arc_51_proposed = np.sum(np.sqrt(np.diff(x_smoothness[50])**2+np.diff(y_smoothness[50])**2+np.diff(z_smoothness[50])**2))

arc_52_current = np.sum(np.sqrt(np.diff(robot_52[0])**2+np.diff(robot_52[1])**2+np.diff(robot_52[2])**2))
arc_52_proposed = np.sum(np.sqrt(np.diff(x_smoothness[51])**2+np.diff(y_smoothness[51])**2+np.diff(z_smoothness[51])**2))

arc_53_current = np.sum(np.sqrt(np.diff(robot_53[0])**2+np.diff(robot_53[1])**2+np.diff(robot_53[2])**2))
arc_53_proposed = np.sum(np.sqrt(np.diff(x_smoothness[52])**2+np.diff(y_smoothness[52])**2+np.diff(z_smoothness[52])**2))

arc_54_current = np.sum(np.sqrt(np.diff(robot_54[0])**2+np.diff(robot_54[1])**2+np.diff(robot_54[2])**2))
arc_54_proposed = np.sum(np.sqrt(np.diff(x_smoothness[53])**2+np.diff(y_smoothness[53])**2+np.diff(z_smoothness[53])**2))

arc_55_current = np.sum(np.sqrt(np.diff(robot_55[0])**2+np.diff(robot_55[1])**2+np.diff(robot_55[2])**2))
arc_55_proposed = np.sum(np.sqrt(np.diff(x_smoothness[54])**2+np.diff(y_smoothness[54])**2+np.diff(z_smoothness[54])**2))

arc_56_current = np.sum(np.sqrt(np.diff(robot_56[0])**2+np.diff(robot_56[1])**2+np.diff(robot_56[2])**2))
arc_56_proposed = np.sum(np.sqrt(np.diff(x_smoothness[55])**2+np.diff(y_smoothness[55])**2+np.diff(z_smoothness[55])**2))

arc_57_current = np.sum(np.sqrt(np.diff(robot_57[0])**2+np.diff(robot_57[1])**2+np.diff(robot_57[2])**2))
arc_57_proposed = np.sum(np.sqrt(np.diff(x_smoothness[56])**2+np.diff(y_smoothness[56])**2+np.diff(z_smoothness[56])**2))

arc_58_current = np.sum(np.sqrt(np.diff(robot_58[0])**2+np.diff(robot_58[1])**2+np.diff(robot_58[2])**2))
arc_58_proposed = np.sum(np.sqrt(np.diff(x_smoothness[57])**2+np.diff(y_smoothness[57])**2+np.diff(z_smoothness[57])**2))

arc_59_current = np.sum(np.sqrt(np.diff(robot_59[0])**2+np.diff(robot_59[1])**2+np.diff(robot_59[2])**2))
arc_59_proposed = np.sum(np.sqrt(np.diff(x_smoothness[58])**2+np.diff(y_smoothness[58])**2+np.diff(z_smoothness[58])**2))

arc_60_current = np.sum(np.sqrt(np.diff(robot_60[0])**2+np.diff(robot_60[1])**2+np.diff(robot_60[2])**2))
arc_60_proposed = np.sum(np.sqrt(np.diff(x_smoothness[59])**2+np.diff(y_smoothness[59])**2+np.diff(z_smoothness[59])**2))

arc_61_current = np.sum(np.sqrt(np.diff(robot_61[0])**2+np.diff(robot_61[1])**2+np.diff(robot_61[2])**2))
arc_61_proposed = np.sum(np.sqrt(np.diff(x_smoothness[60])**2+np.diff(y_smoothness[60])**2+np.diff(z_smoothness[60])**2))

arc_62_current = np.sum(np.sqrt(np.diff(robot_62[0])**2+np.diff(robot_62[1])**2+np.diff(robot_62[2])**2))
arc_62_proposed = np.sum(np.sqrt(np.diff(x_smoothness[61])**2+np.diff(y_smoothness[61])**2+np.diff(z_smoothness[61])**2))

arc_63_current = np.sum(np.sqrt(np.diff(robot_63[0])**2+np.diff(robot_63[1])**2+np.diff(robot_63[2])**2))
arc_63_proposed = np.sum(np.sqrt(np.diff(x_smoothness[62])**2+np.diff(y_smoothness[62])**2+np.diff(z_smoothness[62])**2))

arc_64_current = np.sum(np.sqrt(np.diff(robot_64[0])**2+np.diff(robot_64[1])**2+np.diff(robot_64[2])**2))
arc_64_proposed = np.sum(np.sqrt(np.diff(x_smoothness[63])**2+np.diff(y_smoothness[63])**2+np.diff(z_smoothness[63])**2))



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


arc_mean_proposed_1 =  np.hstack(( arc_1_proposed, arc_2_proposed, arc_3_proposed, arc_4_proposed, arc_5_proposed, arc_6_proposed, arc_7_proposed, arc_8_proposed, arc_9_proposed, arc_10_proposed, arc_11_proposed, arc_12_proposed, arc_13_proposed, arc_14_proposed, arc_15_proposed, arc_16_proposed, arc_17_proposed, arc_18_proposed, arc_19_proposed, arc_20_proposed, arc_21_proposed, arc_22_proposed, arc_23_proposed, arc_24_proposed, arc_25_proposed, arc_26_proposed, arc_27_proposed, arc_28_proposed, arc_29_proposed, arc_30_proposed, arc_31_proposed, arc_32_proposed ))  
arc_mean_proposed_2 =  np.hstack(( arc_33_proposed, arc_34_proposed, arc_35_proposed, arc_36_proposed, arc_37_proposed, arc_38_proposed, arc_39_proposed, arc_40_proposed, arc_41_proposed, arc_42_proposed, arc_43_proposed, arc_44_proposed, arc_45_proposed, arc_46_proposed, arc_47_proposed, arc_48_proposed, arc_49_proposed, arc_50_proposed, arc_51_proposed, arc_52_proposed, arc_53_proposed, arc_54_proposed, arc_55_proposed, arc_56_proposed, arc_57_proposed, arc_58_proposed, arc_59_proposed, arc_60_proposed, arc_61_proposed, arc_62_proposed, arc_63_proposed, arc_64_proposed ))  
arc_mean_proposed = np.hstack((arc_mean_proposed_1, arc_mean_proposed_2)) 


arc_mean_current_1 = np.hstack(( arc_1_current, arc_2_current, arc_3_current, arc_4_current, arc_5_current, arc_6_current, arc_7_current, arc_8_current, arc_9_current, arc_10_current, arc_11_current, arc_12_current, arc_13_current, arc_14_current, arc_15_current, arc_16_current, arc_17_current, arc_18_current, arc_19_current, arc_20_current, arc_21_current, arc_22_current, arc_23_current, arc_24_current, arc_25_current, arc_26_current, arc_27_current, arc_28_current, arc_29_current, arc_30_current, arc_31_current, arc_32_current ))  
arc_mean_current_2 =  np.hstack(( arc_33_current, arc_34_current, arc_35_current, arc_36_current, arc_37_current, arc_38_current, arc_39_current, arc_40_current, arc_41_current, arc_42_current, arc_43_current, arc_44_current, arc_45_current, arc_46_current, arc_47_current, arc_48_current, arc_49_current, arc_50_current, arc_51_current, arc_52_current, arc_53_current, arc_54_current, arc_55_current, arc_56_current, arc_57_current, arc_58_current, arc_59_current, arc_60_current, arc_61_current, arc_62_current, arc_63_current, arc_64_current ))  
arc_mean_current =  np.hstack(( arc_mean_current_1, arc_mean_current_2))  

print(arc_mean_proposed, arc_mean_current)


arc_mean_prop_64robot_12 = arc_mean_proposed
arc_mean_curr_64robot_12 = arc_mean_current

scipy.io.savemat('arc_mean_prop_64robot_12.mat', {'arc_mean_prop_64robot_12': arc_mean_prop_64robot_12})
scipy.io.savemat('arc_mean_curr_64robot_12.mat', {'arc_mean_curr_64robot_12': arc_mean_curr_64robot_12})









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
ax.plot(x[32],y[32],z[32], color ='darkslategrey',linewidth = 3.0)
ax.plot(x[33],y[33],z[33], color ='yellowgreen', linewidth = 3.0)
ax.plot(x[34],y[34],z[34], color ='tomato', linewidth = 3.0)
ax.plot(x[35],y[35],z[35], color ='peachpuff', linewidth = 3.0)
ax.plot(x[36],y[36],z[36], color ='lightgreen', linewidth = 3.0)
ax.plot(x[37],y[37],z[37], color ='darkviolet', linewidth = 3.0)
ax.plot(x[38],y[38],z[38], color ='powderblue', linewidth = 3.0)
ax.plot(x[39],y[39],z[39], color ='hotpink', linewidth = 3.0)
ax.plot(x[40],y[40],z[40], color ='magenta', linewidth = 3.0)
ax.plot(x[41],y[41],z[41], color ='thistle', linewidth = 3.0)
ax.plot(x[42],y[42],z[42], color ='crimson', linewidth = 3.0)
ax.plot(x[43],y[43],z[43], color ='lightpink', linewidth = 3.0)
ax.plot(x[44],y[44],z[44], color ='plum', linewidth = 3.0)
ax.plot(x[45],y[45],z[45], color ='darkblue', linewidth = 3.0)
ax.plot(x[46],y[46],z[46], color ='slateblue', linewidth = 3.0)
ax.plot(x[47],y[47],z[47], color ='royalblue', linewidth = 3.0)
ax.plot(x[48],y[48],z[48], color ='slategrey', linewidth = 3.0)
ax.plot(x[49],y[49],z[49], color ='forestgreen', linewidth = 3.0)
ax.plot(x[50],y[50],z[50], color ='turquoise', linewidth = 3.0)
ax.plot(x[51],y[51],z[51], color ='dodgerblue', linewidth = 3.0)
ax.plot(x[52],y[52],z[52], color ='sandybrown', linewidth = 3.0)
ax.plot(x[53],y[53],z[53], color ='sienna', linewidth = 3.0)
ax.plot(x[54],y[54],z[54], color ='coral', linewidth = 3.0)
ax.plot(x[55],y[55],z[55], color ='darkred', linewidth = 3.0)
ax.plot(x[56],y[56],z[56], color ='firebrick', linewidth = 3.0)
ax.plot(x[57],y[57],z[57], color ='rosybrown', linewidth = 3.0)
ax.plot(x[58],y[58],z[58], color ='darkorange', linewidth = 3.0)
ax.plot(x[59],y[59],z[59], color ='tan', linewidth = 3.0)
ax.plot(x[60],y[60],z[60], color ='darkkhaki', linewidth = 3.0)
ax.plot(x[61],y[61],z[61], color ='olivedrab', linewidth = 3.0)
ax.plot(x[62],y[62],z[62], color ='palegreen', linewidth = 3.0)
ax.plot(x[63],y[63],z[63], color ='lightgreen',linewidth = 3.0)



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
ax.plot(robot_33[0,:], robot_33[1,:], robot_33[2,:], '--r', linewidth = 2.0)
ax.plot(robot_34[0,:], robot_34[1,:], robot_34[2,:], '--', color = 'pink', linewidth = 2.0)
ax.plot(robot_35[0,:], robot_35[1,:], robot_35[2,:], '--', color = 'orange', linewidth = 2.0)
ax.plot(robot_36[0,:], robot_36[1,:], robot_36[2,:], '--', color = 'green', linewidth = 2.0)
ax.plot(robot_37[0,:], robot_37[1,:], robot_37[2,:], '--', color = 'grey', linewidth = 2.0)
ax.plot(robot_38[0,:], robot_38[1,:], robot_38[2,:], '--', color = 'black', linewidth = 2.0)
ax.plot(robot_39[0,:], robot_39[1,:], robot_39[2,:], '--', color = 'yellow', linewidth = 2.0)
ax.plot(robot_40[0,:], robot_40[1,:], robot_40[2,:], '--', color = 'purple', linewidth = 2.0)
ax.plot(robot_41[0,:], robot_41[1,:], robot_41[2,:], '--', color = 'darkgreen', linewidth = 2.0)
ax.plot(robot_42[0,:], robot_42[1,:], robot_42[2,:], '--', color = 'teal', linewidth = 2.0)
ax.plot(robot_43[0,:], robot_43[1,:], robot_43[2,:], '--', color = 'salmon', linewidth = 2.0)
ax.plot(robot_44[0,:], robot_44[1,:], robot_44[2,:], '--', color = 'black', linewidth = 2.0)
ax.plot(robot_45[0,:], robot_45[1,:], robot_45[2,:], '--', color = 'cyan', linewidth = 2.0)
ax.plot(robot_46[0,:], robot_46[1,:], robot_46[2,:], '--', color = 'brown', linewidth = 2.0)
ax.plot(robot_47[0,:], robot_47[1,:], robot_47[2,:], '--', color = 'coral', linewidth = 2.0)
ax.plot(robot_48[0,:], robot_48[1,:], robot_48[2,:], '--', color = 'lime', linewidth = 2.0)
ax.plot(robot_49[0,:], robot_49[1,:], robot_49[2,:], '--r', linewidth = 2.0)
ax.plot(robot_50[0,:], robot_50[1,:], robot_50[2,:], '--', color = 'pink', linewidth = 2.0)
ax.plot(robot_51[0,:], robot_51[1,:], robot_51[2,:], '--', color = 'orange', linewidth = 2.0)
ax.plot(robot_52[0,:], robot_52[1,:], robot_52[2,:], '--', color = 'green', linewidth = 2.0)
ax.plot(robot_53[0,:], robot_53[1,:], robot_53[2,:], '--', color = 'grey', linewidth = 2.0)
ax.plot(robot_54[0,:], robot_54[1,:], robot_54[2,:], '--', color = 'black', linewidth = 2.0)
ax.plot(robot_55[0,:], robot_55[1,:], robot_55[2,:], '--', color = 'yellow', linewidth = 2.0)
ax.plot(robot_56[0,:], robot_56[1,:], robot_56[2,:], '--', color = 'purple', linewidth = 2.0)
ax.plot(robot_57[0,:], robot_57[1,:], robot_57[2,:], '--', color = 'darkgreen', linewidth = 2.0)
ax.plot(robot_58[0,:], robot_58[1,:], robot_58[2,:], '--', color = 'teal', linewidth = 2.0)
ax.plot(robot_59[0,:], robot_59[1,:], robot_59[2,:], '--', color = 'salmon', linewidth = 2.0)
ax.plot(robot_60[0,:], robot_60[1,:], robot_60[2,:], '--', color = 'black', linewidth = 2.0)
ax.plot(robot_61[0,:], robot_61[1,:], robot_61[2,:], '--', color = 'cyan', linewidth = 2.0)
ax.plot(robot_62[0,:], robot_62[1,:], robot_62[2,:], '--', color = 'brown', linewidth = 2.0)
ax.plot(robot_63[0,:], robot_63[1,:], robot_63[2,:], '--', color = 'coral', linewidth = 2.0)
ax.plot(robot_64[0,:], robot_64[1,:], robot_64[2,:], '--', color = 'lime', linewidth = 2.0)



# plt.axis('equal')

plt.show()
