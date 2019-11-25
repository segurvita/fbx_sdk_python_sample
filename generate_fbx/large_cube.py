import sys
from fbx import *


def create_mesh(scene):
    # Create a node for our mesh in the scene.
    mesh_node = FbxNode.Create(scene, "meshNode")

    # Create a mesh.
    mesh = FbxMesh.Create(scene, "mesh")

    # Set the node attribute of the mesh node.
    mesh_node.SetNodeAttribute(mesh)

    # Add the mesh node to the root node in the scene.
    root_node = scene.GetRootNode()
    root_node.AddChild(mesh_node)

    return mesh


def define_control_points(scene, mesh):
    # Define the eight corner of the cube.
    vertex0 = FbxVector4(-50.0, 0.0, 50.0)
    vertex1 = FbxVector4(50.0, 0.0, 50.0)
    vertex2 = FbxVector4(50.0, 100.0, 50.0)
    vertex3 = FbxVector4(-50.0, 100.0, 50.0)
    vertex4 = FbxVector4(-50.0, 0.0, -50.0)
    vertex5 = FbxVector4(50.0, 0.0, -50.0)
    vertex6 = FbxVector4(50.0, 100.0, -50.0)
    vertex7 = FbxVector4(-50.0, 100.0, -50.0)

    # Initialize the control point array of the mesh.
    mesh.InitControlPoints(24)
    control_points = mesh.GetControlPoints()

    # Define each face of the cube.

    # Face 1
    control_points[0] = vertex0
    control_points[1] = vertex1
    control_points[2] = vertex2
    control_points[3] = vertex3

    # Face 2
    control_points[4] = vertex1
    control_points[5] = vertex5
    control_points[6] = vertex6
    control_points[7] = vertex2

    # Face 3
    control_points[8] = vertex5
    control_points[9] = vertex4
    control_points[10] = vertex7
    control_points[11] = vertex6

    # Face 4
    control_points[12] = vertex4
    control_points[13] = vertex0
    control_points[14] = vertex3
    control_points[15] = vertex7

    # Face 5
    control_points[16] = vertex3
    control_points[17] = vertex2
    control_points[18] = vertex6
    control_points[19] = vertex7

    # Face 6
    control_points[20] = vertex1
    control_points[21] = vertex0
    control_points[22] = vertex4
    control_points[23] = vertex5


def assign_normals(scene, mesh):
    # Define normal vectors along each axis.
    normal_x_pos = FbxVector4(1,  0,  0)
    normal_x_neg = FbxVector4(-1,  0,  0)
    normal_y_pos = FbxVector4(0,  1,  0)
    normal_y_neg = FbxVector4(0, -1,  0)
    normal_z_pos = FbxVector4(0,  0,  1)
    normal_z_neg = FbxVector4(0, 0, -1)

    # Create layer 0 for the mesh if it does not already exist.
    layer = mesh.GetLayer(0)
    if layer == None:
        mesh.CreateLayer()
        layer = mesh.GetLayer(0)

    # Create a normal layer.
    layer_element_normal = FbxLayerElementNormal.Create(mesh, "")

    # Set its mapping mode to map each normal vector to each control point.
    layer_element_normal.SetMappingMode(FbxLayerElement.eByControlPoint)

    # Set the reference mode of so that the nth element of the normal array maps to the nth element of the control point array.
    layer_element_normal.SetReferenceMode(FbxLayerElement.eDirect)

    # Assign the normal vectors in the same order the control points were defined for the mesh.
    # Face 1
    layer_element_normal.GetDirectArray().Add(normal_z_pos)
    layer_element_normal.GetDirectArray().Add(normal_z_pos)
    layer_element_normal.GetDirectArray().Add(normal_z_pos)
    layer_element_normal.GetDirectArray().Add(normal_z_pos)
    # Face 2
    layer_element_normal.GetDirectArray().Add(normal_x_pos)
    layer_element_normal.GetDirectArray().Add(normal_x_pos)
    layer_element_normal.GetDirectArray().Add(normal_x_pos)
    layer_element_normal.GetDirectArray().Add(normal_x_pos)
    # Face 3
    layer_element_normal.GetDirectArray().Add(normal_z_neg)
    layer_element_normal.GetDirectArray().Add(normal_z_neg)
    layer_element_normal.GetDirectArray().Add(normal_z_neg)
    layer_element_normal.GetDirectArray().Add(normal_z_neg)
    # Face 4
    layer_element_normal.GetDirectArray().Add(normal_x_neg)
    layer_element_normal.GetDirectArray().Add(normal_x_neg)
    layer_element_normal.GetDirectArray().Add(normal_x_neg)
    layer_element_normal.GetDirectArray().Add(normal_x_neg)
    # Face 5
    layer_element_normal.GetDirectArray().Add(normal_y_pos)
    layer_element_normal.GetDirectArray().Add(normal_y_pos)
    layer_element_normal.GetDirectArray().Add(normal_y_pos)
    layer_element_normal.GetDirectArray().Add(normal_y_pos)
    # Face 6
    layer_element_normal.GetDirectArray().Add(normal_y_neg)
    layer_element_normal.GetDirectArray().Add(normal_y_neg)
    layer_element_normal.GetDirectArray().Add(normal_y_neg)
    layer_element_normal.GetDirectArray().Add(normal_y_neg)

    # Finally, we set layer 0 of the mesh to the normal layer element.
    layer.SetNormals(layer_element_normal)


def get_ascii_format_id(manager):
    # Search file format ID of ASCII
    for formatId in range(manager.GetIOPluginRegistry().GetWriterFormatCount()):
        if manager.GetIOPluginRegistry().WriterIsFBX(formatId):
            if "ascii" in manager.GetIOPluginRegistry().GetWriterFormatDescription(formatId):
                return formatId

    # Default format is auto
    return -1


def main(fbx_path):
    # Create
    manager = FbxManager.Create()
    scene = FbxScene.Create(manager, "fbxScene")
    exporter = FbxExporter.Create(manager, "")

    # generate cube
    mesh = create_mesh(scene)
    define_control_points(scene, mesh)
    assign_normals(scene, mesh)

    # Export the scene to the file.
    exporter.Initialize(fbx_path, get_ascii_format_id(manager))
    exporter.Export(scene)

    # Destroy
    exporter.Destroy()
    scene.Destroy()
    manager.Destroy()


if __name__ == '__main__':
    # get argument
    args = sys.argv

    if len(args) < 1:
        print('Arguments are too short')
    else:
        main(args[1])
