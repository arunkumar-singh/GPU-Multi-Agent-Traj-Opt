



from numpy import *
from scipy.linalg import block_diag
import time





def compute_obs_mat(P, num, n_rob, n_con):

    nvar = shape(P)[1]
    temp_mat_1 = empty((0, n_rob*nvar), dtype=float, order='C')

    temp_mat_2 = zeros(( num, nvar  ))
    for i in range(1, n_rob):
        temp = hstack(( tile(temp_mat_2, ( n_rob-i, i-1 ) ),  tile(P, (n_rob-i, 1) ), -kron(eye(n_rob-i,dtype=int), P)       ))

        temp_mat_1 = append(temp_mat_1, temp, axis = 0)

    Ax_eq_obs = temp_mat_1

    bx_eq_obs = zeros(n_con*num)
    by_eq_obs = zeros(n_con*num)
    bz_eq_obs = zeros(n_con*num)


    Ay_eq_obs = Ax_eq_obs
    Az_eq_obs = Ax_eq_obs

    Ax_eq_obs = Ax_eq_obs

    return Ax_eq_obs, bx_eq_obs, Ay_eq_obs, by_eq_obs, Az_eq_obs, bz_eq_obs


def compute_pos_matrix( n_rob, n_con, P, Pdot, Pddot  ):

    num = shape(P)[0]
    A_mat = vstack((P[0], Pdot[0], Pddot[0], P[-1], Pdot[-1], Pddot[-1]      ))

    # bx_eq = vstack(( x_init, vx_init, ax_init, x_fin, vx_fin, ax_fin  )).T
    # by_eq = vstack(( y_init, vy_init, ay_init, y_fin, vy_fin, ay_fin  )).T
    # bz_eq = vstack(( z_init, vz_init, az_init, z_fin, vz_fin, az_fin  )).T

    Ax_eq = kron(eye(n_rob,dtype=int), A_mat)
    # Ax_eq = hstack(( Ax_eq, zeros(( shape(Ax_eq)[0], n_con*num   ))  ))
    Ay_eq = Ax_eq
    Az_eq = Ax_eq

    return Ax_eq


def compute_inv_mat(num, n_con, n_rob, P, cost_smoothness_x, cost_smoothness_y, cost_smoothness_z, lincost_smoothness_x, lincost_smoothness_y, lincost_smoothness_z, Ax_eq, Ax_eq_obs, rho_w_alpha):

    nvar = shape(P)[1]
    Ax = Ax_eq
    Ay = Ax_eq
    Az = Ax_eq

    A_w = -Ax_eq_obs

    obj_x = cost_smoothness_x+rho_w_alpha*dot(A_w.T, A_w)
    obj_y = cost_smoothness_y+rho_w_alpha*dot(A_w.T, A_w)
    obj_z = cost_smoothness_z+rho_w_alpha*dot(A_w.T, A_w)

    # obj_y = cost_smoothness+rho_w_alpha*dot(A_w.T, A_w)

    cost_mat_x = vstack((  hstack(( obj_x, Ax.T )), hstack(( Ax, zeros(( shape(Ax)[0], n_rob*6 )) ))         ))
    cost_mat_y = vstack((  hstack(( obj_y, Ay.T )), hstack(( Ay, zeros(( shape(Ax)[0], n_rob*6 )) ))         ))
    cost_mat_z = vstack((  hstack(( obj_z, Az.T )), hstack(( Ax, zeros(( shape(Ax)[0], n_rob*6 )) ))         ))

    # cost_mat_y = vstack((  hstack(( obj_y, Ay.T        )), hstack(( Ay, zeros(( shape(Ay)[0], n_rob*6 )) ))         ))

    return linalg.inv(cost_mat_x), linalg.inv(cost_mat_y), linalg.inv(cost_mat_z)
