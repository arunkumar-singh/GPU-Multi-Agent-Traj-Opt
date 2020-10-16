





from numpy import *
import matplotlib.pyplot as plt
import scipy.special
import bernstein_coeff_order10_arbitinterval
import time
import scipy.io
from scipy import interpolate
from scipy.io import loadmat
import scipy.special
import optim_inv_mat_computation
import scipy.io
from scipy.io import loadmat
from scipy.linalg import block_diag

maxiter = 100

t_fin =  10.0
num_horizon = 100
nn = 100
num =num_horizon
t = t_fin/num_horizon
tot_time = linspace(0.0, t_fin, num_horizon)
tot_time_copy = tot_time.reshape(num_horizon,1)

P, Pdot, Pddot = bernstein_coeff_order10_arbitinterval.bernstein_coeff_order10_new(10, tot_time_copy[0], tot_time_copy[-1], tot_time_copy)

nvar = shape(P)[1]

##################################################
n_rob = 8
n_con = int(scipy.special.binom(n_rob,2))

##################################
weight_x = 100
weight_y = 100
weight_z = 3000
######################################

alpha_ij = zeros((n_con)*num_horizon)
beta_ij = zeros((n_con)*num_horizon)
d_obs_ij = ones((n_con)*num_horizon)


lamda_wc = ones((n_con)*num_horizon)
lamda_ws = ones((n_con)*num_horizon)


rho_w_alpha = 7
rho_w_alpha_init_1 = rho_w_alpha
rho_w_alpha_init_2 = rho_w_alpha*4.2
rho_w_alpha_init_3 = rho_w_alpha*4.2**2
rho_w_alpha_init_4 = rho_w_alpha*4.2**3
rho_w_alpha_init_5 = rho_w_alpha*4.2**4
rho_w_alpha_init_6 = rho_w_alpha*4.2**5
rho_w_alpha_init_7 = rho_w_alpha*6.2**6
rho_w_alpha_init_8 = rho_w_alpha*6.2**7
rho_w_alpha_init_9 = rho_w_alpha*6.2**8
rho_w_alpha_init_10 = rho_w_alpha*6.2**9

res_w_alpha = ones(maxiter)
res_w_beta = ones(maxiter)


cost_smoothness_individual_x = weight_x*dot(Pddot.T, Pddot   )
cost_smoothness_individual_y = weight_y*dot(Pddot.T, Pddot   )
cost_smoothness_individual_z = weight_z*dot(Pddot.T, Pddot   )

cost_smoothness_x = kron(eye(n_rob,dtype=int), cost_smoothness_individual_x)
cost_smoothness_y = kron(eye(n_rob,dtype=int), cost_smoothness_individual_y)
cost_smoothness_z = kron(eye(n_rob,dtype=int), cost_smoothness_individual_z)


lincost_smoothness_x = zeros(n_rob*nvar)
lincost_smoothness_y = zeros(n_rob*nvar)
lincost_smoothness_z = zeros(n_rob*nvar)

Ax_eq_obs, bx_eq_obs, Ay_eq_obs, by_eq_obs, Az_eq_obs, bz_eq_obs = optim_inv_mat_computation.compute_obs_mat(P, num, n_rob, n_con)

Ax_eq = optim_inv_mat_computation.compute_pos_matrix( n_rob, n_con, P, Pdot, Pddot )

