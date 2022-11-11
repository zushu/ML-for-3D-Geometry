""" Procrustes Aligment for point clouds """
import numpy as np
from pathlib import Path


def procrustes_align(pc_x, pc_y):
    """
    calculate the rigid transform to go from point cloud pc_x to point cloud pc_y, assuming points are corresponding
    :param pc_x: Nx3 input point cloud
    :param pc_y: Nx3 target point cloud, corresponding to pc_x locations
    :return: rotation (3, 3) and translation (3,) needed to go from pc_x to pc_y
    """
    R = np.zeros((3, 3), dtype=np.float32)
    t = np.zeros((3,), dtype=np.float32)

    # TODO: Your implementation starts here ###############
    # 1. get centered pc_x and centered pc_y
    centroid_x = np.mean(pc_x, axis=0)
    pc_x_c = np.subtract(pc_x,centroid_x)
    centroid_y = np.mean(pc_y, axis=0)
    pc_y_c = np.subtract(pc_y, centroid_y)
    
    # 2. create X and Y both of shape 3XN by reshaping centered pc_x, centered pc_y
    X = np.transpose(pc_x_c)
    Y = np.transpose(pc_y_c)
    # 3. estimate rotation
    # M = Y*X_T 
    u, s, vh = np.linalg.svd(np.dot(Y,pc_x_c), full_matrices=False)
    # det(v) = det(vh) because v is a square matrix
    S = np.identity(3)
    if np.linalg.det(u)*np.linalg.det(vh) != 1:
        S[2, 2] = -1
    
    R = np.matmul(np.matmul(u,S),vh) 
    # 4. estimate translation
    t = centroid_y - np.matmul(R, centroid_x)
    # R and t should now contain the rotation (shape 3x3) and translation (shape 3,)
    # TODO: Your implementation ends here ###############

    t_broadcast = np.broadcast_to(t[:, np.newaxis], (3, pc_x.shape[0]))

    return R, t


def load_correspondences():
    """
    loads correspondences between meshes from disk
    """

    load_obj_as_np = lambda path: np.array(list(map(lambda x: list(map(float, x.split(' ')[1:4])), path.read_text().splitlines())))
    path_x = (Path(__file__).parent / "resources" / "points_input.obj").absolute()
    path_y = (Path(__file__).parent / "resources" / "points_target.obj").absolute()
    return load_obj_as_np(path_x), load_obj_as_np(path_y)
