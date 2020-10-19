
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


######################obstacles###############
x_obs_static_1_temp = scipy.io.loadmat('x_obs_static_1.mat')
x_obs_static_1 = x_obs_static_1_temp['x_obs_static_1'].squeeze()

y_obs_static_1_temp = scipy.io.loadmat('y_obs_static_1.mat')
y_obs_static_1 = y_obs_static_1_temp['y_obs_static_1'].squeeze()

z_obs_static_1_temp = scipy.io.loadmat('z_obs_static_1.mat')
z_obs_static_1 = z_obs_static_1_temp['z_obs_static_1'].squeeze()

x_obs_static_2_temp = scipy.io.loadmat('x_obs_static_2.mat')
x_obs_static_2 = x_obs_static_2_temp['x_obs_static_2'].squeeze()

y_obs_static_2_temp = scipy.io.loadmat('y_obs_static_2.mat')
y_obs_static_2 = y_obs_static_2_temp['y_obs_static_2'].squeeze()

z_obs_static_2_temp = scipy.io.loadmat('z_obs_static_2.mat')
z_obs_static_2 = z_obs_static_2_temp['z_obs_static_2'].squeeze()

num_horizon = 100

n_d = 2


a_elipse_1 = 4.0
b_elipse_1 = 4.0
c_elipse_1 = 4.0

a_elipse_2 = 6.5
b_elipse_2 = 6.5
c_elipse_2 = 6.5


a_elipse_1 = 0.5*(2/sqrt(3))*a_elipse_1
b_elipse_1 = 0.5*(2/sqrt(3))*b_elipse_1
c_elipse_1 = 0.5*(2/sqrt(3))*c_elipse_1

a_elipse_2 = 0.5*(2/sqrt(3))*a_elipse_2
b_elipse_2 = 0.5*(2/sqrt(3))*b_elipse_2
c_elipse_2 = 0.5*(2/sqrt(3))*c_elipse_2


center_1 = hstack((x_obs_static_1[0,0],y_obs_static_1[0,0],z_obs_static_1[0,0]))
center_2 = hstack((x_obs_static_1[1,0],y_obs_static_1[1,0],z_obs_static_1[1,0]))

center_3 = hstack((x_obs_static_2[0,0],y_obs_static_2[0,0],z_obs_static_2[0,0]))
center_4 = hstack((x_obs_static_2[1,0],y_obs_static_2[1,0],z_obs_static_2[1,0]))





fig = plt.figure(figsize=plt.figaspect(1))
ax = fig.add_subplot(111, projection='3d')

