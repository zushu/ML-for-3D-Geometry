"""Export to disk"""


def export_mesh_to_obj(path, vertices, faces):
    """
    exports mesh as OBJ
    :param path: output path for the OBJ file
    :param vertices: Nx3 vertices
    :param faces: Mx3 faces
    :return: None
    """

    # write vertices starting with "v "
    # write faces starting with "f "

    # ###############
    # TODO: Implement
#    raise NotImplementedError
    with open(path, 'a') as obj_file:
        for v in vertices:
            obj_file.write("v %f %f %f\n" % (v[0], v[1], v[2]))

        for m in faces:
            obj_file.write("f %d %d %d\n" % (m[0]+1, m[1]+1, m[2]+1))
    # ###############


def export_pointcloud_to_obj(path, pointcloud):
    """
    export pointcloud as OBJ
    :param path: output path for the OBJ file
    :param pointcloud: Nx3 points
    :return: None
    """

    # ###############
    # TODO: Implement
    raise NotImplementedError
    # ###############
