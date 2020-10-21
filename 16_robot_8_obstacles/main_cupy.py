


import cupy as cp
import numpy as np
import bernstein_coeff_order10_arbitinterval
import scipy
from scipy.io import loadmat
import time
import optim_cupy
import init_final_pos_1
import wrapper_16_robots
import points 


maxiter = 200

a_1 = 0.64
b_1 = 0.64
c_1 = 0.64

#######################3static obstacles###############
n_rob = 16
n_d = 8
n_con = int(scipy.special.binom(n_rob,2))
num_horizon =100
num = num_horizon

a_elipse_1 = 0.5*cp.ones(n_d)
b_elipse_1 = 0.5*cp.ones(n_d)
c_elipse_1 = 0.5*cp.ones(n_d)


#################################################obstacles center##############

points_x_init_obs, points_y_init_obs, points_z_init_obs = points.obstacles_positions()
#print (points_x_init_obs)

x_centre = points_x_init_obs
y_centre = points_y_init_obs
z_centre = points_z_init_obs


x_obs_static = cp.vstack((x_centre[0]*cp.ones(num_horizon), x_centre[1]*cp.ones(num_horizon), x_centre[2]*cp.ones(num_horizon), x_centre[3]*cp.ones(num_horizon), x_centre[4]*cp.ones(num_horizon), x_centre[5]*cp.ones(num_horizon), x_centre[6]*cp.ones(num_horizon), x_centre[7]*cp.ones(num_horizon) ))
y_obs_static = cp.vstack((y_centre[0]*cp.ones(num_horizon), y_centre[1]*cp.ones(num_horizon), y_centre[2]*cp.ones(num_horizon), y_centre[3]*cp.ones(num_horizon), y_centre[4]*cp.ones(num_horizon), y_centre[5]*cp.ones(num_horizon), y_centre[6]*cp.ones(num_horizon), y_centre[7]*cp.ones(num_horizon) ))
z_obs_static = cp.vstack((z_centre[0]*cp.ones(num_horizon), z_centre[1]*cp.ones(num_horizon), z_centre[2]*cp.ones(num_horizon), z_centre[3]*cp.ones(num_horizon), z_centre[4]*cp.ones(num_horizon), z_centre[5]*cp.ones(num_horizon), z_centre[6]*cp.ones(num_horizon), z_centre[7]*cp.ones(num_horizon) ))


bx_eq_obs_1 = cp.hstack((cp.zeros(n_con*num), cp.tile(x_obs_static.flatten(), n_rob) ))
by_eq_obs_1 = cp.hstack((cp.zeros(n_con*num), cp.tile(y_obs_static.flatten(), n_rob) ))
bz_eq_obs_1 = cp.hstack((cp.zeros(n_con*num), cp.tile(z_obs_static.flatten(), n_rob) ))

#print (np.shape(bx_eq_obs_1))

####################################################33
print('Loading Matrices')

cost_mat_inv_x_1 = cp.asarray(loadmat('matrix_computation/cost_mat_inv_x_1_dynobs_2.mat')['inv_1'])
cost_mat_inv_x_2 = cp.asarray(loadmat('matrix_computation/cost_mat_inv_x_2_dynobs_2.mat')['inv_2'])
cost_mat_inv_x_3 = cp.asarray(loadmat('matrix_computation/cost_mat_inv_x_3_dynobs_2.mat')['inv_3'])
cost_mat_inv_x_4 = cp.asarray(loadmat('matrix_computation/cost_mat_inv_x_4_dynobs_2.mat')['inv_4'])
cost_mat_inv_x_5 = cp.asarray(loadmat('matrix_computation/cost_mat_inv_x_5_dynobs_2.mat')['inv_5'])
cost_mat_inv_x_6 = cp.asarray(loadmat('matrix_computation/cost_mat_inv_x_6_dynobs_2.mat')['inv_6'])
cost_mat_inv_x_7 = cp.asarray(loadmat('matrix_computation/cost_mat_inv_x_7_dynobs_2.mat')['inv_7'])
cost_mat_inv_x_8 = cp.asarray(loadmat('matrix_computation/cost_mat_inv_x_8_dynobs_2.mat')['inv_8'])
cost_mat_inv_x_9 = cp.asarray(loadmat('matrix_computation/cost_mat_inv_x_9_dynobs_2.mat')['inv_9'])
cost_mat_inv_x_10 = cp.asarray(loadmat('matrix_computation/cost_mat_inv_x_10_dynobs_2.mat')['inv_10'])

cost_mat_inv_y_1 = cp.asarray(loadmat('matrix_computation/cost_mat_inv_y_1_dynobs_2.mat')['inv_1'])
cost_mat_inv_y_2 = cp.asarray(loadmat('matrix_computation/cost_mat_inv_y_2_dynobs_2.mat')['inv_2'])
cost_mat_inv_y_3 = cp.asarray(loadmat('matrix_computation/cost_mat_inv_y_3_dynobs_2.mat')['inv_3'])
cost_mat_inv_y_4 = cp.asarray(loadmat('matrix_computation/cost_mat_inv_y_4_dynobs_2.mat')['inv_4'])
cost_mat_inv_y_5 = cp.asarray(loadmat('matrix_computation/cost_mat_inv_y_5_dynobs_2.mat')['inv_5'])
cost_mat_inv_y_6 = cp.asarray(loadmat('matrix_computation/cost_mat_inv_y_6_dynobs_2.mat')['inv_6'])
cost_mat_inv_y_7 = cp.asarray(loadmat('matrix_computation/cost_mat_inv_y_7_dynobs_2.mat')['inv_7'])
cost_mat_inv_y_8 = cp.asarray(loadmat('matrix_computation/cost_mat_inv_y_8_dynobs_2.mat')['inv_8'])
cost_mat_inv_y_9 = cp.asarray(loadmat('matrix_computation/cost_mat_inv_y_9_dynobs_2.mat')['inv_9'])
cost_mat_inv_y_10 = cp.asarray(loadmat('matrix_computation/cost_mat_inv_y_10_dynobs_2.mat')['inv_10'])

