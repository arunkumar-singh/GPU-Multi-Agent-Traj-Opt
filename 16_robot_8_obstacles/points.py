from numpy import *
import scipy.io
from scipy import interpolate
from scipy.io import loadmat



def obstacles_positions():

	min_x = -3.0
	min_y = -3.0
	max_x =  3.0
	max_y =  3.0
	min_z = 0.5
	max_z = 1.2

	min_allowed_distance = 0.8
	num_points = 8

	points_x_init_obs = []
	points_x_fin_obs = []

	points_y_init_obs = []
	points_y_fin_obs = []

	points_z_init_obs = []
	points_z_fin_obs = []


	for i in range (0, 1000):

		random_x_init = random.uniform(min_x, max_x)
		random_x_fin  = random.uniform(min_x, max_x)
		random_y_init = random.uniform(min_y, max_y)
		random_y_fin = random.uniform(min_y, max_y)
		random_z_init = random.uniform(min_z, max_z)
		random_z_fin = random.uniform(min_z, max_z)

		if (i == 0):
			points_x_init_obs.append(random_x_init)
			points_y_init_obs.append(random_y_init)
			points_z_init_obs.append(random_z_init)
		

		
		if (i>0):

			distance_init = sqrt((asarray(points_x_init_obs)-random_x_init)**2+(asarray(points_y_init_obs)-random_y_init)**2+(asarray(points_z_init_obs)-random_z_init)**2)
			distance_init = min(abs(distance_init)) 


			if (distance_init >= min_allowed_distance ):

				points_x_init_obs.append(random_x_init)
				points_y_init_obs.append(random_y_init)
				points_z_init_obs.append(random_z_init)

		if (shape(points_x_init_obs)[0]>num_points-1):

			break

	points_x_init_obs = points_x_init_obs
	points_y_init_obs = points_y_init_obs
	points_z_init_obs = points_z_init_obs

	return points_x_init_obs, points_y_init_obs, points_z_init_obs


		