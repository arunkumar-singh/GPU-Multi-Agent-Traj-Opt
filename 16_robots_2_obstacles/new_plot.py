
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

###########################################

points_x_init_obs_1 = hstack((0,0))
points_y_init_obs_1 = hstack((-5,5))
points_z_init_obs_1 = hstack((2,2))

points_x_init_obs_2 = hstack((0,0))
points_y_init_obs_2 = hstack((-5,5))
points_z_init_obs_2 = hstack((2,2))

points_x_init_obs_3 = hstack((0,0))
points_y_init_obs_3 = hstack((-5,5))
points_z_init_obs_3 = hstack((2,2))

points_x_init_obs_4 = hstack((0,0))
points_y_init_obs_4 = hstack((-7,7))
points_z_init_obs_4 = hstack((2,2))

points_x_init_obs_5 = hstack((0,0))
points_y_init_obs_5 = hstack((-7,7))
points_z_init_obs_5 = hstack((2,2))


center_1 = hstack((points_x_init_obs_1[0],points_y_init_obs_1[0],points_z_init_obs_1[0]))
center_2 = hstack((points_x_init_obs_1[1],points_y_init_obs_1[1],points_z_init_obs_1[1]))
center_3 = hstack((points_x_init_obs_2[0],points_y_init_obs_2[0],points_z_init_obs_2[0]))
center_4 = hstack((points_x_init_obs_2[1],points_y_init_obs_2[1],points_z_init_obs_2[1]))
center_5 = hstack((points_x_init_obs_3[0],points_y_init_obs_3[0],points_z_init_obs_3[0]))
center_6 = hstack((points_x_init_obs_3[1],points_y_init_obs_3[1],points_z_init_obs_3[1]))
center_8 = hstack((points_x_init_obs_4[0],points_y_init_obs_4[0],points_z_init_obs_4[0]))
center_7 = hstack((points_x_init_obs_4[1],points_y_init_obs_4[1],points_z_init_obs_4[1]))
center_9 = hstack((points_x_init_obs_5[0],points_y_init_obs_5[0],points_z_init_obs_5[0]))
center_10 = hstack((points_x_init_obs_5[1],points_y_init_obs_5[1],points_z_init_obs_5[1]))
#######################################

a_elipse_1 = 4.0
b_elipse_1 = 4.0
c_elipse_1 = 4.0

a_elipse_2 = 5.0
b_elipse_2 = 5.0
c_elipse_2 = 5.0

a_elipse_3 = 5.0
b_elipse_3 = 5.0
c_elipse_3 = 5.0

a_elipse_4 = 6.0
b_elipse_4 = 6.0
c_elipse_4 = 6.0

a_elipse_5 = 6.0
b_elipse_5 = 6.0
c_elipse_5 = 6.0


a_elipse_1 = 0.5*(2/sqrt(3))*a_elipse_1
b_elipse_1 = 0.5*(2/sqrt(3))*b_elipse_1
c_elipse_1 = 0.5*(2/sqrt(3))*c_elipse_1

a_elipse_2 = 0.5*(2/sqrt(3))*a_elipse_2
b_elipse_2 = 0.5*(2/sqrt(3))*b_elipse_2
c_elipse_2 = 0.5*(2/sqrt(3))*c_elipse_2

a_elipse_3 = 0.5*(2/sqrt(3))*a_elipse_3
b_elipse_3 = 0.5*(2/sqrt(3))*b_elipse_3
c_elipse_3 = 0.5*(2/sqrt(3))*c_elipse_3

a_elipse_4 = 0.5*(2/sqrt(3))*a_elipse_4
b_elipse_4 = 0.5*(2/sqrt(3))*b_elipse_4
c_elipse_4 = 0.5*(2/sqrt(3))*c_elipse_4

a_elipse_5 = 0.5*(2/sqrt(3))*a_elipse_5
b_elipse_5 = 0.5*(2/sqrt(3))*b_elipse_5
c_elipse_5 = 0.5*(2/sqrt(3))*c_elipse_5

#####################robots trajectories ###########################
x_temp = scipy.io.loadmat('x_1.mat')
x_1 = x_temp['x_1'].squeeze()

y_temp = scipy.io.loadmat('y_1.mat')
y_1 = y_temp['y_1'].squeeze()

z_temp = scipy.io.loadmat('z_1.mat')
z_1 = z_temp['z_1'].squeeze()


x_temp = scipy.io.loadmat('x_2.mat')
x_2 = x_temp['x_2'].squeeze()

y_temp = scipy.io.loadmat('y_2.mat')
y_2 = y_temp['y_2'].squeeze()

z_temp = scipy.io.loadmat('z_2.mat')
z_2 = z_temp['z_2'].squeeze()


x_temp = scipy.io.loadmat('x_3.mat')
x_3 = x_temp['x_3'].squeeze()

