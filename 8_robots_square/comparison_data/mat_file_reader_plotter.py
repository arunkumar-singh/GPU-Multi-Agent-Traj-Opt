#!/usr/bin/env python

# import rospy
# from std_msgs.msg import String
# from nav_msgs.msg import Path


import numpy as np
from scipy.io import loadmat
import matplotlib.pyplot as plt
from scipy.io import loadmat
import scipy.io
from scipy.interpolate import RegularGridInterpolator as rgi
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



############################## Loadng the trajectories from the proposed code



x_temp = scipy.io.loadmat('x_1.mat')
x = x_temp['x_1'].squeeze()

y_temp = scipy.io.loadmat('y_1.mat')
y = y_temp['y_1'].squeeze()

z_temp = scipy.io.loadmat('z_1.mat')
z = z_temp['z_1'].squeeze()
#################################smoothness comparison############
x_smoothness = x
y_smoothness = y
z_smoothness = z



robot_1 = np.delete(robot_1[:,::2],50,1)
robot_2 = np.delete(robot_2[:,::2],50,1)
robot_3 = np.delete(robot_3[:,::2],50,1)
robot_4 = np.delete(robot_4[:,::2],50,1)
robot_5 = np.delete(robot_5[:,::2],50,1)
robot_6 = np.delete(robot_6[:,::2],50,1)
robot_7 = np.delete(robot_7[:,::2],50,1)
robot_8 = np.delete(robot_8[:,::2],50,1)

print(np.shape(robot_1))
#print(np.shape(x_smoothness))

#x_robot = np.vstack((robot_1[0], robot_2[0], robot_3[0], robot_4[0], robot_5[0], robot_6[0], robot_7[0], robot_8[0], robot_9[0], robot_10[0], robot_11[0], robot_12[0], robot_13[0], robot_14[0], robot_15[0], robot_16[0]))
#y_robot = np.vstack((robot_1[1], robot_2[1], robot_3[1], robot_4[1], robot_5[1], robot_6[1], robot_7[1], robot_8[1], robot_9[1], robot_10[1], robot_11[1], robot_12[1], robot_13[1], robot_14[1], robot_15[1], robot_16[1]))
#z_robot = np.vstack((robot_1[2], robot_2[2], robot_3[2], robot_4[2], robot_5[2], robot_6[2], robot_7[2], robot_8[2], robot_9[2], robot_10[2], robot_11[2], robot_12[2], robot_13[2], robot_14[2], robot_15[2], robot_16[2]))



#print(np.shape(x_robot))
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




#cost_smoothness_prop_16rob_30 = np.linalg.norm(np.diff(np.diff(x_smoothness)))+np.linalg.norm(np.diff(np.diff(y_smoothness)))+np.linalg.norm(np.diff(np.diff(z_smoothness)))
#cost_smoothness_curr_16rob_30 = np.linalg.norm(np.diff(np.diff(x_robot)))+np.linalg.norm(np.diff(np.diff(y_robot)))+np.linalg.norm(np.diff(np.diff(z_robot)))

cost_smoothness_prop_8rob_15 = np.hstack((cost_smoothness_prop_1, cost_smoothness_prop_2, cost_smoothness_prop_3, cost_smoothness_prop_4, cost_smoothness_prop_5, cost_smoothness_prop_6, cost_smoothness_prop_7, cost_smoothness_prop_8))
cost_smoothness_curr_8rob_15 = np.hstack((cost_smoothness_curr_1, cost_smoothness_curr_2, cost_smoothness_curr_3, cost_smoothness_curr_4, cost_smoothness_curr_5, cost_smoothness_curr_6, cost_smoothness_curr_7, cost_smoothness_curr_8))

scipy.io.savemat('cost_smoothness_prop_8rob_15.mat', {'cost_smoothness_prop_8rob_15': cost_smoothness_prop_8rob_15})
scipy.io.savemat('cost_smoothness_curr_8rob_15.mat', {'cost_smoothness_curr_8rob_15': cost_smoothness_curr_8rob_15})

print(cost_smoothness_prop_8rob_15)
print(cost_smoothness_curr_8rob_15)
#################################################
arc_1_current = np.sum(np.sqrt(np.diff(robot_1[0])**2+np.diff(robot_1[1])**2+np.diff(robot_1[2])**2))
arc_1_proposed = np.sum(np.sqrt(np.diff(x[0])**2+np.diff(y[0])**2+np.diff(z[0])**2))

