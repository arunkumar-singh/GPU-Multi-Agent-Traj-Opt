

import jax.numpy as jnp
import numpy as np
import wrapper_64_robot
import optim_jax
from scipy.io import loadmat
import time
from jax import jit
from jax.config import config; config.update("jax_enable_x64", True)
import init_final_pos
import scipy
from scipy.io import loadmat


a_1 = 0.34
b_1 = 0.34
c_1 = 0.34

a_2 = 0.28
b_2 = 0.28
c_2 = 0.28

print('Loading Matrices')

cost_mat_inv_x_1 = jnp.asarray(loadmat('matrix_computation/cost_mat_inv_x_1_dynobs_2.mat')['inv_1'])
cost_mat_inv_x_2 = jnp.asarray(loadmat('matrix_computation/cost_mat_inv_x_2_dynobs_2.mat')['inv_2'])
cost_mat_inv_x_3 = jnp.asarray(loadmat('matrix_computation/cost_mat_inv_x_3_dynobs_2.mat')['inv_3'])
cost_mat_inv_x_4 = jnp.asarray(loadmat('matrix_computation/cost_mat_inv_x_4_dynobs_2.mat')['inv_4'])
cost_mat_inv_x_5 = jnp.asarray(loadmat('matrix_computation/cost_mat_inv_x_5_dynobs_2.mat')['inv_5'])
cost_mat_inv_x_6 = jnp.asarray(loadmat('matrix_computation/cost_mat_inv_x_6_dynobs_2.mat')['inv_6'])
cost_mat_inv_x_7 = jnp.asarray(loadmat('matrix_computation/cost_mat_inv_x_7_dynobs_2.mat')['inv_7'])
cost_mat_inv_x_8 = jnp.asarray(loadmat('matrix_computation/cost_mat_inv_x_8_dynobs_2.mat')['inv_8'])
cost_mat_inv_x_9 = jnp.asarray(loadmat('matrix_computation/cost_mat_inv_x_9_dynobs_2.mat')['inv_9'])
cost_mat_inv_x_10 = jnp.asarray(loadmat('matrix_computation/cost_mat_inv_x_10_dynobs_2.mat')['inv_10'])

cost_mat_inv_y_1 = jnp.asarray(loadmat('matrix_computation/cost_mat_inv_y_1_dynobs_2.mat')['inv_1'])
cost_mat_inv_y_2 = jnp.asarray(loadmat('matrix_computation/cost_mat_inv_y_2_dynobs_2.mat')['inv_2'])
cost_mat_inv_y_3 = jnp.asarray(loadmat('matrix_computation/cost_mat_inv_y_3_dynobs_2.mat')['inv_3'])
cost_mat_inv_y_4 = jnp.asarray(loadmat('matrix_computation/cost_mat_inv_y_4_dynobs_2.mat')['inv_4'])
cost_mat_inv_y_5 = jnp.asarray(loadmat('matrix_computation/cost_mat_inv_y_5_dynobs_2.mat')['inv_5'])
cost_mat_inv_y_6 = jnp.asarray(loadmat('matrix_computation/cost_mat_inv_y_6_dynobs_2.mat')['inv_6'])
cost_mat_inv_y_7 = jnp.asarray(loadmat('matrix_computation/cost_mat_inv_y_7_dynobs_2.mat')['inv_7'])
cost_mat_inv_y_8 = jnp.asarray(loadmat('matrix_computation/cost_mat_inv_y_8_dynobs_2.mat')['inv_8'])
cost_mat_inv_y_9 = jnp.asarray(loadmat('matrix_computation/cost_mat_inv_y_9_dynobs_2.mat')['inv_9'])
cost_mat_inv_y_10 = jnp.asarray(loadmat('matrix_computation/cost_mat_inv_y_10_dynobs_2.mat')['inv_10'])

cost_mat_inv_z_1 = jnp.asarray(loadmat('matrix_computation/cost_mat_inv_z_1_dynobs_2.mat')['inv_1'])
cost_mat_inv_z_2 = jnp.asarray(loadmat('matrix_computation/cost_mat_inv_z_2_dynobs_2.mat')['inv_2'])
cost_mat_inv_z_3 = jnp.asarray(loadmat('matrix_computation/cost_mat_inv_z_3_dynobs_2.mat')['inv_3'])
cost_mat_inv_z_4 = jnp.asarray(loadmat('matrix_computation/cost_mat_inv_z_4_dynobs_2.mat')['inv_4'])
cost_mat_inv_z_5 = jnp.asarray(loadmat('matrix_computation/cost_mat_inv_z_5_dynobs_2.mat')['inv_5'])
cost_mat_inv_z_6 = jnp.asarray(loadmat('matrix_computation/cost_mat_inv_z_6_dynobs_2.mat')['inv_6'])
cost_mat_inv_z_7 = jnp.asarray(loadmat('matrix_computation/cost_mat_inv_z_7_dynobs_2.mat')['inv_7'])
cost_mat_inv_z_8 = jnp.asarray(loadmat('matrix_computation/cost_mat_inv_z_8_dynobs_2.mat')['inv_8'])
cost_mat_inv_z_9 = jnp.asarray(loadmat('matrix_computation/cost_mat_inv_z_9_dynobs_2.mat')['inv_9'])
cost_mat_inv_z_10 = jnp.asarray(loadmat('matrix_computation/cost_mat_inv_z_10_dynobs_2.mat')['inv_10'])


