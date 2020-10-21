
from numpy import *
import matplotlib.pyplot as plt
import scipy.special
from scipy import interpolate
from scipy.io import loadmat
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import points


matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

plt.rcParams.update({'font.size': 15})



x_temp = scipy.io.loadmat('x_1.mat')
x = x_temp['x_1'].squeeze()

y_temp = scipy.io.loadmat('y_1.mat')
y = y_temp['y_1'].squeeze()

z_temp = scipy.io.loadmat('z_1.mat')
z = z_temp['z_1'].squeeze()


######################obstacles###############
points_x_init_obs, points_y_init_obs, points_z_init_obs = points.obstacles_positions()

num_horizon = 100
n_d = 8

a_elipse_old = 0.5
b_elipse_old = 0.5
c_elipse_old = 0.5

a_elipse = 0.5*(2/sqrt(3))*a_elipse_old
b_elipse = 0.5*(2/sqrt(3))*b_elipse_old
c_elipse = 0.5*(2/sqrt(3))*c_elipse_old

x_centre = points_x_init_obs
y_centre = points_y_init_obs
z_centre = points_z_init_obs

center_1 = hstack((x_centre[0],y_centre[0],z_centre[0]))
center_2 = hstack((x_centre[1],y_centre[1],z_centre[1]))
center_3 = hstack((x_centre[2],y_centre[2],z_centre[2]))
center_4 = hstack((x_centre[3],y_centre[3],z_centre[3]))
center_5 = hstack((x_centre[4],y_centre[4],z_centre[4]))
center_6 = hstack((x_centre[5],y_centre[5],z_centre[5]))
center_7 = hstack((x_centre[6],y_centre[6],z_centre[6]))
center_8 = hstack((x_centre[7],y_centre[7],z_centre[7]))


##########################plot obstacles

def plot_cuboid(center, size):

    ox, oy, oz = center
    l, w, h = size

    x = linspace(ox-l/2,ox+l/2,num=10)
    y = linspace(oy-w/2,oy+w/2,num=10)
    z = linspace(oz-h/2,oz+h/2,num=10)
    x1, z1 = meshgrid(x, z)
    y11 = ones_like(x1)*(oy-w/2)
    y12 = ones_like(x1)*(oy+w/2)
    x2, y2 = meshgrid(x, y)
    z21 = ones_like(x2)*(oz-h/2)
    z22 = ones_like(x2)*(oz+h/2)
    y3, z3 = meshgrid(y, z)
    x31 = ones_like(y3)*(ox-l/2)
    x32 = ones_like(y3)*(ox+l/2)
    ax.plot_surface(x1, y11, z1, color='lightblue', rstride=1, cstride=1,  alpha=0.8)
    ax.plot_surface(x1, y12, z1, color='lightblue', rstride=1, cstride=1, alpha=0.8)
    ax.plot_surface(x2, y2, z21, color='lightblue', rstride=1, cstride=1, alpha=0.8)
    ax.plot_surface(x2, y2, z22, color='lightblue', rstride=1, cstride=1, alpha=0.8)
    ax.plot_surface(x31, y3, z3, color='lightblue', rstride=1, cstride=1, alpha=0.8)
    ax.plot_surface(x32, y3, z3, color='lightblue', rstride=1, cstride=1, alpha=0.8)
    ax.set_zlim(0.5, 1.2)

##########################################


fig = plt.figure(figsize=plt.figaspect(1))
ax = fig.add_subplot(111, projection='3d')

plot_cuboid(center_1, (a_elipse, b_elipse, c_elipse))
plot_cuboid(center_2, (a_elipse, b_elipse, c_elipse))
plot_cuboid(center_3, (a_elipse, b_elipse, c_elipse))
plot_cuboid(center_4, (a_elipse, b_elipse, c_elipse))
plot_cuboid(center_5, (a_elipse, b_elipse, c_elipse))
plot_cuboid(center_6, (a_elipse, b_elipse, c_elipse))
plot_cuboid(center_7, (a_elipse, b_elipse, c_elipse))
plot_cuboid(center_8, (a_elipse, b_elipse, c_elipse))



