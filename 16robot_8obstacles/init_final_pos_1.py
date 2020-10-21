

from numpy import *

def init_final_pos(n_rob):
	x_init_1 = 4.0
	y_init_1 = 0.0
	z_init_1 = 1.0

	x_fin_1 = -4.0
	y_fin_1 = 0.0
	z_fin_1 = 1.0

	x_init_2 = 4.0
	y_init_2 = 2.0
	z_init_2 = 1.0

	x_fin_2 = -4.0
	y_fin_2 = -2.0
	z_fin_2 = 1.0

	x_init_3 = 4.0
	y_init_3 = 4.0
	z_init_3 = 1.0

	x_fin_3 = -4.0
	y_fin_3 = -4.0
	z_fin_3 = 1.0

	x_init_4 = 2.0
	y_init_4 = 4.0
	z_init_4 = 1.0

	x_fin_4 = -2.0
	y_fin_4 = -4.0
	z_fin_4 = 1.0

	x_init_5 = 0.0
	y_init_5 = 4.0
	z_init_5 = 1.0

	x_fin_5 = 0.0
	y_fin_5 = -4.0
	z_fin_5 = 1.0

	x_init_6 = -2.0
	y_init_6 = 4.0
	z_init_6 = 1.0

	x_fin_6 = 2.0
	y_fin_6 = -4.0
	z_fin_6 = 1.0

	x_init_7 = -4.0
	y_init_7 = 4.0
	z_init_7 = 1.0

	x_fin_7 = 4.0
	y_fin_7 = -4.0 
	z_fin_7 = 1.0

	x_init_8 = -4.0
	y_init_8 = 2.0
	z_init_8 = 1.0

	x_fin_8 = 4.0
	y_fin_8 = -2.0
	z_fin_8 = 1.0


	x_init_9 = -4.0
	y_init_9 = 0.0
	z_init_9 = 1.0

	x_fin_9 = 4.0
	y_fin_9 = 0.0
	z_fin_9 = 1.0

	x_init_10 = -4.0
	y_init_10 = -2.0
	z_init_10 = 1.0

	x_fin_10 = 4.0
	y_fin_10 = 2.0
	z_fin_10 = 1.0

	x_init_11 = -4.0
	y_init_11 = -4.0
	z_init_11 = 1.0

	x_fin_11 = 4.0
	y_fin_11 = 4.0
	z_fin_11 = 1.0

	x_init_12 = -2.0
	y_init_12 = -4.0
	z_init_12 = 1.0

	x_fin_12 = 2.0
	y_fin_12 = 4.0
	z_fin_12 = 1.0

	x_init_13 = 0.0
	y_init_13 = -4.0
	z_init_13 = 1.0

	x_fin_13 = 0.0
	y_fin_13 = 4.0
	z_fin_13 = 1.0

	x_init_14 = 2.0
	y_init_14 = -4.0
	z_init_14 = 1.0

	x_fin_14 = -2.0
	y_fin_14 = 4.0
	z_fin_14 = 1.0

	x_init_15 = 4.0
	y_init_15 = -4.0
	z_init_15 = 1.0

	x_fin_15 = -4.0
	y_fin_15 = 4.0
	z_fin_15 = 1.0

	x_init_16 = 4.0
	y_init_16 = -2.0
	z_init_16 = 1.0

	x_fin_16 = -4.0
	y_fin_16 = 2.0
	z_fin_16 = 1.0



	x_init = hstack(( x_init_1, x_init_2, x_init_3, x_init_4, x_init_5, x_init_6, x_init_7, x_init_8, x_init_9, x_init_10, x_init_11, x_init_12, x_init_13, x_init_14, x_init_15, x_init_16))
	y_init = hstack(( y_init_1, y_init_2, y_init_3, y_init_4, y_init_5, y_init_6, y_init_7, y_init_8, y_init_9, y_init_10, y_init_11, y_init_12, y_init_13, y_init_14, y_init_15, y_init_16))
	z_init = hstack(( z_init_1, z_init_2, z_init_3, z_init_4, z_init_5, z_init_6, z_init_7, z_init_8, z_init_9, z_init_10, z_init_11, z_init_12, z_init_13, z_init_14, z_init_15, z_init_16))


	x_fin = hstack(( x_fin_1, x_fin_2, x_fin_3, x_fin_4, x_fin_5, x_fin_6, x_fin_7, x_fin_8, x_fin_9, x_fin_10, x_fin_11, x_fin_12, x_fin_13, x_fin_14, x_fin_15, x_fin_16))
	y_fin = hstack(( y_fin_1, y_fin_2, y_fin_3, y_fin_4, y_fin_5, y_fin_6, y_fin_7, y_fin_8, y_fin_9, y_fin_10, y_fin_11, y_fin_12, y_fin_13, y_fin_14, y_fin_15, y_fin_16))
	z_fin = hstack(( z_fin_1, z_fin_2, z_fin_3, z_fin_4, z_fin_5, z_fin_6, z_fin_7, z_fin_8, z_fin_9, z_fin_10, z_fin_11, z_fin_12, z_fin_13, z_fin_14, z_fin_15, z_fin_16))

	return x_init, y_init, z_init, x_fin, y_fin, z_fin

