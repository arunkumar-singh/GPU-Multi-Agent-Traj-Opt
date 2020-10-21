



import jax.numpy as jnp
import numpy as np
import bernstein_coeff_order10_arbitinterval
import scipy
from scipy.io import loadmat
import time
import optim_jax
import init_final_pos_1
import init_final_pos_2
from jax import jit
from jax.config import config; config.update("jax_enable_x64", True)
import wrapper_32_robots

# start = time.time()
maxiter = 200

a_1 = 0.34 ########## size of the agents for first benchmark
b_1 = 0.34
c_1 = 0.34

a_2 = 1.24 ################ size of the agents for second benchmark
b_2 = 1.24
c_2 = 1.24

a_3 = 0.15 ################ size of the agents for third benchmark
b_3 = 0.15
c_3 = 0.15

a_4 = 0.64 ################ size of the agents for forth benchmark
b_4 = 0.64
c_4 = 0.64

#######################3static obstacles###############
n_d = 2
n_rob = 32
n_con_1 = int(n_d*n_rob)
num_horizon = 100
num=100
n_con = int(scipy.special.binom(n_rob,2))

a_elipse_1 = 4.0*jnp.ones(n_d)
b_elipse_1 = 4.0*jnp.ones(n_d)
c_elipse_1 = 4.0*jnp.ones(n_d)

a_elipse_2 = 6.5*jnp.ones(n_d)
b_elipse_2 = 6.5*jnp.ones(n_d)
c_elipse_2 = 6.5*jnp.ones(n_d)

a_elipse_3 = 4.0*jnp.ones(n_d)
b_elipse_3 = 4.0*jnp.ones(n_d)
c_elipse_3 = 4.0*jnp.ones(n_d)

a_elipse_4 = 5.0*jnp.ones(n_d)
b_elipse_4 = 5.0*jnp.ones(n_d)
c_elipse_4 = 5.0*jnp.ones(n_d)

##################obstacles center##############

points_x_init_obs_1 = np.hstack((0,0))
points_y_init_obs_1 = np.hstack((-4,4))
points_z_init_obs_1 = np.hstack((2,2))

points_x_init_obs_2 = np.hstack((0,0))
points_y_init_obs_2 = np.hstack((-10,10))
points_z_init_obs_2 = np.hstack((2,2))

points_x_init_obs_3 = np.hstack((0,0))
points_y_init_obs_3 = np.hstack((-4,4))
points_z_init_obs_3 = np.hstack((2,2))

points_x_init_obs_4 = np.hstack((0,0))
points_y_init_obs_4 = np.hstack((-8,8))
points_z_init_obs_4 = np.hstack((2,2))

x_centre_1 = points_x_init_obs_1
y_centre_1 = points_y_init_obs_1
z_centre_1 = points_z_init_obs_1

x_centre_2 = points_x_init_obs_2
y_centre_2 = points_y_init_obs_2
z_centre_2 = points_z_init_obs_2

x_centre_3 = points_x_init_obs_3
y_centre_3 = points_y_init_obs_3
z_centre_3 = points_z_init_obs_3

x_centre_4 = points_x_init_obs_4
y_centre_4 = points_y_init_obs_4
z_centre_4 = points_z_init_obs_4

x_obs_static_1 = np.vstack((x_centre_1[0]*np.ones(num_horizon), x_centre_1[1]*np.ones(num_horizon)))
y_obs_static_1 = np.vstack((y_centre_1[0]*np.ones(num_horizon), y_centre_1[1]*np.ones(num_horizon)))
z_obs_static_1 = np.vstack((z_centre_1[0]*np.ones(num_horizon), z_centre_1[1]*np.ones(num_horizon)))

x_obs_static_2 = np.vstack((x_centre_2[0]*np.ones(num_horizon), x_centre_2[1]*np.ones(num_horizon)))
y_obs_static_2 = np.vstack((y_centre_2[0]*np.ones(num_horizon), y_centre_2[1]*np.ones(num_horizon)))
z_obs_static_2 = np.vstack((z_centre_2[0]*np.ones(num_horizon), z_centre_2[1]*np.ones(num_horizon)))