arc_2_current = np.sum(np.sqrt(np.diff(robot_2[0])**2+np.diff(robot_2[1])**2+np.diff(robot_2[2])**2))
arc_2_proposed = np.sum(np.sqrt(np.diff(x[1])**2+np.diff(y[1])**2+np.diff(z[1])**2))


arc_3_current = np.sum(np.sqrt(np.diff(robot_3[0])**2+np.diff(robot_3[1])**2+np.diff(robot_3[2])**2))
arc_3_proposed = np.sum(np.sqrt(np.diff(x[2])**2+np.diff(y[2])**2+np.diff(z[2])**2))


arc_4_current = np.sum(np.sqrt(np.diff(robot_4[0])**2+np.diff(robot_4[1])**2+np.diff(robot_4[2])**2))
arc_4_proposed = np.sum(np.sqrt(np.diff(x[3])**2+np.diff(y[3])**2+np.diff(z[3])**2))


arc_5_current = np.sum(np.sqrt(np.diff(robot_5[0])**2+np.diff(robot_5[1])**2+np.diff(robot_5[2])**2))
arc_5_proposed = np.sum(np.sqrt(np.diff(x[4])**2+np.diff(y[4])**2+np.diff(z[4])**2))

arc_6_current = np.sum(np.sqrt(np.diff(robot_6[0])**2+np.diff(robot_6[1])**2+np.diff(robot_6[2])**2))
arc_6_proposed = np.sum(np.sqrt(np.diff(x[5])**2+np.diff(y[5])**2+np.diff(z[5])**2))

arc_7_current = np.sum(np.sqrt(np.diff(robot_7[0])**2+np.diff(robot_7[1])**2+np.diff(robot_7[2])**2))
arc_7_proposed = np.sum(np.sqrt(np.diff(x[6])**2+np.diff(y[6])**2+np.diff(z[6])**2))

arc_8_current = np.sum(np.sqrt(np.diff(robot_8[0])**2+np.diff(robot_8[1])**2+np.diff(robot_8[2])**2))
arc_8_proposed = np.sum(np.sqrt(np.diff(x[7])**2+np.diff(y[7])**2+np.diff(z[7])**2))








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


arc_mean_proposed =  np.hstack(( arc_1_proposed, arc_2_proposed, arc_3_proposed, arc_4_proposed, arc_5_proposed, arc_6_proposed, arc_7_proposed, arc_8_proposed))  
arc_mean_current = np.hstack(( arc_1_current, arc_2_current, arc_3_current, arc_4_current, arc_5_current, arc_6_current, arc_7_current, arc_8_current ))  


arc_mean_prop_8robot_15 = arc_mean_proposed
arc_mean_curr_8robot_15 = arc_mean_current

scipy.io.savemat('arc_mean_prop_8robot_15.mat', {'arc_mean_prop_8robot_15': arc_mean_prop_8robot_15})
scipy.io.savemat('arc_mean_curr_8robot_15.mat', {'arc_mean_curr_8robot_15': arc_mean_curr_8robot_15})

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



ax.plot(robot_1[0,:], robot_1[1,:], robot_1[2,:], '--r', linewidth = 2.0)
ax.plot(robot_2[0,:], robot_2[1,:], robot_2[2,:], '--', color = 'pink', linewidth = 2.0)
ax.plot(robot_3[0,:], robot_3[1,:], robot_3[2,:], '--', color = 'orange', linewidth = 2.0)
ax.plot(robot_4[0,:], robot_4[1,:], robot_4[2,:], '--', color = 'green', linewidth = 2.0)
ax.plot(robot_5[0,:], robot_5[1,:], robot_5[2,:], '--', color = 'grey', linewidth = 2.0)
ax.plot(robot_6[0,:], robot_6[1,:], robot_6[2,:], '--', color = 'black', linewidth = 2.0)
ax.plot(robot_7[0,:], robot_7[1,:], robot_7[2,:], '--', color = 'yellow', linewidth = 2.0)
ax.plot(robot_8[0,:], robot_8[1,:], robot_8[2,:], '--', color = 'purple', linewidth = 2.0)



# plt.axis('equal')

plt.show()