plot_cuboid(center_1, (a_elipse_1, b_elipse_1, c_elipse_1))
plot_cuboid(center_2, (a_elipse_1, b_elipse_1, c_elipse_1))

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
ax.plot(x_1[16],y_1[16],z_1[16], color = 'khaki', linewidth = 3.0)
ax.plot(x_1[17],y_1[17],z_1[17], color ='deeppink', linewidth = 3.0)
ax.plot(x_1[18],y_1[18],z_1[18], color ='darkorange', linewidth = 3.0)
ax.plot(x_1[19],y_1[19],z_1[19], color ='crimson', linewidth = 3.0)
ax.plot(x_1[20],y_1[20],z_1[20], color ='darkgrey', linewidth = 3.0)
ax.plot(x_1[21],y_1[21],z_1[21], color ='tomato', linewidth = 3.0)
ax.plot(x_1[22],y_1[22],z_1[22], color ='plum', linewidth = 3.0)
ax.plot(x_1[23],y_1[23],z_1[23], color ='hotpink', linewidth = 3.0)
ax.plot(x_1[24],y_1[24],z_1[24], color ='limegreen', linewidth = 3.0)
ax.plot(x_1[25],y_1[25],z_1[25], color ='peru', linewidth = 3.0)
ax.plot(x_1[26],y_1[26],z_1[26], color ='olive', linewidth = 3.0)
ax.plot(x_1[27],y_1[27],z_1[27], color ='wheat', linewidth = 3.0)
ax.plot(x_1[28],y_1[28],z_1[28], color ='blue', linewidth = 3.0)
ax.plot(x_1[29],y_1[29],z_1[29], color ='orchid', linewidth = 3.0)
ax.plot(x_1[30],y_1[30],z_1[30], color ='gold', linewidth = 3.0)
ax.plot(x_1[31],y_1[31],z_1[31], color ='lightgreen',linewidth = 3.0)
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
ax.scatter3D(x_1[16,0], y_1[16,0], z_1[16,0], s=13**2,color = "khaki", marker ="x") 
ax.scatter3D(x_1[17,0], y_1[17,0], z_1[17,0], s=13**2,color = "deeppink", marker ="x") 
ax.scatter3D(x_1[18,0], y_1[18,0], z_1[18,0], s=13**2,color = "darkorange", marker ="x") 
ax.scatter3D(x_1[19,0], y_1[19,0], z_1[19,0], s=13**2,color = "crimson", marker ="x") 
ax.scatter3D(x_1[20,0], y_1[20,0], z_1[20,0], s=13**2,color = "darkgrey", marker ="x") 
ax.scatter3D(x_1[21,0], y_1[21,0], z_1[21,0], s=13**2,color = "tomato", marker ="x") 
ax.scatter3D(x_1[22,0], y_1[22,0], z_1[22,0], s=13**2,color = "plum", marker ="x") 
ax.scatter3D(x_1[23,0], y_1[23,0], z_1[23,0], s=13**2,color = "hotpink", marker ="x") 
ax.scatter3D(x_1[24,0], y_1[24,0], z_1[24,0], s=13**2,color = "limegreen", marker ="x") 
ax.scatter3D(x_1[25,0], y_1[25,0], z_1[25,0], s=13**2,color = "peru", marker ="x") 
ax.scatter3D(x_1[26,0], y_1[26,0], z_1[26,0],s=13**2, color = "olive", marker ="x") 
ax.scatter3D(x_1[27,0], y_1[27,0], z_1[27,0],s=13**2, color = "wheat", marker ="x") 
ax.scatter3D(x_1[28,0], y_1[28,0], z_1[28,0],s=13**2, color = "blue", marker ="x") 
ax.scatter3D(x_1[29,0], y_1[29,0], z_1[29,0],s=13**2, color = "orchid", marker ="x") 
ax.scatter3D(x_1[30,0], y_1[30,0], z_1[30,0],s=13**2, color = "gold", marker ="x") 
ax.scatter3D(x_1[31,0], y_1[31,0], z_1[31,0],s=13**2, color = "lightgreen", marker ="x")
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
ax.scatter3D(x_1[16,-1], y_1[16,-1], z_1[16,-1],s=8**2, color = "khaki") 
ax.scatter3D(x_1[17,-1], y_1[17,-1], z_1[17,-1],s=8**2, color = "deeppink") 
ax.scatter3D(x_1[18,-1], y_1[18,-1], z_1[18,-1],s=8**2, color = "darkorange") 
ax.scatter3D(x_1[19,-1], y_1[19,-1], z_1[19,-1],s=8**2, color = "crimson") 
ax.scatter3D(x_1[20,-1], y_1[20,-1], z_1[20,-1],s=8**2, color = "darkgrey") 
ax.scatter3D(x_1[21,-1], y_1[21,-1], z_1[21,-1],s=8**2, color = "tomato") 
ax.scatter3D(x_1[22,-1], y_1[22,-1], z_1[22,-1],s=8**2, color = "plum") 
ax.scatter3D(x_1[23,-1], y_1[23,-1], z_1[23,-1],s=8**2, color = "hotpink") 
ax.scatter3D(x_1[24,-1], y_1[24,-1], z_1[24,-1],s=8**2, color = "limegreen") 
ax.scatter3D(x_1[25,-1], y_1[25,-1], z_1[25,-1],s=8**2, color = "peru") 
ax.scatter3D(x_1[26,-1], y_1[26,-1], z_1[26,-1],s=8**2, color = "olive") 
ax.scatter3D(x_1[27,-1], y_1[27,-1], z_1[27,-1],s=8**2, color = "wheat") 
ax.scatter3D(x_1[28,-1], y_1[28,-1], z_1[28,-1],s=8**2, color = "blue") 
ax.scatter3D(x_1[29,-1], y_1[29,-1], z_1[29,-1],s=8**2, color = "orchid") 
ax.scatter3D(x_1[30,-1], y_1[30,-1], z_1[30,-1],s=8**2, color = "gold") 
ax.scatter3D(x_1[31,-1], y_1[31,-1], z_1[31,-1],s=8**2, color = "lightgreen") 