ax.plot(x[0],y[0],z[0], '-r', linewidth = 3.0)
ax.plot(x[1],y[1],z[1], color ='pink', linewidth = 3.0)
ax.plot(x[2],y[2],z[2], color ='orange', linewidth = 3.0)
ax.plot(x[3],y[3],z[3], color ='green', linewidth = 3.0)
ax.plot(x[4],y[4],z[4], color ='grey', linewidth = 3.0)
ax.plot(x[5],y[5],z[5], color ='navy', linewidth = 3.0)
ax.plot(x[6],y[6],z[6], color ='yellow', linewidth = 3.0)
ax.plot(x[7],y[7],z[7], color ='purple', linewidth = 3.0)
ax.plot(x[8],y[8],z[8], color ='darkgreen', linewidth = 3.0)
ax.plot(x[9],y[9],z[9], color ='teal', linewidth = 3.0)
ax.plot(x[10],y[10],z[10], color ='salmon', linewidth = 3.0)
ax.plot(x[11],y[11],z[11], color ='black', linewidth = 3.0)
ax.plot(x[12],y[12],z[12], color ='cyan', linewidth = 3.0)
ax.plot(x[13],y[13],z[13], color ='brown', linewidth = 3.0)
ax.plot(x[14],y[14],z[14], color ='coral', linewidth = 3.0)
ax.plot(x[15],y[15],z[15], color ='lime', linewidth = 3.0)
ax.scatter3D(x[0,0], y[0,0], z[0,0], s=13**2,color = "red", marker ="x") 
ax.scatter3D(x[1,0], y[1,0], z[1,0], s=13**2,color = "pink", marker ="x") 
ax.scatter3D(x[2,0], y[2,0], z[2,0], s=13**2,color = "orange", marker ="x") 
ax.scatter3D(x[3,0], y[3,0], z[3,0], s=13**2,color = "green", marker ="x") 
ax.scatter3D(x[4,0], y[4,0], z[4,0], s=13**2,color = "grey", marker ="x") 
ax.scatter3D(x[5,0], y[5,0], z[5,0], s=13**2,color = "navy", marker ="x") 
ax.scatter3D(x[6,0], y[6,0], z[6,0], s=13**2,color = "yellow", marker ="x") 
ax.scatter3D(x[7,0], y[7,0], z[7,0], s=13**2,color = "purple", marker ="x") 
ax.scatter3D(x[8,0], y[8,0], z[8,0], s=13**2,color = "darkgreen", marker ="x") 
ax.scatter3D(x[9,0], y[9,0], z[9,0], s=13**2,color = "teal", marker ="x") 
ax.scatter3D(x[10,0], y[10,0], z[10,0],s=13**2, color = "salmon", marker ="x") 
ax.scatter3D(x[11,0], y[11,0], z[11,0],s=13**2, color = "black", marker ="x") 
ax.scatter3D(x[12,0], y[12,0], z[12,0],s=13**2, color = "cyan", marker ="x") 
ax.scatter3D(x[13,0], y[13,0], z[13,0],s=13**2, color = "brown", marker ="x") 
ax.scatter3D(x[14,0], y[14,0], z[14,0],s=13**2, color = "coral", marker ="x") 
ax.scatter3D(x[15,0], y[15,0], z[15,0],s=13**2, color = "lime", marker ="x") 
ax.scatter3D(x[0,-1], y[0,-1], z[0,-1],s=8**2, color = "red") 
ax.scatter3D(x[1,-1], y[1,-1], z[1,-1],s=8**2, color = "pink") 
ax.scatter3D(x[2,-1], y[2,-1], z[2,-1],s=8**2, color = "orange") 
ax.scatter3D(x[3,-1], y[3,-1], z[3,-1],s=8**2, color = "green") 
ax.scatter3D(x[4,-1], y[4,-1], z[4,-1],s=8**2, color = "grey") 
ax.scatter3D(x[5,-1], y[5,-1], z[5,-1],s=8**2, color = "navy") 
ax.scatter3D(x[6,-1], y[6,-1], z[6,-1],s=8**2, color = "yellow") 
ax.scatter3D(x[7,-1], y[7,-1], z[7,-1],s=8**2, color = "purple") 
ax.scatter3D(x[8,-1], y[8,-1], z[8,-1],s=8**2, color = "darkgreen") 
ax.scatter3D(x[9,-1], y[9,-1], z[9,-1],s=8**2, color = "teal") 
ax.scatter3D(x[10,-1], y[10,-1], z[10,-1],s=8**2, color = "salmon") 
ax.scatter3D(x[11,-1], y[11,-1], z[11,-1],s=8**2, color = "black") 
ax.scatter3D(x[12,-1], y[12,-1], z[12,-1],s=8**2, color = "cyan") 
ax.scatter3D(x[13,-1], y[13,-1], z[13,-1],s=8**2, color = "brown") 
ax.scatter3D(x[14,-1], y[14,-1], z[14,-1],s=8**2, color = "coral") 
ax.scatter3D(x[15,-1], y[15,-1], z[15,-1],s=8**2, color = "lime") 
ax.set_xlabel('x[m]', fontweight ='bold')  
ax.set_ylabel('y[m]', fontweight ='bold')  
ax.set_zlabel('z[m]', fontweight ='bold') 

plt.show()