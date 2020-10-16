
import cupy as cp
import numpy as np
import bernstein_coeff_order10_arbitinterval
import scipy
from scipy.io import loadmat
import time
import init_final_pos
import optim_cupy
import init_final_pos


def main_cupy(x_init, y_init, z_init, x_fin, y_fin, z_fin, a, b, c, cost_mat_inv_x_1, cost_mat_inv_x_2, cost_mat_inv_x_3, cost_mat_inv_x_4, cost_mat_inv_x_5, cost_mat_inv_x_6, cost_mat_inv_x_7, cost_mat_inv_x_8, cost_mat_inv_x_9, cost_mat_inv_x_10, cost_mat_inv_y_1, cost_mat_inv_y_2, cost_mat_inv_y_3, cost_mat_inv_y_4, cost_mat_inv_y_5, cost_mat_inv_y_6, cost_mat_inv_y_7, cost_mat_inv_y_8, cost_mat_inv_y_9, cost_mat_inv_y_10, cost_mat_inv_z_1, cost_mat_inv_z_2, cost_mat_inv_z_3, cost_mat_inv_z_4, cost_mat_inv_z_5, cost_mat_inv_z_6, cost_mat_inv_z_7, cost_mat_inv_z_8, cost_mat_inv_z_9, cost_mat_inv_z_10, Ax_eq_obs, Ax_eq, rho_w_alpha_init  ):

	n_rob = 8

	vx_init = np.zeros(n_rob)
	vy_init = np.zeros(n_rob)
	vz_init = np.zeros(n_rob)
	ax_init = np.zeros(n_rob)
	ay_init = np.zeros(n_rob)
	az_init = np.zeros(n_rob)

	vx_fin = np.zeros(n_rob)
	vy_fin = np.zeros(n_rob)
	vz_fin = np.zeros(n_rob)
	ax_fin = np.zeros(n_rob)
	ay_fin = np.zeros(n_rob)
	az_fin = np.zeros(n_rob)


	bx_eq = np.vstack(( x_init, vx_init, ax_init, x_fin, vx_fin, ax_fin  )).T
	by_eq = np.vstack(( y_init, vy_init, ay_init, y_fin, vy_fin, ay_fin  )).T
	bz_eq = np.vstack(( z_init, vz_init, az_init, z_fin, vz_fin, az_fin  )).T

	maxiter = 200



	a_init = a

	a_ellipse = a
	b_ellipse = b
	c_ellipse = c


	t_fin =  10.0
	num_horizon = 100
	nn = 100
	num =num_horizon
	t = t_fin/num_horizon
	tot_time = np.linspace(0.0, t_fin, num_horizon)
	tot_time_copy = tot_time.reshape(num_horizon,1)

	P, Pdot, Pddot = bernstein_coeff_order10_arbitinterval.bernstein_coeff_order10_new(10, tot_time_copy[0], tot_time_copy[-1], tot_time_copy)
	#####################################
	nvar = np.shape(P)[1]

	n_con = int(scipy.special.binom(n_rob,2))

	P, Pdot, Pddot = bernstein_coeff_order10_arbitinterval.bernstein_coeff_order10_new(10, tot_time_copy[0], tot_time_copy[-1], tot_time_copy)
	#####################################
	nvar = np.shape(P)[1]
	n_con = int(scipy.special.binom(n_rob,2))


	alpha_ij = cp.zeros((n_con)*num_horizon)
	beta_ij = cp.zeros((n_con)*num_horizon)
	d_obs_ij = cp.ones((n_con)*num_horizon)

	lamda_x = cp.ones((n_con)*num_horizon)
	lamda_y = cp.ones((n_con)*num_horizon)
	lamda_z = cp.ones((n_con)*num_horizon)


	P = cp.asarray(P)
	Pdot = cp.asarray(Pdot)
	Pddot = cp.asarray(Pddot)

	Ay_eq = Ax_eq
	Az_eq = Ax_eq


	bx_eq = bx_eq.reshape(n_rob*6)
	by_eq = by_eq.reshape(n_rob*6)
	bz_eq = bz_eq.reshape(n_rob*6)

	Ay_eq_obs = Ax_eq_obs
	Az_eq_obs = Ax_eq_obs

	bx_eq_obs = cp.zeros((n_con)*num_horizon)
	by_eq_obs = bx_eq_obs
	bz_eq_obs = bx_eq_obs

	start = time.time()

	for i in range(0, maxiter):

	    if(i<=0.1*maxiter):
	        rho_w_alpha = rho_w_alpha_init[0]
	        x, y,z, wc_alpha, ws_alpha, alpha_ij, wc_beta, ws_beta, beta_ij = optim_cupy.compute_x(nvar, num, n_con, n_rob, P, Ax_eq, bx_eq, Ay_eq, by_eq, Az_eq, bz_eq, Ax_eq_obs, bx_eq_obs, Ay_eq_obs, by_eq_obs, Az_eq_obs, bz_eq_obs, a, d_obs_ij, alpha_ij, beta_ij, lamda_x, lamda_y, lamda_z, rho_w_alpha, cost_mat_inv_x_1,  cost_mat_inv_y_1, cost_mat_inv_z_1)

	    if(i>0.1*maxiter and i<=0.2*maxiter ):
	        rho_w_alpha = rho_w_alpha_init[1]
	        x, y,z, wc_alpha, ws_alpha, alpha_ij, wc_beta, ws_beta, beta_ij = optim_cupy.compute_x(nvar, num, n_con, n_rob, P, Ax_eq, bx_eq, Ay_eq, by_eq, Az_eq, bz_eq, Ax_eq_obs, bx_eq_obs, Ay_eq_obs, by_eq_obs, Az_eq_obs, bz_eq_obs, a, d_obs_ij, alpha_ij, beta_ij, lamda_x, lamda_y, lamda_z, rho_w_alpha,  cost_mat_inv_x_2, cost_mat_inv_y_2, cost_mat_inv_z_2)


	    if(i>0.2*maxiter and i<=0.3*maxiter ):
	        rho_w_alpha = rho_w_alpha_init[2]
	        x, y,z, wc_alpha, ws_alpha, alpha_ij, wc_beta, ws_beta, beta_ij = optim_cupy.compute_x(nvar, num, n_con, n_rob, P, Ax_eq, bx_eq, Ay_eq, by_eq, Az_eq, bz_eq, Ax_eq_obs, bx_eq_obs, Ay_eq_obs, by_eq_obs, Az_eq_obs, bz_eq_obs, a, d_obs_ij, alpha_ij, beta_ij, lamda_x, lamda_y, lamda_z, rho_w_alpha,  cost_mat_inv_x_3,  cost_mat_inv_y_3, cost_mat_inv_z_3)


	    if(i>0.3*maxiter and i<=0.4*maxiter ):
	        rho_w_alpha = rho_w_alpha_init[3]
	        x, y,z, wc_alpha, ws_alpha, alpha_ij, wc_beta, ws_beta, beta_ij = optim_cupy.compute_x(nvar, num, n_con, n_rob, P, Ax_eq, bx_eq, Ay_eq, by_eq, Az_eq, bz_eq, Ax_eq_obs, bx_eq_obs, Ay_eq_obs, by_eq_obs, Az_eq_obs, bz_eq_obs, a, d_obs_ij, alpha_ij, beta_ij, lamda_x, lamda_y, lamda_z, rho_w_alpha, cost_mat_inv_x_4, cost_mat_inv_y_4, cost_mat_inv_z_4)


	    if(i>0.4*maxiter and i<=0.5*maxiter ):
	        rho_w_alpha = rho_w_alpha_init[4]
	        x, y,z, wc_alpha, ws_alpha, alpha_ij, wc_beta, ws_beta, beta_ij = optim_cupy.compute_x(nvar, num, n_con, n_rob, P, Ax_eq, bx_eq, Ay_eq, by_eq, Az_eq, bz_eq, Ax_eq_obs, bx_eq_obs, Ay_eq_obs, by_eq_obs, Az_eq_obs, bz_eq_obs, a, d_obs_ij, alpha_ij, beta_ij, lamda_x, lamda_y, lamda_z, rho_w_alpha, cost_mat_inv_x_5, cost_mat_inv_y_5, cost_mat_inv_z_5 )


	    if(i>0.5*maxiter and i<=0.6*maxiter ):
	        rho_w_alpha = rho_w_alpha_init[5]
	        x, y,z, wc_alpha, ws_alpha, alpha_ij, wc_beta, ws_beta, beta_ij = optim_cupy.compute_x(nvar, num, n_con, n_rob, P, Ax_eq, bx_eq, Ay_eq, by_eq, Az_eq, bz_eq, Ax_eq_obs, bx_eq_obs, Ay_eq_obs, by_eq_obs, Az_eq_obs, bz_eq_obs, a, d_obs_ij, alpha_ij, beta_ij, lamda_x, lamda_y, lamda_z, rho_w_alpha, cost_mat_inv_x_6, cost_mat_inv_y_6, cost_mat_inv_z_6)

	    if(i>0.6*maxiter and i<=0.7*maxiter ):
	        rho_w_alpha = rho_w_alpha_init[6]
	        x, y,z, wc_alpha, ws_alpha, alpha_ij, wc_beta, ws_beta, beta_ij = optim_cupy.compute_x(nvar, num, n_con, n_rob, P, Ax_eq, bx_eq, Ay_eq, by_eq, Az_eq, bz_eq, Ax_eq_obs, bx_eq_obs, Ay_eq_obs, by_eq_obs, Az_eq_obs, bz_eq_obs, a, d_obs_ij, alpha_ij, beta_ij, lamda_x, lamda_y, lamda_z, rho_w_alpha, cost_mat_inv_x_7, cost_mat_inv_y_7, cost_mat_inv_z_7)

	    if(i>0.7*maxiter and i<=0.8*maxiter ):
	        rho_w_alpha = rho_w_alpha_init[7]
	        x, y,z, wc_alpha, ws_alpha, alpha_ij, wc_beta, ws_beta, beta_ij = optim_cupy.compute_x(nvar, num, n_con, n_rob,  P, Ax_eq, bx_eq, Ay_eq, by_eq, Az_eq, bz_eq, Ax_eq_obs, bx_eq_obs, Ay_eq_obs, by_eq_obs, Az_eq_obs, bz_eq_obs, a, d_obs_ij, alpha_ij, beta_ij, lamda_x, lamda_y, lamda_z, rho_w_alpha, cost_mat_inv_x_8, cost_mat_inv_y_8, cost_mat_inv_z_8)

	    if(i>0.8*maxiter and i<=0.9*maxiter ):
	        rho_w_alpha = rho_w_alpha_init[8]
	        x, y,z, wc_alpha, ws_alpha, alpha_ij, wc_beta, ws_beta, beta_ij = optim_cupy.compute_x(nvar, num, n_con, n_rob,  P, Ax_eq, bx_eq, Ay_eq, by_eq, Az_eq, bz_eq, Ax_eq_obs, bx_eq_obs, Ay_eq_obs, by_eq_obs, Az_eq_obs, bz_eq_obs, a, d_obs_ij, alpha_ij, beta_ij, lamda_x, lamda_y, lamda_z, rho_w_alpha, cost_mat_inv_x_9, cost_mat_inv_y_9, cost_mat_inv_z_9)


	    if(i>0.9*maxiter and i<=maxiter ):
	        rho_w_alpha = rho_w_alpha_init[9]
	        x, y,z, wc_alpha, ws_alpha, alpha_ij, wc_beta, ws_beta, beta_ij = optim_cupy.compute_x(nvar, num, n_con, n_rob, P, Ax_eq, bx_eq, Ay_eq, by_eq, Az_eq, bz_eq, Ax_eq_obs, bx_eq_obs, Ay_eq_obs, by_eq_obs, Az_eq_obs, bz_eq_obs, a, d_obs_ij, alpha_ij, beta_ij, lamda_x, lamda_y, lamda_z, rho_w_alpha, cost_mat_inv_x_10, cost_mat_inv_y_10, cost_mat_inv_z_10)



	    d_obs_ij, lamda_x, lamda_y, lamda_z, res_x, res_y, res_z = optim_cupy.compute_dobs(n_con, num, rho_w_alpha, alpha_ij, beta_ij, lamda_x, lamda_y, lamda_z, a, b, wc_alpha, ws_alpha, wc_beta, ws_beta)


	    if(cp.max(cp.abs(res_x))<0.02 and cp.max(cp.abs(res_y))<0.02 and cp.max(cp.abs(res_z))<0.02 ):
	        break

	print(cp.max(res_x), cp.max(res_y), cp.max(res_z))


	return x, y, z


