

from numpy import *

def init_final_pos(n_rob):

	x_init_1 = 8*ones(n_rob//2)
	x_init_2 = -8*ones(n_rob//2)

	x_fin_1 = -8*ones(n_rob//2)
	x_fin_2 = 8*ones(n_rob//2)

	y_init_1 = linspace(-11,11,n_rob//2)
	y_init_2 = linspace(-11,11,n_rob//2)

	y_fin_1 = linspace(-11,11,n_rob//2)
	y_fin_2 = linspace(-11,11,n_rob//2)

	z_init_1 = 2*ones(n_rob//2)
	z_init_2 = 2*ones(n_rob//2)

	z_fin_1 = 2*ones(n_rob//2)
	z_fin_2 = 2*ones(n_rob//2)


	x_init = hstack(( x_init_1, x_init_2))
	y_init = hstack(( y_init_1, y_init_2))
	z_init = hstack(( z_init_1, z_init_2))


	x_fin = hstack(( x_fin_1, x_fin_2))
	y_fin = hstack(( y_fin_1, y_fin_2))
	z_fin = hstack(( z_fin_1, z_fin_2))

	return x_init, y_init, z_init, x_fin, y_fin, z_fin