




import numpy as np
import cupy as cp



def compute_x(nvar, num, n_con, n_rob, P, Ax_eq, bx_eq, Ay_eq, by_eq, Az_eq, bz_eq, Ax_eq_obs, bx_eq_obs, Ay_eq_obs, by_eq_obs, Az_eq_obs, bz_eq_obs, a, d_obs_ij, alpha_ij, beta_ij, lamda_x, lamda_y, lamda_z,  rho_w_alpha, cost_mat_inv_x, cost_mat_inv_y, cost_mat_inv_z):

    A_w = Ax_eq_obs

    aug_term = cp.vstack(( bx_eq_obs+a*cp.ones(num*n_con)*d_obs_ij*cp.cos(alpha_ij)*cp.sin(beta_ij)-lamda_x/rho_w_alpha,   by_eq_obs+a*cp.ones(num*n_con)*d_obs_ij*cp.sin(alpha_ij)*cp.sin(beta_ij)-lamda_y/rho_w_alpha, bz_eq_obs+a*cp.ones(num*n_con)*d_obs_ij*cp.cos(beta_ij)-lamda_z/rho_w_alpha  ))

    linterm_augment = -rho_w_alpha*cp.dot(A_w.T, aug_term.T ).T

    lincost_mat = cp.hstack(( -linterm_augment, cp.vstack(( bx_eq, by_eq, bz_eq  ))   ))

    sol_x = cp.dot(cost_mat_inv_x, lincost_mat[0])
    sol_y = cp.dot(cost_mat_inv_y, lincost_mat[1])
    sol_z = cp.dot(cost_mat_inv_z, lincost_mat[2])

    ################## from here
    primal_sol_x = sol_x[0:n_rob*nvar]
    primal_sol_y = sol_y[0:n_rob*nvar]
    primal_sol_z = sol_z[0:n_rob*nvar]

    ##############computing x

    cx = primal_sol_x[0:n_rob*nvar]
    cx = cx.reshape(n_rob, nvar)
    x = cp.dot(P, cx.T).T
    wc_alpha = cp.dot(A_w, primal_sol_x)-bx_eq_obs ### xi-xj

    ############computing y 

    cy = primal_sol_y[0:n_rob*nvar]
    cy = cy.reshape(n_rob, nvar)
    y = cp.dot(P, cy.T).T
    ws_alpha = cp.dot(A_w, primal_sol_y)-by_eq_obs ### yi-yj
    alpha_ij = cp.arctan2( ws_alpha, wc_alpha )

    ############computing z

    cz = primal_sol_z[0:n_rob*nvar]
    cz = cz.reshape(n_rob, nvar)
    z = cp.dot(P, cz.T).T

    ####################################

    wc_beta = cp.dot(A_w, primal_sol_z)-bz_eq_obs
    ws_beta = (cp.dot(A_w, primal_sol_x)-bx_eq_obs)/cp.cos(alpha_ij)

    beta_ij = cp.arctan2( ws_beta, wc_beta )

    return x, y, z, wc_alpha, ws_alpha, alpha_ij, wc_beta, ws_beta, beta_ij

def compute_dobs(n_con, num_horizon, rho_w_alpha, alpha_ij, beta_ij, lamda_x, lamda_y, lamda_z, a, b, wc_alpha, ws_alpha, wc_beta, ws_beta):

    c1_d = 1.0*a**2*rho_w_alpha
    c2_d = 1.0*a*(lamda_x*cp.cos(alpha_ij)*cp.sin(beta_ij) + lamda_y*cp.sin(alpha_ij)*cp.sin(beta_ij) + lamda_z*cp.cos(beta_ij)+ rho_w_alpha*wc_alpha*cp.cos(alpha_ij)*cp.sin(beta_ij) + rho_w_alpha*ws_alpha*cp.sin(alpha_ij)*cp.sin(beta_ij) +rho_w_alpha*wc_beta*cp.cos(beta_ij))


    d_temp_1 = c2_d[0:n_con*num_horizon]/c1_d
    d_temp = d_temp_1
    d_obs_ij = cp.maximum(cp.ones((n_con)*num_horizon), d_temp   )


    res_x = wc_alpha-a*d_obs_ij*cp.cos(alpha_ij)*cp.sin(beta_ij)
    res_y = ws_alpha-a*d_obs_ij*cp.sin(alpha_ij)*cp.sin(beta_ij)
    res_z = wc_beta-a*d_obs_ij*cp.cos(beta_ij)

    lamda_x = lamda_x+res_x*rho_w_alpha
    lamda_y = lamda_y+res_y*rho_w_alpha
    lamda_z = lamda_z+res_z*rho_w_alpha

    return d_obs_ij, lamda_x, lamda_y, lamda_z, res_x, res_y, res_z