x_obs_static_3 = np.vstack((x_centre_3[0]*np.ones(num_horizon), x_centre_3[1]*np.ones(num_horizon)))
y_obs_static_3 = np.vstack((y_centre_3[0]*np.ones(num_horizon), y_centre_3[1]*np.ones(num_horizon)))
z_obs_static_3 = np.vstack((z_centre_3[0]*np.ones(num_horizon), z_centre_3[1]*np.ones(num_horizon)))

x_obs_static_4 = np.vstack((x_centre_4[0]*np.ones(num_horizon), x_centre_4[1]*np.ones(num_horizon)))
y_obs_static_4 = np.vstack((y_centre_4[0]*np.ones(num_horizon), y_centre_4[1]*np.ones(num_horizon)))
z_obs_static_4 = np.vstack((z_centre_4[0]*np.ones(num_horizon), z_centre_4[1]*np.ones(num_horizon)))

bx_eq_obs_1 = np.hstack((np.zeros(n_con*num), np.tile(x_obs_static_1.flatten(), n_rob) ))
by_eq_obs_1 = np.hstack((np.zeros(n_con*num), np.tile(y_obs_static_1.flatten(), n_rob) ))
bz_eq_obs_1 = np.hstack((np.zeros(n_con*num), np.tile(z_obs_static_1.flatten(), n_rob) ))

bx_eq_obs_2 = np.hstack((np.zeros(n_con*num), np.tile(x_obs_static_2.flatten(), n_rob) ))
by_eq_obs_2 = np.hstack((np.zeros(n_con*num), np.tile(y_obs_static_2.flatten(), n_rob) ))
bz_eq_obs_2 = np.hstack((np.zeros(n_con*num), np.tile(z_obs_static_2.flatten(), n_rob) ))

bx_eq_obs_3 = np.hstack((np.zeros(n_con*num), np.tile(x_obs_static_3.flatten(), n_rob) ))
by_eq_obs_3 = np.hstack((np.zeros(n_con*num), np.tile(y_obs_static_3.flatten(), n_rob) ))
bz_eq_obs_3 = np.hstack((np.zeros(n_con*num), np.tile(z_obs_static_3.flatten(), n_rob) ))

bx_eq_obs_4 = np.hstack((np.zeros(n_con*num), np.tile(x_obs_static_4.flatten(), n_rob) ))
by_eq_obs_4 = np.hstack((np.zeros(n_con*num), np.tile(y_obs_static_4.flatten(), n_rob) ))
bz_eq_obs_4 = np.hstack((np.zeros(n_con*num), np.tile(z_obs_static_4.flatten(), n_rob) ))
###################################
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


rho_w_alpha_init = jnp.asarray(loadmat('matrix_computation/rho_w_alpha_init_dynobs_2.mat')['rho_w_alpha_init'][0])


Ax_eq = jnp.asarray(loadmat('matrix_computation/Ax_eq.mat')['Ax_eq'])
Ax_eq_obs = jnp.asarray(loadmat('matrix_computation/Ax_eq_obs.mat')['Ax_eq_obs'])


################################# Conversion to Jax array
print('Starting Actual Computation')

x_init_1, y_init_1, z_init_1, x_fin_1, y_fin_1, z_fin_1 = init_final_pos_1.init_final_pos(n_rob)
x_init_2, y_init_2, z_init_2, x_fin_2, y_fin_2, z_fin_2 = init_final_pos_2.init_final_pos(n_rob)
x_init_3, y_init_3, z_init_3, x_fin_3, y_fin_3, z_fin_3 = init_final_pos_1.init_final_pos(n_rob)
x_init_4, y_init_4, z_init_4, x_fin_4, y_fin_4, z_fin_4 = init_final_pos_2.init_final_pos(n_rob)