cost_mat_inv_x_1, cost_mat_inv_y_1, cost_mat_inv_z_1 = optim_inv_mat_computation.compute_inv_mat(num, n_con, n_rob, P, cost_smoothness_x, cost_smoothness_y, cost_smoothness_z, lincost_smoothness_x, lincost_smoothness_y, lincost_smoothness_z, Ax_eq, Ax_eq_obs, rho_w_alpha_init_1 )
cost_mat_inv_x_2, cost_mat_inv_y_2, cost_mat_inv_z_2 = optim_inv_mat_computation.compute_inv_mat(num, n_con, n_rob, P, cost_smoothness_x, cost_smoothness_y, cost_smoothness_z, lincost_smoothness_x, lincost_smoothness_y,  lincost_smoothness_z, Ax_eq, Ax_eq_obs, rho_w_alpha_init_2 )
cost_mat_inv_x_3, cost_mat_inv_y_3, cost_mat_inv_z_3 = optim_inv_mat_computation.compute_inv_mat(num, n_con, n_rob, P, cost_smoothness_x, cost_smoothness_y, cost_smoothness_z, lincost_smoothness_x, lincost_smoothness_y,  lincost_smoothness_z, Ax_eq, Ax_eq_obs, rho_w_alpha_init_3 )
cost_mat_inv_x_4, cost_mat_inv_y_4, cost_mat_inv_z_4 = optim_inv_mat_computation.compute_inv_mat(num, n_con, n_rob, P, cost_smoothness_x, cost_smoothness_y, cost_smoothness_z, lincost_smoothness_x, lincost_smoothness_y,  lincost_smoothness_z, Ax_eq, Ax_eq_obs, rho_w_alpha_init_4 )
cost_mat_inv_x_5, cost_mat_inv_y_5, cost_mat_inv_z_5 = optim_inv_mat_computation.compute_inv_mat(num, n_con, n_rob, P, cost_smoothness_x, cost_smoothness_y, cost_smoothness_z, lincost_smoothness_x, lincost_smoothness_y,  lincost_smoothness_z, Ax_eq, Ax_eq_obs, rho_w_alpha_init_5 )
cost_mat_inv_x_6, cost_mat_inv_y_6, cost_mat_inv_z_6 = optim_inv_mat_computation.compute_inv_mat(num, n_con, n_rob, P, cost_smoothness_x, cost_smoothness_y, cost_smoothness_z, lincost_smoothness_x, lincost_smoothness_y,  lincost_smoothness_z, Ax_eq, Ax_eq_obs, rho_w_alpha_init_6 )
cost_mat_inv_x_7, cost_mat_inv_y_7, cost_mat_inv_z_7 = optim_inv_mat_computation.compute_inv_mat(num, n_con, n_rob, P, cost_smoothness_x, cost_smoothness_y, cost_smoothness_z, lincost_smoothness_x, lincost_smoothness_y,  lincost_smoothness_z, Ax_eq, Ax_eq_obs, rho_w_alpha_init_7 )
cost_mat_inv_x_8, cost_mat_inv_y_8, cost_mat_inv_z_8 = optim_inv_mat_computation.compute_inv_mat(num, n_con, n_rob, P, cost_smoothness_x, cost_smoothness_y, cost_smoothness_z, lincost_smoothness_x, lincost_smoothness_y,  lincost_smoothness_z, Ax_eq, Ax_eq_obs, rho_w_alpha_init_8 )
cost_mat_inv_x_9, cost_mat_inv_y_9, cost_mat_inv_z_9 = optim_inv_mat_computation.compute_inv_mat(num, n_con, n_rob, P, cost_smoothness_x, cost_smoothness_y, cost_smoothness_z, lincost_smoothness_x, lincost_smoothness_y,  lincost_smoothness_z, Ax_eq, Ax_eq_obs, rho_w_alpha_init_9 )
cost_mat_inv_x_10, cost_mat_inv_y_10, cost_mat_inv_z_10 = optim_inv_mat_computation.compute_inv_mat(num, n_con, n_rob, P, cost_smoothness_x, cost_smoothness_y, cost_smoothness_z, lincost_smoothness_x, lincost_smoothness_y, lincost_smoothness_z,  Ax_eq, Ax_eq_obs, rho_w_alpha_init_10 )
rho_w_alpha_init = hstack(( rho_w_alpha_init_1, rho_w_alpha_init_2, rho_w_alpha_init_3, rho_w_alpha_init_4, rho_w_alpha_init_5, rho_w_alpha_init_6, rho_w_alpha_init_7, rho_w_alpha_init_8, rho_w_alpha_init_9, rho_w_alpha_init_10   ))