y_temp = scipy.io.loadmat('y_3.mat')
y_3 = y_temp['y_3'].squeeze()

z_temp = scipy.io.loadmat('z_3.mat')
z_3 = z_temp['z_3'].squeeze()


x_temp = scipy.io.loadmat('x_4.mat')
x_4 = x_temp['x_4'].squeeze()

y_temp = scipy.io.loadmat('y_4.mat')
y_4 = y_temp['y_4'].squeeze()

z_temp = scipy.io.loadmat('z_4.mat')
z_4 = z_temp['z_4'].squeeze()


x_temp = scipy.io.loadmat('x_5.mat')
x_5 = x_temp['x_5'].squeeze()

y_temp = scipy.io.loadmat('y_5.mat')
y_5 = y_temp['y_5'].squeeze()

z_temp = scipy.io.loadmat('z_5.mat')
z_5 = z_temp['z_5'].squeeze()


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
    ax.plot_surface(x1, y11, z1, color='lightblue', rstride=1, cstride=1,  alpha=0.3)
    ax.plot_surface(x1, y12, z1, color='lightblue', rstride=1, cstride=1, alpha=0.3)
    ax.plot_surface(x2, y2, z21, color='lightblue', rstride=1, cstride=1, alpha=0.3)
    ax.plot_surface(x2, y2, z22, color='lightblue', rstride=1, cstride=1, alpha=0.3)
    ax.plot_surface(x31, y3, z3, color='lightblue', rstride=1, cstride=1, alpha=0.3)
    ax.plot_surface(x32, y3, z3, color='lightblue', rstride=1, cstride=1, alpha=0.3)

##########################################




#################ploting ####################

fig = plt.figure(figsize=plt.figaspect(1))
ax = fig.add_subplot(111, projection='3d')

plot_cuboid(center_1, (a_elipse_1, b_elipse_1, c_elipse_1))
plot_cuboid(center_2, (a_elipse_1, b_elipse_1, c_elipse_1))#