ax.set_xlabel('x[m]', fontweight ='bold')  
ax.set_ylabel('y[m]', fontweight ='bold')  
ax.set_zlabel('z[m]', fontweight ='bold') 
ax.text2D(0.05, 0.95, "r=0.15", transform=ax.transAxes)




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
ax.plot(x_2[16],y_2[16],z_2[16], color = 'khaki', linewidth = 3.0)
ax.plot(x_2[17],y_2[17],z_2[17], color ='deeppink', linewidth = 3.0)
ax.plot(x_2[18],y_2[18],z_2[18], color ='darkorange', linewidth = 3.0)
ax.plot(x_2[19],y_2[19],z_2[19], color ='crimson', linewidth = 3.0)
ax.plot(x_2[20],y_2[20],z_2[20], color ='darkgrey', linewidth = 3.0)
ax.plot(x_2[21],y_2[21],z_2[21], color ='tomato', linewidth = 3.0)
ax.plot(x_2[22],y_2[22],z_2[22], color ='plum', linewidth = 3.0)
ax.plot(x_2[23],y_2[23],z_2[23], color ='hotpink', linewidth = 3.0)
ax.plot(x_2[24],y_2[24],z_2[24], color ='limegreen', linewidth = 3.0)
ax.plot(x_2[25],y_2[25],z_2[25], color ='peru', linewidth = 3.0)
ax.plot(x_2[26],y_2[26],z_2[26], color ='olive', linewidth = 3.0)
ax.plot(x_2[27],y_2[27],z_2[27], color ='wheat', linewidth = 3.0)
ax.plot(x_2[28],y_2[28],z_2[28], color ='blue', linewidth = 3.0)
ax.plot(x_2[29],y_2[29],z_2[29], color ='orchid', linewidth = 3.0)
ax.plot(x_2[30],y_2[30],z_2[30], color ='gold', linewidth = 3.0)
ax.plot(x_2[31],y_2[31],z_2[31], color ='lightgreen',linewidth = 3.0)

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
ax.scatter3D(x_2[16,0], y_2[16,0], z_2[16,0], s=13**2,color = "khaki", marker ="x") 
ax.scatter3D(x_2[17,0], y_2[17,0], z_2[17,0], s=13**2,color = "deeppink", marker ="x") 
ax.scatter3D(x_2[18,0], y_2[18,0], z_2[18,0], s=13**2,color = "darkorange", marker ="x") 
ax.scatter3D(x_2[19,0], y_2[19,0], z_2[19,0], s=13**2,color = "crimson", marker ="x") 
ax.scatter3D(x_2[20,0], y_2[20,0], z_2[20,0], s=13**2,color = "darkgrey", marker ="x") 
ax.scatter3D(x_2[21,0], y_2[21,0], z_2[21,0], s=13**2,color = "tomato", marker ="x") 
ax.scatter3D(x_2[22,0], y_2[22,0], z_2[22,0], s=13**2,color = "plum", marker ="x") 
ax.scatter3D(x_2[23,0], y_2[23,0], z_2[23,0], s=13**2,color = "hotpink", marker ="x") 
ax.scatter3D(x_2[24,0], y_2[24,0], z_2[24,0], s=13**2,color = "limegreen", marker ="x") 
ax.scatter3D(x_2[25,0], y_2[25,0], z_2[25,0], s=13**2,color = "peru", marker ="x") 
ax.scatter3D(x_2[26,0], y_2[26,0], z_2[26,0],s=13**2, color = "olive", marker ="x") 
ax.scatter3D(x_2[27,0], y_2[27,0], z_2[27,0],s=13**2, color = "wheat", marker ="x") 
ax.scatter3D(x_2[28,0], y_2[28,0], z_2[28,0],s=13**2, color = "blue", marker ="x") 
ax.scatter3D(x_2[29,0], y_2[29,0], z_2[29,0],s=13**2, color = "orchid", marker ="x") 
ax.scatter3D(x_2[30,0], y_2[30,0], z_2[30,0],s=13**2, color = "gold", marker ="x") 
ax.scatter3D(x_2[31,0], y_2[31,0], z_2[31,0],s=13**2, color = "lightgreen", marker ="x")

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
ax.scatter3D(x_2[16,-1], y_2[16,-1], z_2[16,-1],s=8**2, color = "khaki") 
ax.scatter3D(x_2[17,-1], y_2[17,-1], z_2[17,-1],s=8**2, color = "deeppink") 
ax.scatter3D(x_2[18,-1], y_2[18,-1], z_2[18,-1],s=8**2, color = "darkorange") 
ax.scatter3D(x_2[19,-1], y_2[19,-1], z_2[19,-1],s=8**2, color = "crimson") 
ax.scatter3D(x_2[20,-1], y_2[20,-1], z_2[20,-1],s=8**2, color = "darkgrey") 
ax.scatter3D(x_2[21,-1], y_2[21,-1], z_2[21,-1],s=8**2, color = "tomato") 
ax.scatter3D(x_2[22,-1], y_2[22,-1], z_2[22,-1],s=8**2, color = "plum") 
ax.scatter3D(x_2[23,-1], y_2[23,-1], z_2[23,-1],s=8**2, color = "hotpink") 
ax.scatter3D(x_2[24,-1], y_2[24,-1], z_2[24,-1],s=8**2, color = "limegreen") 
ax.scatter3D(x_2[25,-1], y_2[25,-1], z_2[25,-1],s=8**2, color = "peru") 
ax.scatter3D(x_2[26,-1], y_2[26,-1], z_2[26,-1],s=8**2, color = "olive") 
ax.scatter3D(x_2[27,-1], y_2[27,-1], z_2[27,-1],s=8**2, color = "wheat") 
ax.scatter3D(x_2[28,-1], y_2[28,-1], z_2[28,-1],s=8**2, color = "blue") 
ax.scatter3D(x_2[29,-1], y_2[29,-1], z_2[29,-1],s=8**2, color = "orchid") 
ax.scatter3D(x_2[30,-1], y_2[30,-1], z_2[30,-1],s=8**2, color = "gold") 
ax.scatter3D(x_2[31,-1], y_2[31,-1], z_2[31,-1],s=8**2, color = "lightgreen") 
ax.set_xlabel('x[m]', fontweight ='bold')  
ax.set_ylabel('y[m]', fontweight ='bold')  
ax.set_zlabel('z[m]', fontweight ='bold') 
ax.text2D(0.05, 0.95, "r=0.6", transform=ax.transAxes)




plt.show()