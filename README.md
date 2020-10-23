# GPU-Multi-Agent-Traj-Opt
Repository associated with the paper "GPU Accelerated Convex Approximations for Fast Multi-Agent TrajectoryOptimization". 

The paper has been submitted to Robotics and Automation Letters with ICRA 2021 option.

Source-codes will start appearing here from 19th October. 

Contacts: Arun Kumar Singh (aks1812@gmail.com), Fatemeh Rastgar (fatemeh@ut.ee)

Requirements:

1. CUPY (https://docs.cupy.dev/en/stable/install.html)

2. Numpy.

3. Scipy.

4. Jax-Numpy (https://github.com/google/jax).

5. The code has been tested with CUDA version 10.1 and 10.2 on RTX-2080 (8GB) i7-8750 deskptop computer with 32 GB RAM and Nvidia Jetson TX2. A good tutorial to install cuda 10.1 on ubuntu 18.04.5 (https://gist.github.com/Mahedi-61/2a2f1579d4271717d421065168ce6a73)


Running on Google Colab:
Google Colab automatically comes with CUPY and Jax support. So the codes can be run on colab after clonig the repo. A detailed instructions with examples can be found here (https://colab.research.google.com/drive/1soJXHHgqziwHlarbkS6DhLiLTuUravOf?usp=sharing)


How to run the code:

1. For each benchmark, first inverse_matrix_computation.py code in matrix_computation subfolder should be run. These generates the different matrices and inverses required for multi-agent trajectory optimization.

2. The main file to be run for each benchmark is main_x_y.py where x can be 16, 32, 64 etc and y is either cupy or jax. Running this code will create the trajectory mat files for different agents.

3. The trajectory can be visualized by running new_plot.py