ax.plot(x_1[0],y_1[0],z_1[0], '-r', linewidth = 3.0)
ax.plot(x_1[1],y_1[1],z_1[1], color ='pink', linewidth = 3.0)
ax.plot(x_1[2],y_1[2],z_1[2], color ='orange', linewidth = 3.0)
ax.plot(x_1[3],y_1[3],z_1[3], color ='green', linewidth = 3.0)
ax.plot(x_1[4],y_1[4],z_1[4], color ='grey', linewidth = 3.0)
ax.plot(x_1[5],y_1[5],z_1[5], color ='navy', linewidth = 3.0)
ax.plot(x_1[6],y_1[6],z_1[6], color ='yellow', linewidth = 3.0)
ax.plot(x_1[7],y_1[7],z_1[7], color ='purple', linewidth = 3.0)
ax.plot(x_1[8],y_1[8],z_1[8], color ='darkgreen', linewidth = 3.0)
ax.plot(x_1[9],y_1[9],z_1[9], color ='teal', linewidth = 3.0)
ax.plot(x_1[10],y_1[10],z_1[10], color ='salmon', linewidth = 3.0)
ax.plot(x_1[11],y_1[11],z_1[11], color ='black', linewidth = 3.0)
ax.plot(x_1[12],y_1[12],z_1[12], color ='cyan', linewidth = 3.0)
ax.plot(x_1[13],y_1[13],z_1[13], color ='brown', linewidth = 3.0)
ax.plot(x_1[14],y_1[14],z_1[14], color ='coral', linewidth = 3.0)
ax.plot(x_1[15],y_1[15],z_1[15], color ='lime', linewidth = 3.0)
ax.scatter3D(x_1[0,0], y_1[0,0], z_1[0,0], s=13**2,color = "red", marker ="x") 
ax.scatter3D(x_1[1,0], y_1[1,0], z_1[1,0], s=13**2,color = "pink", marker ="x") 
ax.scatter3D(x_1[2,0], y_1[2,0], z_1[2,0], s=13**2,color = "orange", marker ="x") 
ax.scatter3D(x_1[3,0], y_1[3,0], z_1[3,0], s=13**2,color = "green", marker ="x") 
ax.scatter3D(x_1[4,0], y_1[4,0], z_1[4,0], s=13**2,color = "grey", marker ="x") 
ax.scatter3D(x_1[5,0], y_1[5,0], z_1[5,0], s=13**2,color = "navy", marker ="x") 
ax.scatter3D(x_1[6,0], y_1[6,0], z_1[6,0], s=13**2,color = "yellow", marker ="x") 
ax.scatter3D(x_1[7,0], y_1[7,0], z_1[7,0], s=13**2,color = "purple", marker ="x") 
ax.scatter3D(x_1[8,0], y_1[8,0], z_1[8,0], s=13**2,color = "darkgreen", marker ="x") 
ax.scatter3D(x_1[9,0], y_1[9,0], z_1[9,0], s=13**2,color = "teal", marker ="x") 
ax.scatter3D(x_1[10,0], y_1[10,0], z_1[10,0],s=13**2, color = "salmon", marker ="x") 
ax.scatter3D(x_1[11,0], y_1[11,0], z_1[11,0],s=13**2, color = "black", marker ="x") 
ax.scatter3D(x_1[12,0], y_1[12,0], z_1[12,0],s=13**2, color = "cyan", marker ="x") 
ax.scatter3D(x_1[13,0], y_1[13,0], z_1[13,0],s=13**2, color = "brown", marker ="x") 
ax.scatter3D(x_1[14,0], y_1[14,0], z_1[14,0],s=13**2, color = "coral", marker ="x") 
ax.scatter3D(x_1[15,0], y_1[15,0], z_1[15,0],s=13**2, color = "lime", marker ="x") 
ax.scatter3D(x_1[0,-1], y_1[0,-1], z_1[0,-1],s=8**2, color = "red") 
ax.scatter3D(x_1[1,-1], y_1[1,-1], z_1[1,-1],s=8**2, color = "pink") 
ax.scatter3D(x_1[2,-1], y_1[2,-1], z_1[2,-1],s=8**2, color = "orange") 
ax.scatter3D(x_1[3,-1], y_1[3,-1], z_1[3,-1],s=8**2, color = "green") 
ax.scatter3D(x_1[4,-1], y_1[4,-1], z_1[4,-1],s=8**2, color = "grey") 
ax.scatter3D(x_1[5,-1], y_1[5,-1], z_1[5,-1],s=8**2, color = "navy") 
ax.scatter3D(x_1[6,-1], y_1[6,-1], z_1[6,-1],s=8**2, color = "yellow") 
ax.scatter3D(x_1[7,-1], y_1[7,-1], z_1[7,-1],s=8**2, color = "purple") 
ax.scatter3D(x_1[8,-1], y_1[8,-1], z_1[8,-1],s=8**2, color = "darkgreen") 
ax.scatter3D(x_1[9,-1], y_1[9,-1], z_1[9,-1],s=8**2, color = "teal") 
ax.scatter3D(x_1[10,-1], y_1[10,-1], z_1[10,-1],s=8**2, color = "salmon") 
ax.scatter3D(x_1[11,-1], y_1[11,-1], z_1[11,-1],s=8**2, color = "black") 
ax.scatter3D(x_1[12,-1], y_1[12,-1], z_1[12,-1],s=8**2, color = "cyan") 
ax.scatter3D(x_1[13,-1], y_1[13,-1], z_1[13,-1],s=8**2, color = "brown") 
ax.scatter3D(x_1[14,-1], y_1[14,-1], z_1[14,-1],s=8**2, color = "coral") 
ax.scatter3D(x_1[15,-1], y_1[15,-1], z_1[15,-1],s=8**2, color = "lime") 
ax.set_xlabel('x[m]', fontweight ='bold')  
ax.set_ylabel('y[m]', fontweight ='bold')  
ax.set_zlabel('z[m]', fontweight ='bold') 
#ax.text2D(0.05, 0.95, "r=0.25", transform=ax.transAxes)



fig = plt.figure(figsize=plt.figaspect(1))
ax = fig.add_subplot(111, projection='3d')

plot_cuboid(center_3, (a_elipse_2, b_elipse_2, c_elipse_2))
plot_cuboid(center_4, (a_elipse_2, b_elipse_2, c_elipse_2))