start = time.time()


x_1, y_1, z_1 = wrapper_32_robots.main_jax(  x_init_1, y_init_1, z_init_1, x_fin_1, y_fin_1, z_fin_1, a_1, b_1, c_1, cost_mat_inv_x_1, cost_mat_inv_x_2, cost_mat_inv_x_3, cost_mat_inv_x_4, cost_mat_inv_x_5, cost_mat_inv_x_6, cost_mat_inv_x_7, cost_mat_inv_x_8, cost_mat_inv_x_9, cost_mat_inv_x_10, cost_mat_inv_y_1, cost_mat_inv_y_2, cost_mat_inv_y_3, cost_mat_inv_y_4, cost_mat_inv_y_5, cost_mat_inv_y_6, cost_mat_inv_y_7, cost_mat_inv_y_8, cost_mat_inv_y_9, cost_mat_inv_y_10, cost_mat_inv_z_1, cost_mat_inv_z_2, cost_mat_inv_z_3, cost_mat_inv_z_4, cost_mat_inv_z_5, cost_mat_inv_z_6, cost_mat_inv_z_7, cost_mat_inv_z_8, cost_mat_inv_z_9, cost_mat_inv_z_10, Ax_eq_obs, bx_eq_obs_1, by_eq_obs_1, bz_eq_obs_1, Ax_eq, rho_w_alpha_init, a_elipse_1, b_elipse_1, c_elipse_1  )


x_2, y_2, z_2 = wrapper_32_robots.main_jax(  x_init_2, y_init_2, z_init_2, x_fin_2, y_fin_2, z_fin_2, a_2, b_2, c_2, cost_mat_inv_x_1, cost_mat_inv_x_2, cost_mat_inv_x_3, cost_mat_inv_x_4, cost_mat_inv_x_5, cost_mat_inv_x_6, cost_mat_inv_x_7, cost_mat_inv_x_8, cost_mat_inv_x_9, cost_mat_inv_x_10, cost_mat_inv_y_1, cost_mat_inv_y_2, cost_mat_inv_y_3, cost_mat_inv_y_4, cost_mat_inv_y_5, cost_mat_inv_y_6, cost_mat_inv_y_7, cost_mat_inv_y_8, cost_mat_inv_y_9, cost_mat_inv_y_10, cost_mat_inv_z_1, cost_mat_inv_z_2, cost_mat_inv_z_3, cost_mat_inv_z_4, cost_mat_inv_z_5, cost_mat_inv_z_6, cost_mat_inv_z_7, cost_mat_inv_z_8, cost_mat_inv_z_9, cost_mat_inv_z_10, Ax_eq_obs,  bx_eq_obs_2, by_eq_obs_2, bz_eq_obs_2, Ax_eq, rho_w_alpha_init, a_elipse_2, b_elipse_2, c_elipse_2  )


x_3, y_3, z_3 = wrapper_32_robots.main_jax(  x_init_3, y_init_3, z_init_3, x_fin_3, y_fin_3, z_fin_3, a_3, b_3, c_3, cost_mat_inv_x_1, cost_mat_inv_x_2, cost_mat_inv_x_3, cost_mat_inv_x_4, cost_mat_inv_x_5, cost_mat_inv_x_6, cost_mat_inv_x_7, cost_mat_inv_x_8, cost_mat_inv_x_9, cost_mat_inv_x_10, cost_mat_inv_y_1, cost_mat_inv_y_2, cost_mat_inv_y_3, cost_mat_inv_y_4, cost_mat_inv_y_5, cost_mat_inv_y_6, cost_mat_inv_y_7, cost_mat_inv_y_8, cost_mat_inv_y_9, cost_mat_inv_y_10, cost_mat_inv_z_1, cost_mat_inv_z_2, cost_mat_inv_z_3, cost_mat_inv_z_4, cost_mat_inv_z_5, cost_mat_inv_z_6, cost_mat_inv_z_7, cost_mat_inv_z_8, cost_mat_inv_z_9, cost_mat_inv_z_10, Ax_eq_obs, bx_eq_obs_3, by_eq_obs_3, bz_eq_obs_3, Ax_eq, rho_w_alpha_init, a_elipse_3, b_elipse_3, c_elipse_3 )