#
rho_w_alpha_init = jnp.asarray(loadmat('matrix_computation/rho_w_alpha_init_dynobs_2.mat')['rho_w_alpha_init'][0])


Ax_eq = jnp.asarray(loadmat('matrix_computation/Ax_eq.mat')['Ax_eq'])
# bx_eq = jnp.asarray(loadmat('bx_eq.mat')['bx_eq'])
# by_eq = jnp.asarray(loadmat('by_eq.mat')['by_eq'])
# bz_eq = jnp.asarray(loadmat('bz_eq.mat')['bz_eq'])
Ax_eq_obs = jnp.asarray(loadmat('matrix_computation/Ax_eq_obs.mat')['Ax_eq_obs'])

# compute_x_jit = jit(optim_jax.compute_x)
# compute_dobs_jit = jit(optim_jax.compute_dobs)

print('Starting Actual Computation')

x_init, y_init, z_init, x_fin, y_fin, z_fin = init_final_pos.init_final_pos()


start = time.time()
x_1, y_1, z_1 = wrapper_64_robot.main_jax(  x_init, y_init, z_init, x_fin, y_fin, z_fin, a_1, b_1, c_1, cost_mat_inv_x_1, cost_mat_inv_x_2, cost_mat_inv_x_3, cost_mat_inv_x_4, cost_mat_inv_x_5, cost_mat_inv_x_6, cost_mat_inv_x_7, cost_mat_inv_x_8, cost_mat_inv_x_9, cost_mat_inv_x_10, cost_mat_inv_y_1, cost_mat_inv_y_2, cost_mat_inv_y_3, cost_mat_inv_y_4, cost_mat_inv_y_5, cost_mat_inv_y_6, cost_mat_inv_y_7, cost_mat_inv_y_8, cost_mat_inv_y_9, cost_mat_inv_y_10, cost_mat_inv_z_1, cost_mat_inv_z_2, cost_mat_inv_z_3, cost_mat_inv_z_4, cost_mat_inv_z_5, cost_mat_inv_z_6, cost_mat_inv_z_7, cost_mat_inv_z_8, cost_mat_inv_z_9, cost_mat_inv_z_10, Ax_eq_obs, Ax_eq, rho_w_alpha_init     )


x_2, y_2, z_2 = wrapper_64_robot.main_jax(  x_init, y_init, z_init, x_fin, y_fin, z_fin, a_2, b_2, c_2, cost_mat_inv_x_1, cost_mat_inv_x_2, cost_mat_inv_x_3, cost_mat_inv_x_4, cost_mat_inv_x_5, cost_mat_inv_x_6, cost_mat_inv_x_7, cost_mat_inv_x_8, cost_mat_inv_x_9, cost_mat_inv_x_10, cost_mat_inv_y_1, cost_mat_inv_y_2, cost_mat_inv_y_3, cost_mat_inv_y_4, cost_mat_inv_y_5, cost_mat_inv_y_6, cost_mat_inv_y_7, cost_mat_inv_y_8, cost_mat_inv_y_9, cost_mat_inv_y_10, cost_mat_inv_z_1, cost_mat_inv_z_2, cost_mat_inv_z_3, cost_mat_inv_z_4, cost_mat_inv_z_5, cost_mat_inv_z_6, cost_mat_inv_z_7, cost_mat_inv_z_8, cost_mat_inv_z_9, cost_mat_inv_z_10, Ax_eq_obs, Ax_eq, rho_w_alpha_init     )

print('comp time for 2 benchmarks =', time.time()-start)


scipy.io.savemat('x_1.mat', {'x_1': x_1})
scipy.io.savemat('y_1.mat', {'y_1': y_1})
scipy.io.savemat('z_1.mat', {'z_1': z_1})

scipy.io.savemat('x_2.mat', {'x_2': x_2})
scipy.io.savemat('y_2.mat', {'y_2': y_2})
scipy.io.savemat('z_2.mat', {'z_2': z_2})


print ('done')