ax.plot(x_2[0],y_2[0],z_2[0], '-r', linewidth = 3.0)
ax.plot(x_2[1],y_2[1],z_2[1], color ='pink', linewidth = 3.0)
ax.plot(x_2[2],y_2[2],z_2[2], color ='orange', linewidth = 3.0)
ax.plot(x_2[3],y_2[3],z_2[3], color ='green', linewidth = 3.0)
ax.plot(x_2[4],y_2[4],z_2[4], color ='grey', linewidth = 3.0)
ax.plot(x_2[5],y_2[5],z_2[5], color ='navy', linewidth = 3.0)
ax.plot(x_2[6],y_2[6],z_2[6], color ='yellow', linewidth = 3.0)
ax.plot(x_2[7],y_2[7],z_2[7], color ='purple', linewidth = 3.0)
ax.plot(x_2[8],y_2[8],z_2[8], color ='darkgreen', linewidth = 3.0)
ax.plot(x_2[9],y_2[9],z_2[9], color ='teal', linewidth = 3.0)
ax.plot(x_2[10],y_2[10],z_2[10], color ='salmon', linewidth = 3.0)
ax.plot(x_2[11],y_2[11],z_2[11], color ='black', linewidth = 3.0)
ax.plot(x_2[12],y_2[12],z_2[12], color ='cyan', linewidth = 3.0)
ax.plot(x_2[13],y_2[13],z_2[13], color ='brown', linewidth = 3.0)
ax.plot(x_2[14],y_2[14],z_2[14], color ='coral', linewidth = 3.0)
ax.plot(x_2[15],y_2[15],z_2[15], color ='lime', linewidth = 3.0)
ax.scatter3D(x_2[0,0], y_2[0,0], z_2[0,0], s=13**2,color = "red", marker ="x") 
ax.scatter3D(x_2[1,0], y_2[1,0], z_2[1,0], s=13**2,color = "pink", marker ="x") 
ax.scatter3D(x_2[2,0], y_2[2,0], z_2[2,0], s=13**2,color = "orange", marker ="x") 
ax.scatter3D(x_2[3,0], y_2[3,0], z_2[3,0], s=13**2,color = "green", marker ="x") 
ax.scatter3D(x_2[4,0], y_2[4,0], z_2[4,0], s=13**2,color = "grey", marker ="x") 
ax.scatter3D(x_2[5,0], y_2[5,0], z_2[5,0], s=13**2,color = "navy", marker ="x") 
ax.scatter3D(x_2[6,0], y_2[6,0], z_2[6,0], s=13**2,color = "yellow", marker ="x") 
ax.scatter3D(x_2[7,0], y_2[7,0], z_2[7,0], s=13**2,color = "purple", marker ="x") 
ax.scatter3D(x_2[8,0], y_2[8,0], z_2[8,0], s=13**2,color = "darkgreen", marker ="x") 
ax.scatter3D(x_2[9,0], y_2[9,0], z_2[9,0], s=13**2,color = "teal", marker ="x") 
ax.scatter3D(x_2[10,0], y_2[10,0], z_2[10,0],s=13**2, color = "salmon", marker ="x") 
ax.scatter3D(x_2[11,0], y_2[11,0], z_2[11,0],s=13**2, color = "black", marker ="x") 
ax.scatter3D(x_2[12,0], y_2[12,0], z_2[12,0],s=13**2, color = "cyan", marker ="x") 
ax.scatter3D(x_2[13,0], y_2[13,0], z_2[13,0],s=13**2, color = "brown", marker ="x") 
ax.scatter3D(x_2[14,0], y_2[14,0], z_2[14,0],s=13**2, color = "coral", marker ="x") 
ax.scatter3D(x_2[15,0], y_2[15,0], z_2[15,0],s=13**2, color = "lime", marker ="x") 
ax.scatter3D(x_2[0,-1], y_2[0,-1], z_2[0,-1],s=8**2, color = "red") 
ax.scatter3D(x_2[1,-1], y_2[1,-1], z_2[1,-1],s=8**2, color = "pink") 
ax.scatter3D(x_2[2,-1], y_2[2,-1], z_2[2,-1],s=8**2, color = "orange") 
ax.scatter3D(x_2[3,-1], y_2[3,-1], z_2[3,-1],s=8**2, color = "green") 
ax.scatter3D(x_2[4,-1], y_2[4,-1], z_2[4,-1],s=8**2, color = "grey") 
ax.scatter3D(x_2[5,-1], y_2[5,-1], z_2[5,-1],s=8**2, color = "navy") 
ax.scatter3D(x_2[6,-1], y_2[6,-1], z_2[6,-1],s=8**2, color = "yellow") 
ax.scatter3D(x_2[7,-1], y_2[7,-1], z_2[7,-1],s=8**2, color = "purple") 
ax.scatter3D(x_2[8,-1], y_2[8,-1], z_2[8,-1],s=8**2, color = "darkgreen") 
ax.scatter3D(x_2[9,-1], y_2[9,-1], z_2[9,-1],s=8**2, color = "teal") 
ax.scatter3D(x_2[10,-1], y_2[10,-1], z_2[10,-1],s=8**2, color = "salmon") 
ax.scatter3D(x_2[11,-1], y_2[11,-1], z_2[11,-1],s=8**2, color = "black") 
ax.scatter3D(x_2[12,-1], y_2[12,-1], z_2[12,-1],s=8**2, color = "cyan") 
ax.scatter3D(x_2[13,-1], y_2[13,-1], z_2[13,-1],s=8**2, color = "brown") 
ax.scatter3D(x_2[14,-1], y_2[14,-1], z_2[14,-1],s=8**2, color = "coral") 
ax.scatter3D(x_2[15,-1], y_2[15,-1], z_2[15,-1],s=8**2, color = "lime") 
ax.set_xlabel('x[m]', fontweight ='bold')  
ax.set_ylabel('y[m]', fontweight ='bold')  
ax.set_zlabel('z[m]', fontweight ='bold') 
ax.text2D(0.05, 0.95, "r=0.30", transform=ax.transAxes)



