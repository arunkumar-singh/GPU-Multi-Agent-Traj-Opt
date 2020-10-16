
from numpy import *
import matplotlib.pyplot as plt
import scipy.special
from scipy import interpolate
from scipy.io import loadmat
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
plt.rcParams.update({'font.size': 15})

#####################robots trajectories ###########################
x_temp = scipy.io.loadmat('x_1.mat')
x_1 = x_temp['x_1'].squeeze()

y_temp = scipy.io.loadmat('y_1.mat')
y_1 = y_temp['y_1'].squeeze()

z_temp = scipy.io.loadmat('z_1.mat')
z_1 = z_temp['z_1'].squeeze()




###############ploting ####################

fig = plt.figure(figsize=plt.figaspect(1))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_1[0],y_1[0],z_1[0], '-r', linewidth = 3.0)
ax.plot(x_1[1],y_1[1],z_1[1], color ='pink', linewidth = 3.0)
ax.plot(x_1[2],y_1[2],z_1[2], color ='orange', linewidth = 3.0)
ax.plot(x_1[3],y_1[3],z_1[3], color ='green', linewidth = 3.0)
ax.plot(x_1[4],y_1[4],z_1[4], color ='grey', linewidth = 3.0)
ax.plot(x_1[5],y_1[5],z_1[5], color ='navy', linewidth = 3.0)
ax.plot(x_1[6],y_1[6],z_1[6], color ='yellow', linewidth = 3.0)
ax.plot(x_1[7],y_1[7],z_1[7], color ='purple', linewidth = 3.0)

ax.scatter3D(x_1[0,0], y_1[0,0], z_1[0,0], s=13**2,color = "red", marker ="x") 
ax.scatter3D(x_1[1,0], y_1[1,0], z_1[1,0], s=13**2,color = "pink", marker ="x") 
ax.scatter3D(x_1[2,0], y_1[2,0], z_1[2,0], s=13**2,color = "orange", marker ="x") 
ax.scatter3D(x_1[3,0], y_1[3,0], z_1[3,0], s=13**2,color = "green", marker ="x") 
ax.scatter3D(x_1[4,0], y_1[4,0], z_1[4,0], s=13**2,color = "grey", marker ="x") 
ax.scatter3D(x_1[5,0], y_1[5,0], z_1[5,0], s=13**2,color = "navy", marker ="x") 
ax.scatter3D(x_1[6,0], y_1[6,0], z_1[6,0], s=13**2,color = "yellow", marker ="x") 
ax.scatter3D(x_1[7,0], y_1[7,0], z_1[7,0], s=13**2,color = "purple", marker ="x") 

ax.scatter3D(x_1[0,-1], y_1[0,-1], z_1[0,-1],s=8**2, color = "red") 
ax.scatter3D(x_1[1,-1], y_1[1,-1], z_1[1,-1],s=8**2, color = "pink") 
ax.scatter3D(x_1[2,-1], y_1[2,-1], z_1[2,-1],s=8**2, color = "orange") 
ax.scatter3D(x_1[3,-1], y_1[3,-1], z_1[3,-1],s=8**2, color = "green") 
ax.scatter3D(x_1[4,-1], y_1[4,-1], z_1[4,-1],s=8**2, color = "grey") 
ax.scatter3D(x_1[5,-1], y_1[5,-1], z_1[5,-1],s=8**2, color = "navy") 
ax.scatter3D(x_1[6,-1], y_1[6,-1], z_1[6,-1],s=8**2, color = "yellow") 
ax.scatter3D(x_1[7,-1], y_1[7,-1], z_1[7,-1],s=8**2, color = "purple") 

ax.set_xlabel('x[m]', fontweight ='bold')  
ax.set_ylabel('y[m]', fontweight ='bold')  
ax.set_zlabel('z[m]', fontweight ='bold') 
ax.text2D(0.05, 0.95, "r=0.15", transform=ax.transAxes)




plt.show()