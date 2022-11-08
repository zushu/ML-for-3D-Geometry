"""Triangle Meshes to Point Clouds"""
import numpy as np


def sample_point_cloud(vertices, faces, n_points):
    """
    Sample n_points uniformly from the mesh represented by vertices and faces
    :param vertices: Nx3 numpy array of mesh vertices
    :param faces: Mx3 numpy array of mesh faces
    :param n_points: number of points to be sampled
    :return: sampled points, a numpy array of shape (n_points, 3)
    """

    # ###############
    # TODO: Implement
#    raise NotImplementedError
    sampled_points = np.empty((n_points, 3))
    num_faces = faces.shape[0]
    
    # TODO: FIND PROBABILITY OF SAMPLING A TRIANGLE FROM ITS SURFACE AREA 
    # then USE n_points, how many points to sample from each triangle acc.to the probability 
    # I AM FED UP I WISH I DID THIS WITH A PARTNER 
    # PSEUDOCODE
#    for i in range(n_points):
        # barycentric coords calc
 #       sqrt_r_1 = np.sqrt(np.random.rand()) # sqrt is used for barycentric coord formulas
  #      r_2 = np.random.rand()
   #     u = 1-sqrt_r_1
    #    v = sqrt_r_1*(1-r_2)
     #   w = sqrt_r_1*r_2
    
#        np.random.choice(num_faces)


    # ###############

def surface_area(p1, p2, p3):
    # i did this calc in CG course before 
    # use 3rd formula from this link https://math.stackexchange.com/questions/128991/how-to-calculate-the-area-of-a-3d-triangle