fig = plt.figure(figsize=plt.figaspect(1))
ax = fig.add_subplot(111, projection='3d')

plot_cuboid(center_5, (a_elipse_3, b_elipse_3, c_elipse_3))
plot_cuboid(center_6, (a_elipse_3, b_elipse_3, c_elipse_3))

ax.plot(x_3[0],y_3[0],z_3[0], '-r', linewidth = 3.0)
ax.plot(x_3[1],y_3[1],z_3[1], color ='pink', linewidth = 3.0)
ax.plot(x_3[2],y_3[2],z_3[2], color ='orange', linewidth = 3.0)
ax.plot(x_3[3],y_3[3],z_3[3], color ='green', linewidth = 3.0)
ax.plot(x_3[4],y_3[4],z_3[4], color ='grey', linewidth = 3.0)
ax.plot(x_3[5],y_3[5],z_3[5], color ='navy', linewidth = 3.0)
ax.plot(x_3[6],y_3[6],z_3[6], color ='yellow', linewidth = 3.0)
ax.plot(x_3[7],y_3[7],z_3[7], color ='purple', linewidth = 3.0)
ax.plot(x_3[8],y_3[8],z_3[8], color ='darkgreen', linewidth = 3.0)
ax.plot(x_3[9],y_3[9],z_3[9], color ='teal', linewidth = 3.0)
ax.plot(x_3[10],y_3[10],z_3[10], color ='salmon', linewidth = 3.0)
ax.plot(x_3[11],y_3[11],z_3[11], color ='black', linewidth = 3.0)
ax.plot(x_3[12],y_3[12],z_3[12], color ='cyan', linewidth = 3.0)
ax.plot(x_3[13],y_3[13],z_3[13], color ='brown', linewidth = 3.0)
ax.plot(x_3[14],y_3[14],z_3[14], color ='coral', linewidth = 3.0)
ax.plot(x_3[15],y_3[15],z_3[15], color ='lime', linewidth = 3.0)
ax.scatter3D(x_3[0,0], y_3[0,0], z_3[0,0], s=13**2,color = "red", marker ="x") 
ax.scatter3D(x_3[1,0], y_3[1,0], z_3[1,0], s=13**2,color = "pink", marker ="x") 
ax.scatter3D(x_3[2,0], y_3[2,0], z_3[2,0], s=13**2,color = "orange", marker ="x") 
ax.scatter3D(x_3[3,0], y_3[3,0], z_3[3,0], s=13**2,color = "green", marker ="x") 
ax.scatter3D(x_3[4,0], y_3[4,0], z_3[4,0], s=13**2,color = "grey", marker ="x") 
ax.scatter3D(x_3[5,0], y_3[5,0], z_3[5,0], s=13**2,color = "navy", marker ="x") 
ax.scatter3D(x_3[6,0], y_3[6,0], z_3[6,0], s=13**2,color = "yellow", marker ="x") 
ax.scatter3D(x_3[7,0], y_3[7,0], z_3[7,0], s=13**2,color = "purple", marker ="x") 
ax.scatter3D(x_3[8,0], y_3[8,0], z_3[8,0], s=13**2,color = "darkgreen", marker ="x") 
ax.scatter3D(x_3[9,0], y_3[9,0], z_3[9,0], s=13**2,color = "teal", marker ="x") 
ax.scatter3D(x_3[10,0], y_3[10,0], z_3[10,0],s=13**2, color = "salmon", marker ="x") 
ax.scatter3D(x_3[11,0], y_3[11,0], z_3[11,0],s=13**2, color = "black", marker ="x") 
ax.scatter3D(x_3[12,0], y_3[12,0], z_3[12,0],s=13**2, color = "cyan", marker ="x") 
ax.scatter3D(x_3[13,0], y_3[13,0], z_3[13,0],s=13**2, color = "brown", marker ="x") 
ax.scatter3D(x_3[14,0], y_3[14,0], z_3[14,0],s=13**2, color = "coral", marker ="x") 
ax.scatter3D(x_3[15,0], y_3[15,0], z_3[15,0],s=13**2, color = "lime", marker ="x") 
ax.scatter3D(x_3[0,-1], y_3[0,-1], z_3[0,-1],s=8**2, color = "red") 
ax.scatter3D(x_3[1,-1], y_3[1,-1], z_3[1,-1],s=8**2, color = "pink") 
ax.scatter3D(x_3[2,-1], y_3[2,-1], z_3[2,-1],s=8**2, color = "orange") 
ax.scatter3D(x_3[3,-1], y_3[3,-1], z_3[3,-1],s=8**2, color = "green") 
ax.scatter3D(x_3[4,-1], y_3[4,-1], z_3[4,-1],s=8**2, color = "grey") 
ax.scatter3D(x_3[5,-1], y_3[5,-1], z_3[5,-1],s=8**2, color = "navy") 
ax.scatter3D(x_3[6,-1], y_3[6,-1], z_3[6,-1],s=8**2, color = "yellow") 
ax.scatter3D(x_3[7,-1], y_3[7,-1], z_3[7,-1],s=8**2, color = "purple") 
ax.scatter3D(x_3[8,-1], y_3[8,-1], z_3[8,-1],s=8**2, color = "darkgreen") 
ax.scatter3D(x_3[9,-1], y_3[9,-1], z_3[9,-1],s=8**2, color = "teal") 
ax.scatter3D(x_3[10,-1], y_3[10,-1], z_3[10,-1],s=8**2, color = "salmon") 
ax.scatter3D(x_3[11,-1], y_3[11,-1], z_3[11,-1],s=8**2, color = "black") 
ax.scatter3D(x_3[12,-1], y_3[12,-1], z_3[12,-1],s=8**2, color = "cyan") 
ax.scatter3D(x_3[13,-1], y_3[13,-1], z_3[13,-1],s=8**2, color = "brown") 
ax.scatter3D(x_3[14,-1], y_3[14,-1], z_3[14,-1],s=8**2, color = "coral") 
ax.scatter3D(x_3[15,-1], y_3[15,-1], z_3[15,-1],s=8**2, color = "lime") 