x_4, y_4, z_4 = wrapper_32_robots.main_jax(  x_init_4, y_init_4, z_init_4, x_fin_4, y_fin_4, z_fin_4, a_4, b_4, c_4, cost_mat_inv_x_1, cost_mat_inv_x_2, cost_mat_inv_x_3, cost_mat_inv_x_4, cost_mat_inv_x_5, cost_mat_inv_x_6, cost_mat_inv_x_7, cost_mat_inv_x_8, cost_mat_inv_x_9, cost_mat_inv_x_10, cost_mat_inv_y_1, cost_mat_inv_y_2, cost_mat_inv_y_3, cost_mat_inv_y_4, cost_mat_inv_y_5, cost_mat_inv_y_6, cost_mat_inv_y_7, cost_mat_inv_y_8, cost_mat_inv_y_9, cost_mat_inv_y_10, cost_mat_inv_z_1, cost_mat_inv_z_2, cost_mat_inv_z_3, cost_mat_inv_z_4, cost_mat_inv_z_5, cost_mat_inv_z_6, cost_mat_inv_z_7, cost_mat_inv_z_8, cost_mat_inv_z_9, cost_mat_inv_z_10, Ax_eq_obs,  bx_eq_obs_4, by_eq_obs_4, bz_eq_obs_4, Ax_eq, rho_w_alpha_init, a_elipse_4, b_elipse_4, c_elipse_4  )

print('comp time for 2 benchmarks with 4 static obstacles =', time.time()-start)

scipy.io.savemat('x_1.mat', {'x_1': x_1})
scipy.io.savemat('y_1.mat', {'y_1': y_1})
scipy.io.savemat('z_1.mat', {'z_1': z_1})

scipy.io.savemat('x_2.mat', {'x_2': x_2})
scipy.io.savemat('y_2.mat', {'y_2': y_2})
scipy.io.savemat('z_2.mat', {'z_2': z_2})

scipy.io.savemat('x_3.mat', {'x_3': x_3})
scipy.io.savemat('y_3.mat', {'y_3': y_3})
scipy.io.savemat('z_3.mat', {'z_3': z_3})

scipy.io.savemat('x_4.mat', {'x_4': x_2})
scipy.io.savemat('y_4.mat', {'y_4': y_2})
scipy.io.savemat('z_4.mat', {'z_4': z_2})


scipy.io.savemat('x_obs_static_1.mat', {'x_obs_static_1': x_obs_static_1})
scipy.io.savemat('y_obs_static_1.mat', {'y_obs_static_1': y_obs_static_1})
scipy.io.savemat('z_obs_static_1.mat', {'z_obs_static_1': z_obs_static_1})

scipy.io.savemat('x_obs_static_2.mat', {'x_obs_static_2': x_obs_static_2})
scipy.io.savemat('y_obs_static_2.mat', {'y_obs_static_2': y_obs_static_2})
scipy.io.savemat('z_obs_static_2.mat', {'z_obs_static_2': z_obs_static_2})

scipy.io.savemat('x_obs_static_3.mat', {'x_obs_static_3': x_obs_static_3})
scipy.io.savemat('y_obs_static_3.mat', {'y_obs_static_3': y_obs_static_3})
scipy.io.savemat('z_obs_static_3.mat', {'z_obs_static_3': z_obs_static_3})

scipy.io.savemat('x_obs_static_4.mat', {'x_obs_static_4': x_obs_static_4})
scipy.io.savemat('y_obs_static_4.mat', {'y_obs_static_4': y_obs_static_4})
scipy.io.savemat('z_obs_static_4.mat', {'z_obs_static_4': z_obs_static_4})


