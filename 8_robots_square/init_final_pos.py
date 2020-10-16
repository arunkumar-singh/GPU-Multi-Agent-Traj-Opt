

from numpy import *

def init_final_pos():

	x_init_1 = 4.0
	y_init_1 = 0.0
	z_init_1 = 1.0

	x_fin_1 = -4.0
	y_fin_1 = 0.0
	z_fin_1 = 1.0

	x_init_2 = 4.0
	y_init_2 = 4.0
	z_init_2 = 1.0

	x_fin_2 = -4.0
	y_fin_2 = -4.0
	z_fin_2 = 1.0

	x_init_3 = 0.0
	y_init_3 = 4.0
	z_init_3 = 1.0

	x_fin_3 = 0.0
	y_fin_3 = -4.0
	z_fin_3 = 1.0

	x_init_4 = -4.0
	y_init_4 = 4.0
	z_init_4 = 1.0

	x_fin_4 = 4.0
	y_fin_4 = -4.0
	z_fin_4 = 1.0

	x_init_5 = -4.0
	y_init_5 = 0.0
	z_init_5 = 1.0

	x_fin_5 = 4.0
	y_fin_5 = 0.0
	z_fin_5 = 1.0

	x_init_6 = -4.0
	y_init_6 = -4.0
	z_init_6 = 1.0

	x_fin_6 = 4.0
	y_fin_6 = 4.0
	z_fin_6 = 1.0

	x_init_7 = 0.0
	y_init_7 = -4.0
	z_init_7 = 1.0

	x_fin_7 = 0.0
	y_fin_7 = 4.0
	z_fin_7 = 1.0

	x_init_8 = 4.0
	y_init_8 = -4.0
	z_init_8 = 1.0

	x_fin_8 = -4.0
	y_fin_8 = 4.0
	z_fin_8 = 1.0


	x_init = hstack(( x_init_1, x_init_2, x_init_3, x_init_4, x_init_5, x_init_6, x_init_7, x_init_8))
	y_init = hstack(( y_init_1, y_init_2, y_init_3, y_init_4, y_init_5, y_init_6, y_init_7, y_init_8))
	z_init = hstack(( z_init_1, z_init_2, z_init_3, z_init_4, z_init_5, z_init_6, z_init_7, z_init_8 ))

	x_fin = hstack(( x_fin_1, x_fin_2, x_fin_3, x_fin_4, x_fin_5, x_fin_6, x_fin_7, x_fin_8))
	y_fin = hstack(( y_fin_1, y_fin_2, y_fin_3, y_fin_4, y_fin_5, y_fin_6, y_fin_7, y_fin_8))
	z_fin = hstack(( z_fin_1, z_fin_2, z_fin_3, z_fin_4, z_fin_5, z_fin_6, z_fin_7, z_fin_8))


	return x_init, y_init, z_init, x_fin, y_fin, z_fin