ax.set_xlabel('x[m]', fontweight ='bold')  
ax.set_ylabel('y[m]', fontweight ='bold')  
ax.set_zlabel('z[m]', fontweight ='bold') 
ax.text2D(0.05, 0.95, "r=0.15", transform=ax.transAxes)



fig = plt.figure(figsize=plt.figaspect(1))
ax = fig.add_subplot(111, projection='3d')

plot_cuboid(center_7, (a_elipse_4, b_elipse_4, c_elipse_4))
plot_cuboid(center_8, (a_elipse_4, b_elipse_4, c_elipse_4))

ax.plot(x_4[0],y_4[0],z_4[0], '-r', linewidth = 3.0)
ax.plot(x_4[1],y_4[1],z_4[1], color ='pink', linewidth = 3.0)
ax.plot(x_4[2],y_4[2],z_4[2], color ='orange', linewidth = 3.0)
ax.plot(x_4[3],y_4[3],z_4[3], color ='green', linewidth = 3.0)
ax.plot(x_4[4],y_4[4],z_4[4], color ='grey', linewidth = 3.0)
ax.plot(x_4[5],y_4[5],z_4[5], color ='navy', linewidth = 3.0)
ax.plot(x_4[6],y_4[6],z_4[6], color ='yellow', linewidth = 3.0)
ax.plot(x_4[7],y_4[7],z_4[7], color ='purple', linewidth = 3.0)
ax.plot(x_4[8],y_4[8],z_4[8], color ='darkgreen', linewidth = 3.0)
ax.plot(x_4[9],y_4[9],z_4[9], color ='teal', linewidth = 3.0)
ax.plot(x_4[10],y_4[10],z_4[10], color ='salmon', linewidth = 3.0)
ax.plot(x_4[11],y_4[11],z_4[11], color ='black', linewidth = 3.0)
ax.plot(x_4[12],y_4[12],z_4[12], color ='cyan', linewidth = 3.0)
ax.plot(x_4[13],y_4[13],z_4[13], color ='brown', linewidth = 3.0)
ax.plot(x_4[14],y_4[14],z_4[14], color ='coral', linewidth = 3.0)
ax.plot(x_4[15],y_4[15],z_4[15], color ='lime', linewidth = 3.0)
ax.scatter3D(x_4[0,0], y_4[0,0], z_4[0,0], s=13**2,color = "red", marker ="x") 
ax.scatter3D(x_4[1,0], y_4[1,0], z_4[1,0], s=13**2,color = "pink", marker ="x") 
ax.scatter3D(x_4[2,0], y_4[2,0], z_4[2,0], s=13**2,color = "orange", marker ="x") 
ax.scatter3D(x_4[3,0], y_4[3,0], z_4[3,0], s=13**2,color = "green", marker ="x") 
ax.scatter3D(x_4[4,0], y_4[4,0], z_4[4,0], s=13**2,color = "grey", marker ="x") 
ax.scatter3D(x_4[5,0], y_4[5,0], z_4[5,0], s=13**2,color = "navy", marker ="x") 
ax.scatter3D(x_4[6,0], y_4[6,0], z_4[6,0], s=13**2,color = "yellow", marker ="x") 
ax.scatter3D(x_4[7,0], y_4[7,0], z_4[7,0], s=13**2,color = "purple", marker ="x") 
ax.scatter3D(x_4[8,0], y_4[8,0], z_4[8,0], s=13**2,color = "darkgreen", marker ="x") 
ax.scatter3D(x_4[9,0], y_4[9,0], z_4[9,0], s=13**2,color = "teal", marker ="x") 
ax.scatter3D(x_4[10,0], y_4[10,0], z_4[10,0],s=13**2, color = "salmon", marker ="x") 
ax.scatter3D(x_4[11,0], y_4[11,0], z_4[11,0],s=13**2, color = "black", marker ="x") 
ax.scatter3D(x_4[12,0], y_4[12,0], z_4[12,0],s=13**2, color = "cyan", marker ="x") 
ax.scatter3D(x_4[13,0], y_4[13,0], z_4[13,0],s=13**2, color = "brown", marker ="x") 
ax.scatter3D(x_4[14,0], y_4[14,0], z_4[14,0],s=13**2, color = "coral", marker ="x") 
ax.scatter3D(x_4[15,0], y_4[15,0], z_4[15,0],s=13**2, color = "lime", marker ="x") 
ax.scatter3D(x_4[0,-1], y_4[0,-1], z_4[0,-1],s=8**2, color = "red") 
ax.scatter3D(x_4[1,-1], y_4[1,-1], z_4[1,-1],s=8**2, color = "pink") 
ax.scatter3D(x_4[2,-1], y_4[2,-1], z_4[2,-1],s=8**2, color = "orange") 
ax.scatter3D(x_4[3,-1], y_4[3,-1], z_4[3,-1],s=8**2, color = "green") 
ax.scatter3D(x_4[4,-1], y_4[4,-1], z_4[4,-1],s=8**2, color = "grey") 
ax.scatter3D(x_4[5,-1], y_4[5,-1], z_4[5,-1],s=8**2, color = "navy") 
ax.scatter3D(x_4[6,-1], y_4[6,-1], z_4[6,-1],s=8**2, color = "yellow") 
ax.scatter3D(x_4[7,-1], y_4[7,-1], z_4[7,-1],s=8**2, color = "purple") 
ax.scatter3D(x_4[8,-1], y_4[8,-1], z_4[8,-1],s=8**2, color = "darkgreen") 
ax.scatter3D(x_4[9,-1], y_4[9,-1], z_4[9,-1],s=8**2, color = "teal") 
ax.scatter3D(x_4[10,-1], y_4[10,-1], z_4[10,-1],s=8**2, color = "salmon") 
ax.scatter3D(x_4[11,-1], y_4[11,-1], z_4[11,-1],s=8**2, color = "black") 
ax.scatter3D(x_4[12,-1], y_4[12,-1], z_4[12,-1],s=8**2, color = "cyan") 
ax.scatter3D(x_4[13,-1], y_4[13,-1], z_4[13,-1],s=8**2, color = "brown") 
ax.scatter3D(x_4[14,-1], y_4[14,-1], z_4[14,-1],s=8**2, color = "coral") 
ax.scatter3D(x_4[15,-1], y_4[15,-1], z_4[15,-1],s=8**2, color = "lime") 
ax.set_xlabel('x[m]', fontweight ='bold')  
ax.set_ylabel('y[m]', fontweight ='bold')  
ax.set_zlabel('z[m]', fontweight ='bold') 
ax.text2D(0.05, 0.95, "r=0.60", transform=ax.transAxes)