cost_mat_inv_z_1 = cp.asarray(loadmat('matrix_computation/cost_mat_inv_z_1_dynobs_2.mat')['inv_1'])
cost_mat_inv_z_2 = cp.asarray(loadmat('matrix_computation/cost_mat_inv_z_2_dynobs_2.mat')['inv_2'])
cost_mat_inv_z_3 = cp.asarray(loadmat('matrix_computation/cost_mat_inv_z_3_dynobs_2.mat')['inv_3'])
cost_mat_inv_z_4 = cp.asarray(loadmat('matrix_computation/cost_mat_inv_z_4_dynobs_2.mat')['inv_4'])
cost_mat_inv_z_5 = cp.asarray(loadmat('matrix_computation/cost_mat_inv_z_5_dynobs_2.mat')['inv_5'])
cost_mat_inv_z_6 = cp.asarray(loadmat('matrix_computation/cost_mat_inv_z_6_dynobs_2.mat')['inv_6'])
cost_mat_inv_z_7 = cp.asarray(loadmat('matrix_computation/cost_mat_inv_z_7_dynobs_2.mat')['inv_7'])
cost_mat_inv_z_8 = cp.asarray(loadmat('matrix_computation/cost_mat_inv_z_8_dynobs_2.mat')['inv_8'])
cost_mat_inv_z_9 = cp.asarray(loadmat('matrix_computation/cost_mat_inv_z_9_dynobs_2.mat')['inv_9'])
cost_mat_inv_z_10 = cp.asarray(loadmat('matrix_computation/cost_mat_inv_z_10_dynobs_2.mat')['inv_10'])


rho_w_alpha_init = cp.asarray(loadmat('matrix_computation/rho_w_alpha_init_dynobs_2.mat')['rho_w_alpha_init'][0])


Ax_eq = cp.asarray(loadmat('matrix_computation/Ax_eq.mat')['Ax_eq'])

Ax_eq_obs = cp.asarray(loadmat('matrix_computation/Ax_eq_obs.mat')['Ax_eq_obs'])
###########################################
print('Starting Actual Computation')

x_init_1, y_init_1, z_init_1, x_fin_1, y_fin_1, z_fin_1 = init_final_pos_1.init_final_pos(n_rob)

start = time.time()


x_1, y_1, z_1 = wrapper_16_robots.main_cupy(  x_init_1, y_init_1, z_init_1, x_fin_1, y_fin_1, z_fin_1, a_1, b_1, c_1, cost_mat_inv_x_1, cost_mat_inv_x_2, cost_mat_inv_x_3, cost_mat_inv_x_4, cost_mat_inv_x_5, cost_mat_inv_x_6, cost_mat_inv_x_7, cost_mat_inv_x_8, cost_mat_inv_x_9, cost_mat_inv_x_10, cost_mat_inv_y_1, cost_mat_inv_y_2, cost_mat_inv_y_3, cost_mat_inv_y_4, cost_mat_inv_y_5, cost_mat_inv_y_6, cost_mat_inv_y_7, cost_mat_inv_y_8, cost_mat_inv_y_9, cost_mat_inv_y_10, cost_mat_inv_z_1, cost_mat_inv_z_2, cost_mat_inv_z_3, cost_mat_inv_z_4, cost_mat_inv_z_5, cost_mat_inv_z_6, cost_mat_inv_z_7, cost_mat_inv_z_8, cost_mat_inv_z_9, cost_mat_inv_z_10, Ax_eq_obs,  bx_eq_obs_1, by_eq_obs_1, bz_eq_obs_1, Ax_eq, rho_w_alpha_init, a_elipse_1, b_elipse_1, c_elipse_1  )

print('comp time for 16 robot with 12 obstacles =', time.time()-start)


x_1 = cp.asnumpy(x_1,stream=None,order='C')
y_1 = cp.asnumpy(y_1,stream=None,order='C')
z_1 = cp.asnumpy(z_1,stream=None,order='C')


scipy.io.savemat('x_1.mat', {'x_1': x_1})
scipy.io.savemat('y_1.mat', {'y_1': y_1})
scipy.io.savemat('z_1.mat', {'z_1': z_1})

points_x_init_obs = cp.asnumpy(points_x_init_obs,stream=None,order='C')
points_y_init_obs = cp.asnumpy(points_y_init_obs,stream=None,order='C')
points_z_init_obs = cp.asnumpy(points_z_init_obs,stream=None,order='C')


scipy.io.savemat('points_x_init_obs.mat', {'points_x_init_obs': points_x_init_obs})
scipy.io.savemat('points_y_init_obs.mat', {'points_y_init_obs': points_y_init_obs})
scipy.io.savemat('points_z_init_obs.mat', {'points_z_init_obs': points_z_init_obs})