scipy.io.savemat('cost_mat_inv_x_1_dynobs_2.mat', {'inv_1': cost_mat_inv_x_1})
scipy.io.savemat('cost_mat_inv_x_2_dynobs_2.mat', {'inv_2': cost_mat_inv_x_2})
scipy.io.savemat('cost_mat_inv_x_3_dynobs_2.mat', {'inv_3': cost_mat_inv_x_3})
scipy.io.savemat('cost_mat_inv_x_4_dynobs_2.mat', {'inv_4': cost_mat_inv_x_4})
scipy.io.savemat('cost_mat_inv_x_5_dynobs_2.mat', {'inv_5': cost_mat_inv_x_5})
scipy.io.savemat('cost_mat_inv_x_6_dynobs_2.mat', {'inv_6': cost_mat_inv_x_6})
scipy.io.savemat('cost_mat_inv_x_7_dynobs_2.mat', {'inv_7': cost_mat_inv_x_7})
scipy.io.savemat('cost_mat_inv_x_8_dynobs_2.mat', {'inv_8': cost_mat_inv_x_8})
scipy.io.savemat('cost_mat_inv_x_9_dynobs_2.mat', {'inv_9': cost_mat_inv_x_9})
scipy.io.savemat('cost_mat_inv_x_10_dynobs_2.mat', {'inv_10': cost_mat_inv_x_10})
scipy.io.savemat('rho_w_alpha_init_dynobs_2.mat', {'rho_w_alpha_init': rho_w_alpha_init})

scipy.io.savemat('cost_mat_inv_y_1_dynobs_2.mat', {'inv_1': cost_mat_inv_y_1})
scipy.io.savemat('cost_mat_inv_y_2_dynobs_2.mat', {'inv_2': cost_mat_inv_y_2})
scipy.io.savemat('cost_mat_inv_y_3_dynobs_2.mat', {'inv_3': cost_mat_inv_y_3})
scipy.io.savemat('cost_mat_inv_y_4_dynobs_2.mat', {'inv_4': cost_mat_inv_y_4})
scipy.io.savemat('cost_mat_inv_y_5_dynobs_2.mat', {'inv_5': cost_mat_inv_y_5})
scipy.io.savemat('cost_mat_inv_y_6_dynobs_2.mat', {'inv_6': cost_mat_inv_y_6})
scipy.io.savemat('cost_mat_inv_y_7_dynobs_2.mat', {'inv_7': cost_mat_inv_y_7})
scipy.io.savemat('cost_mat_inv_y_8_dynobs_2.mat', {'inv_8': cost_mat_inv_y_8})
scipy.io.savemat('cost_mat_inv_y_9_dynobs_2.mat', {'inv_9': cost_mat_inv_y_9})
scipy.io.savemat('cost_mat_inv_y_10_dynobs_2.mat', {'inv_10': cost_mat_inv_y_10})


scipy.io.savemat('cost_mat_inv_z_1_dynobs_2.mat', {'inv_1': cost_mat_inv_z_1})
scipy.io.savemat('cost_mat_inv_z_2_dynobs_2.mat', {'inv_2': cost_mat_inv_z_2})
scipy.io.savemat('cost_mat_inv_z_3_dynobs_2.mat', {'inv_3': cost_mat_inv_z_3})
scipy.io.savemat('cost_mat_inv_z_4_dynobs_2.mat', {'inv_4': cost_mat_inv_z_4})
scipy.io.savemat('cost_mat_inv_z_5_dynobs_2.mat', {'inv_5': cost_mat_inv_z_5})
scipy.io.savemat('cost_mat_inv_z_6_dynobs_2.mat', {'inv_6': cost_mat_inv_z_6})
scipy.io.savemat('cost_mat_inv_z_7_dynobs_2.mat', {'inv_7': cost_mat_inv_z_7})
scipy.io.savemat('cost_mat_inv_z_8_dynobs_2.mat', {'inv_8': cost_mat_inv_z_8})
scipy.io.savemat('cost_mat_inv_z_9_dynobs_2.mat', {'inv_9': cost_mat_inv_z_9})
scipy.io.savemat('cost_mat_inv_z_10_dynobs_2.mat', {'inv_10': cost_mat_inv_z_10})

scipy.io.savemat('rho_w_alpha_init_dynobs_2.mat', {'rho_w_alpha_init': rho_w_alpha_init})

scipy.io.savemat('Ax_eq.mat', {'Ax_eq': Ax_eq})
scipy.io.savemat('Ax_eq_obs.mat', {'Ax_eq_obs': Ax_eq_obs})