fig = plt.figure(figsize=plt.figaspect(1))
ax = fig.add_subplot(111, projection='3d')

plot_cuboid(center_9, (a_elipse_5, b_elipse_5, c_elipse_5))
plot_cuboid(center_10, (a_elipse_5, b_elipse_5, c_elipse_5))


ax.plot(x_5[0],y_5[0],z_5[0], '-r', linewidth = 3.0)
ax.plot(x_5[1],y_5[1],z_5[1], color ='pink', linewidth = 3.0)
ax.plot(x_5[2],y_5[2],z_5[2], color ='orange', linewidth = 3.0)
ax.plot(x_5[3],y_5[3],z_5[3], color ='green', linewidth = 3.0)
ax.plot(x_5[4],y_5[4],z_5[4], color ='grey', linewidth = 3.0)
ax.plot(x_5[5],y_5[5],z_5[5], color ='navy', linewidth = 3.0)
ax.plot(x_5[6],y_5[6],z_5[6], color ='yellow', linewidth = 3.0)
ax.plot(x_5[7],y_5[7],z_5[7], color ='purple', linewidth = 3.0)
ax.plot(x_5[8],y_5[8],z_5[8], color ='darkgreen', linewidth = 3.0)
ax.plot(x_5[9],y_5[9],z_5[9], color ='teal', linewidth = 3.0)
ax.plot(x_5[10],y_5[10],z_5[10], color ='salmon', linewidth = 3.0)
ax.plot(x_5[11],y_5[11],z_5[11], color ='black', linewidth = 3.0)
ax.plot(x_5[12],y_5[12],z_5[12], color ='cyan', linewidth = 3.0)
ax.plot(x_5[13],y_5[13],z_5[13], color ='brown', linewidth = 3.0)
ax.plot(x_5[14],y_5[14],z_5[14], color ='coral', linewidth = 3.0)
ax.plot(x_5[15],y_5[15],z_5[15], color ='lime', linewidth = 3.0)
ax.scatter3D(x_5[0,0], y_5[0,0], z_5[0,0], s=13**2,color = "red", marker ="x") 
ax.scatter3D(x_5[1,0], y_5[1,0], z_5[1,0], s=13**2,color = "pink", marker ="x") 
ax.scatter3D(x_5[2,0], y_5[2,0], z_5[2,0], s=13**2,color = "orange", marker ="x") 
ax.scatter3D(x_5[3,0], y_5[3,0], z_5[3,0], s=13**2,color = "green", marker ="x") 
ax.scatter3D(x_5[4,0], y_5[4,0], z_5[4,0], s=13**2,color = "grey", marker ="x") 
ax.scatter3D(x_5[5,0], y_5[5,0], z_5[5,0], s=13**2,color = "navy", marker ="x") 
ax.scatter3D(x_5[6,0], y_5[6,0], z_5[6,0], s=13**2,color = "yellow", marker ="x") 
ax.scatter3D(x_5[7,0], y_5[7,0], z_5[7,0], s=13**2,color = "purple", marker ="x") 
ax.scatter3D(x_5[8,0], y_5[8,0], z_5[8,0], s=13**2,color = "darkgreen", marker ="x") 
ax.scatter3D(x_5[9,0], y_5[9,0], z_5[9,0], s=13**2,color = "teal", marker ="x") 
ax.scatter3D(x_5[10,0], y_5[10,0], z_5[10,0],s=13**2, color = "salmon", marker ="x") 
ax.scatter3D(x_5[11,0], y_5[11,0], z_5[11,0],s=13**2, color = "black", marker ="x") 
ax.scatter3D(x_5[12,0], y_5[12,0], z_5[12,0],s=13**2, color = "cyan", marker ="x") 
ax.scatter3D(x_5[13,0], y_5[13,0], z_5[13,0],s=13**2, color = "brown", marker ="x") 
ax.scatter3D(x_5[14,0], y_5[14,0], z_5[14,0],s=13**2, color = "coral", marker ="x") 
ax.scatter3D(x_5[15,0], y_5[15,0], z_5[15,0],s=13**2, color = "lime", marker ="x") 
ax.scatter3D(x_5[0,-1], y_5[0,-1], z_5[0,-1],s=8**2, color = "red") 
ax.scatter3D(x_5[1,-1], y_5[1,-1], z_5[1,-1],s=8**2, color = "pink") 
ax.scatter3D(x_5[2,-1], y_5[2,-1], z_5[2,-1],s=8**2, color = "orange") 
ax.scatter3D(x_5[3,-1], y_5[3,-1], z_5[3,-1],s=8**2, color = "green") 
ax.scatter3D(x_5[4,-1], y_5[4,-1], z_5[4,-1],s=8**2, color = "grey") 
ax.scatter3D(x_5[5,-1], y_5[5,-1], z_5[5,-1],s=8**2, color = "navy") 
ax.scatter3D(x_5[6,-1], y_5[6,-1], z_5[6,-1],s=8**2, color = "yellow") 
ax.scatter3D(x_5[7,-1], y_5[7,-1], z_5[7,-1],s=8**2, color = "purple") 
ax.scatter3D(x_5[8,-1], y_5[8,-1], z_5[8,-1],s=8**2, color = "darkgreen") 
ax.scatter3D(x_5[9,-1], y_5[9,-1], z_5[9,-1],s=8**2, color = "teal") 
ax.scatter3D(x_5[10,-1], y_5[10,-1], z_5[10,-1],s=8**2, color = "salmon") 
ax.scatter3D(x_5[11,-1], y_5[11,-1], z_5[11,-1],s=8**2, color = "black") 
ax.scatter3D(x_5[12,-1], y_5[12,-1], z_5[12,-1],s=8**2, color = "cyan") 
ax.scatter3D(x_5[13,-1], y_5[13,-1], z_5[13,-1],s=8**2, color = "brown") 
ax.scatter3D(x_5[14,-1], y_5[14,-1], z_5[14,-1],s=8**2, color = "coral") 
ax.scatter3D(x_5[15,-1], y_5[15,-1], z_5[15,-1],s=8**2, color = "lime") 
ax.set_xlabel('x[m]', fontweight ='bold')  
ax.set_ylabel('y[m]', fontweight ='bold')  
ax.set_zlabel('z[m]', fontweight ='bold') 
ax.text2D(0.05, 0.95, "r=0.30", transform=ax.transAxes)


plt.show()