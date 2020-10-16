


import jax.numpy as jnp




def compute_x(num, n_con, n_rob, P, Ax_eq, bx_eq, Ay_eq, by_eq, Az_eq, bz_eq, Ax_eq_obs, bx_eq_obs, Ay_eq_obs, by_eq_obs, Az_eq_obs, bz_eq_obs, a, d_obs_ij, alpha_ij, beta_ij, lamda_x, lamda_y, lamda_z,  rho_w_alpha, cost_mat_inv_x, cost_mat_inv_y, cost_mat_inv_z):


    nvar = jnp.shape(P)[1]
    A_w = Ax_eq_obs

    # aug_term = jnp.vstack(( bx_eq_obs+a*jnp.ones(num*n_con)*d_obs_ij*jnp.cos(alpha_ij)*jnp.sin(beta_ij)-lamda_x/rho_w_alpha,   by_eq_obs+a*jnp.ones(num*n_con)*d_obs_ij*jnp.sin(alpha_ij)*jnp.sin(beta_ij)-lamda_y/rho_w_alpha, bz_eq_obs+a*jnp.ones(num*n_con)*d_obs_ij*jnp.cos(beta_ij)-lamda_z/rho_w_alpha  ))

    aug_term = jnp.vstack(( bx_eq_obs+a*d_obs_ij*jnp.cos(alpha_ij)*jnp.sin(beta_ij)-lamda_x/rho_w_alpha,   by_eq_obs+a*d_obs_ij*jnp.sin(alpha_ij)*jnp.sin(beta_ij)-lamda_y/rho_w_alpha, bz_eq_obs+a*d_obs_ij*jnp.cos(beta_ij)-lamda_z/rho_w_alpha  ))


    linterm_augment = -rho_w_alpha*jnp.dot(A_w.T, aug_term.T ).T

    # lincost_mat = jnp.hstack(( -linterm_augment, jnp.vstack(( bx_eq.reshape(n_rob*6), by_eq.reshape(n_rob*6), bz_eq.reshape(n_rob*6)  ))   ))

    lincost_mat = jnp.hstack(( -linterm_augment, jnp.vstack(( bx_eq, by_eq, bz_eq  ))   ))


    # lincost_mat = vstack(( lincost_mat_x, lincost_mat_y    ))

    sol_x = jnp.dot(cost_mat_inv_x, lincost_mat[0])
    sol_y = jnp.dot(cost_mat_inv_y, lincost_mat[1])
    sol_z = jnp.dot(cost_mat_inv_z, lincost_mat[2])

    ################## from here
    # primal_sol_x = sol_x[0:n_rob*nvar]
    # primal_sol_y = sol_y[0:n_rob*nvar]
    # primal_sol_z = sol_z[0:n_rob*nvar]

    primal_sol_x = sol_x[0:64*11]
    primal_sol_y = sol_y[0:64*11]
    primal_sol_z = sol_z[0:64*11]


    # cx = primal_sol_x[0:n_rob*nvar]
    cx = primal_sol_x[0:64*11]

    # cx = cx.reshape(n_rob, nvar)
    cx = cx.reshape(64, 11)

    x = jnp.dot(P, cx.T).T
    wc_alpha = jnp.dot(A_w, primal_sol_x)-bx_eq_obs ### xi-xj

    #print shape(cx)

    # cy = primal_sol_y[0:n_rob*nvar]
    cy = primal_sol_y[0:64*11]

    # cy = cy.reshape(n_rob, nvar)
    cy = cy.reshape(64, 11)

    y = jnp.dot(P, cy.T).T
    ws_alpha = jnp.dot(A_w, primal_sol_y)-by_eq_obs ### yi-yj

    alpha_ij = jnp.arctan2( ws_alpha, wc_alpha )

    # cz = primal_sol_z[0:n_rob*nvar]
    cz = primal_sol_z[0:64*11]

    # cz = cz.reshape(n_rob, nvar)
    cz = cz.reshape(64, 11)

    z = jnp.dot(P, cz.T).T

    wc_beta = jnp.dot(A_w, primal_sol_z)-bz_eq_obs
    ws_beta = (jnp.dot(A_w, primal_sol_x)-bx_eq_obs)/jnp.cos(alpha_ij)

    beta_ij = jnp.arctan2( ws_beta, wc_beta )

    return x, y, z, wc_alpha, ws_alpha, alpha_ij, wc_beta, ws_beta, beta_ij

def compute_dobs(rho_w_alpha, alpha_ij, beta_ij, lamda_x, lamda_y, lamda_z, a, b, wc_alpha, ws_alpha, wc_beta, ws_beta):

    c1_d = 1.0*a**2*rho_w_alpha#*sin(beta_ij[0:num*n_con])**2 + 1.0*a**2*cos(beta_ij[0:num*n_con])**2*rho_w_alpha
    #c1_d_new = 1.0*a_elipse[0]**2*rho_w_alpha#*sin(beta_ij[num*n_con:num*(n_con+n_con_1)])**2 + 1.0*c_elipse[0]**2*cos(beta_ij[num*n_con:num*(n_con+n_con_1)])**2*rho_w_alpha

    c2_d = 1.0*a*(lamda_x*jnp.cos(alpha_ij)*jnp.sin(beta_ij) + lamda_y*jnp.sin(alpha_ij)*jnp.sin(beta_ij) + lamda_z*jnp.cos(beta_ij)+ rho_w_alpha*wc_alpha*jnp.cos(alpha_ij)*jnp.sin(beta_ij) + rho_w_alpha*ws_alpha*jnp.sin(alpha_ij)*jnp.sin(beta_ij) +rho_w_alpha*wc_beta*jnp.cos(beta_ij))


    # d_temp_1 = c2_d[0:n_con*num_horizon]/c1_d

    d_temp_1 = c2_d[0:2016*100]/c1_d

    #d_temp_2 = c2_d[n_con*num_horizon:(n_con+n_con_1)*num_horizon]/c1_d_new

    d_temp = d_temp_1
    # d_obs_ij = jnp.maximum(jnp.ones((n_con)*num_horizon), d_temp   )
    d_obs_ij = jnp.maximum(jnp.ones(2016*100), d_temp   )

    # print(time.time()-start)

    res_x = wc_alpha-a*d_obs_ij*jnp.cos(alpha_ij)*jnp.sin(beta_ij)
    res_y = ws_alpha-a*d_obs_ij*jnp.sin(alpha_ij)*jnp.sin(beta_ij)
    res_z = wc_beta-a*d_obs_ij*jnp.cos(beta_ij)

    lamda_x = lamda_x+res_x*rho_w_alpha
    lamda_y = lamda_y+res_y*rho_w_alpha
    lamda_z = lamda_z+res_z*rho_w_alpha

    return d_obs_ij, lamda_x, lamda_y, lamda_z, res_x, res_y, res_z
