


import cupy as cp
import numpy as np
import bernstein_coeff_order10_arbitinterval
import scipy
from scipy.io import loadmat
import time
import optim_cupy
import scipy
from scipy.io import loadmat
import wrapper_32_robots
import init_final_pos


maxiter = 200

a_1 = 0.34
b_1 = 0.34
c_1 = 0.34

a_2 = 0.28
b_2 = 0.28
c_2 = 0.28


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

print('Starting Actual Computation')

x_init, y_init, z_init, x_fin, y_fin, z_fin = init_final_pos.init_final_pos()


start = time.time()
x_1, y_1, z_1 = wrapper_32_robots.main_cupy(  x_init, y_init, z_init, x_fin, y_fin, z_fin, a_1, b_1, c_1, cost_mat_inv_x_1, cost_mat_inv_x_2, cost_mat_inv_x_3, cost_mat_inv_x_4, cost_mat_inv_x_5, cost_mat_inv_x_6, cost_mat_inv_x_7, cost_mat_inv_x_8, cost_mat_inv_x_9, cost_mat_inv_x_10, cost_mat_inv_y_1, cost_mat_inv_y_2, cost_mat_inv_y_3, cost_mat_inv_y_4, cost_mat_inv_y_5, cost_mat_inv_y_6, cost_mat_inv_y_7, cost_mat_inv_y_8, cost_mat_inv_y_9, cost_mat_inv_y_10, cost_mat_inv_z_1, cost_mat_inv_z_2, cost_mat_inv_z_3, cost_mat_inv_z_4, cost_mat_inv_z_5, cost_mat_inv_z_6, cost_mat_inv_z_7, cost_mat_inv_z_8, cost_mat_inv_z_9, cost_mat_inv_z_10, Ax_eq_obs, Ax_eq, rho_w_alpha_init     )


x_2, y_2, z_2 = wrapper_32_robots.main_cupy(  x_init, y_init, z_init, x_fin, y_fin, z_fin, a_2, b_2, c_2, cost_mat_inv_x_1, cost_mat_inv_x_2, cost_mat_inv_x_3, cost_mat_inv_x_4, cost_mat_inv_x_5, cost_mat_inv_x_6, cost_mat_inv_x_7, cost_mat_inv_x_8, cost_mat_inv_x_9, cost_mat_inv_x_10, cost_mat_inv_y_1, cost_mat_inv_y_2, cost_mat_inv_y_3, cost_mat_inv_y_4, cost_mat_inv_y_5, cost_mat_inv_y_6, cost_mat_inv_y_7, cost_mat_inv_y_8, cost_mat_inv_y_9, cost_mat_inv_y_10, cost_mat_inv_z_1, cost_mat_inv_z_2, cost_mat_inv_z_3, cost_mat_inv_z_4, cost_mat_inv_z_5, cost_mat_inv_z_6, cost_mat_inv_z_7, cost_mat_inv_z_8, cost_mat_inv_z_9, cost_mat_inv_z_10, Ax_eq_obs, Ax_eq, rho_w_alpha_init     )


print('comp time for 2 benchmarks =', time.time()-start)



x_1 = cp.asnumpy(x_1,stream=None,order='C')
y_1 = cp.asnumpy(y_1,stream=None,order='C')
z_1 = cp.asnumpy(z_1,stream=None,order='C')

x_2 = cp.asnumpy(x_2,stream=None,order='C')
y_2 = cp.asnumpy(y_2,stream=None,order='C')
z_2 = cp.asnumpy(z_2,stream=None,order='C')



a_1 = cp.asnumpy(a_1,stream=None,order='C')
b_1 = cp.asnumpy(b_1,stream=None,order='C')
c_1 = cp.asnumpy(c_1,stream=None,order='C')


a_2 = cp.asnumpy(a_2,stream=None,order='C')
b_2 = cp.asnumpy(b_2,stream=None,order='C')
c_2 = cp.asnumpy(c_2,stream=None,order='C')



scipy.io.savemat('x_1.mat', {'x_1': x_1})
scipy.io.savemat('y_1.mat', {'y_1': y_1})
scipy.io.savemat('z_1.mat', {'z_1': z_1})

scipy.io.savemat('x_2.mat', {'x_2': x_2})
scipy.io.savemat('y_2.mat', {'y_2': y_2})
scipy.io.savemat('z_2.mat', {'z_2': z_2})


scipy.io.savemat('a_1.mat', {'a_1': a_1})
scipy.io.savemat('b_1.mat', {'b_1': b_1})
scipy.io.savemat('c_1.mat', {'c_1': c_1})

scipy.io.savemat('a_2.mat', {'a_2': a_2})
scipy.io.savemat('b_2.mat', {'b_2': b_2})
scipy.io.savemat('c_2.mat', {'c_2': c_2})








