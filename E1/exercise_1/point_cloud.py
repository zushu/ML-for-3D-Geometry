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
    sampled_points = [] 
    num_faces = faces.shape[0]

    # surface area of each face
    areas = []
    for face in faces:
        # get vertex coords of face
        p1 = vertices[face[0]]
        p2 = vertices[face[1]]
        p3 = vertices[face[2]]
        area_face = surface_area(p1, p2, p3)
        areas.append(area_face)

    areas = np.array(areas)
    # full surface area of mesh
    mesh_area = np.sum(areas)
    # probability of sampling a face: face surface area / mesh surface area 
    areas = areas / mesh_area

    for i in range(n_points):
        # return a random face index 
        face_index = np.random.choice(faces.shape[0], p=areas)
        sampled_face = faces[face_index]
        # vertex coords of sampled face = (A, B, C)
        A = vertices[sampled_face[0]]
        B = vertices[sampled_face[1]]
        C = vertices[sampled_face[2]]
        # barycentric coordinate calculation  
        sqrt_r_1 = np.sqrt(np.random.rand()) # sqrt is used for barycentric coord formulas
        r_2 = np.random.rand()
        u = 1-sqrt_r_1
        v = sqrt_r_1*(1-r_2)
        w = sqrt_r_1*r_2
        sample_point = np.array(u*A + v*B + w*C)
        sampled_points.append(sample_point)
        
    return np.array(sampled_points)
    # ###############

def surface_area(p1, p2, p3):
    # define p1(ax, ay, az), p2(bx, by, bz), p3(cx, cy, cz)
    #two sides of triangle: p1_p2 and p1_p3
    # p1_p2 = (bx- ax, by - ay, bz - az) -> rename as (x1, y1, z1) 
    # p1_p3 = (cx - ax, ...) -> rename as (x2, y2, z2) 
    (x1, y1, z1)= (p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2])  # x1, y1, z1
    (x2, y2, z2)= (p3[0] - p1[0], p3[1] - p1[1], p3[2] - p1[2])  # x2, y2, z2
    # cross product of two sides
    (x3, y3, z3) = (y1*z2 - y2*z1, x1*z2-x2*z1, x1*y2-x2*y1) 
    # area of the triangle
    return np.sqrt(x3**2 + y3**2 + z3**2) / 2.0 
    
