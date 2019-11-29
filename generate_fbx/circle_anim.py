import sys
import math
from fbx import *

# frame per seconde
fps = 30.0

# rotation per second
rps = 0.5


def generate_anim_stack(scene):
    '''
    # Reference
    - http://help.autodesk.com/view/FBX/2019/ENU/?guid=FBX_Developer_Help_animation_example_animating_a_node_html
    '''

    # create an animation stack
    anim_stack = FbxAnimStack.Create(scene, "stack")

    return anim_stack


def generate_anim_layer(scene, anim_stack, node):
    # Get name of the node.
    node_name = node.GetName()

    # Set the default local translation values (X, Y, Z) for the camera
    node.LclTranslation.Set(FbxDouble3(0.0, 0.0, 0.0))
    node.LclRotation.Set(FbxDouble3(0.0, 0.0, 0.0))

    # Create the base layer
    anim_base_layer = FbxAnimLayer.Create(scene, "layer_" + node_name)
    anim_stack.AddMember(anim_base_layer)

    # Get the curve node for local translation.
    # The second parameter to GetCurveNode() is "true" to ensure
    # that the curve node is automatically created, if it does not exist.
    anim_curve_node = node.LclTranslation.GetCurveNode(
        anim_base_layer, True
    )

    return anim_base_layer


def prot_circle(degree, time, curve_t_x, curve_t_y, curve_r_z):
    # Convert degree to radian
    radian = math.radians(degree)

    # Translation X : cos(radian)
    key_index, key_last = curve_t_x.KeyAdd(time)
    curve_t_x.KeySet(
        key_index, time, math.cos(radian), FbxAnimCurveDef.eInterpolationLinear
    )

    # Translation Y : sin(radian)
    key_index, key_last = curve_t_y.KeyAdd(time)
    curve_t_y.KeySet(
        key_index, time, math.sin(radian), FbxAnimCurveDef.eInterpolationLinear
    )

    # Rotation Z : degree
    key_index, key_last = curve_r_z.KeyAdd(time)
    curve_r_z.KeySet(
        key_index, time, degree, FbxAnimCurveDef.eInterpolationLinear
    )


def move_circle(node, anim_base_layer):

    # Get the animation curve for local translation of the node.
    # true: If the curve does not exist yet, create it.
    curve_t_x = node.LclTranslation.GetCurve(
        anim_base_layer, "X", True
    )
    curve_t_y = node.LclTranslation.GetCurve(
        anim_base_layer, "Y", True
    )
    curve_r_z = node.LclRotation.GetCurve(
        anim_base_layer, "Z", True
    )

    # anim_curve = FbxAnimCurve.Create(scene, "curve_" + node_name)
    time = FbxTime()

    # First the start keyframe
    curve_t_x.KeyModifyBegin()
    curve_t_y.KeyModifyBegin()
    curve_r_z.KeyModifyBegin()

    # Protting circle
    for frame in range(int(fps / rps)):
        sec = float(frame) / fps
        time.SetSecondDouble(sec)
        degree = rps * sec * 360.0
        prot_circle(degree, time, curve_t_x, curve_t_y, curve_r_z)

    # End
    curve_t_x.KeyModifyEnd()
    curve_t_y.KeyModifyEnd()
    curve_r_z.KeyModifyEnd()


def get_ascii_format_id(manager):
    # Search file format ID of ASCII
    for formatId in range(manager.GetIOPluginRegistry().GetWriterFormatCount()):
        if manager.GetIOPluginRegistry().WriterIsFBX(formatId):
            if "ascii" in manager.GetIOPluginRegistry().GetWriterFormatDescription(formatId):
                return formatId

    # Default format is auto
    return -1


def main(obj_path, fbx_path):
    # Create
    manager = FbxManager.Create()
    scene = FbxScene.Create(manager, "fbxScene")
    importer = FbxImporter.Create(manager, "")
    exporter = FbxExporter.Create(manager, "")

    # Import the file to the scene
    importer.Initialize(obj_path, -1)
    importer.Import(scene)

    # Generate animation stack
    anim_stack = generate_anim_stack(scene)

    # Get cube node
    root_node = scene.GetRootNode()
    if (root_node):
        for i in range(root_node.GetChildCount()):
            node = root_node.GetChild(i)

            # generate animation layer
            anim_base_layer = generate_anim_layer(scene, anim_stack, node)

            # generate node animation
            move_circle(node, anim_base_layer)

    # Export the scene to the file.
    exporter.Initialize(fbx_path, get_ascii_format_id(manager))
    exporter.Export(scene)

    # Destroy
    exporter.Destroy()
    importer.Destroy()
    scene.Destroy()
    manager.Destroy()


if __name__ == '__main__':
    # get argument
    args = sys.argv

    if len(args) < 2:
        print('Arguments are too short')
    else:
        main(args[1], args[2])
