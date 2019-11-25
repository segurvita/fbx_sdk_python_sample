import sys
from fbx import *


def generate_camera_anim(scene):
    # Create Camera
    camera_node = FbxNode.Create(scene, "cameraNode")
    camera = FbxCamera.Create(scene, "camera")
    camera_node.SetNodeAttribute(camera)
    root_node = scene.GetRootNode()
    root_node.AddChild(camera_node)
    scene.GetGlobalSettings().SetDefaultCamera(camera.GetName())

    # Set the default local translation values (X, Y, Z) for the camera
    camera_node.LclTranslation.Set(FbxDouble3(0.0, 0.0, -5.0))

    # create an animation stack
    anim_stack = FbxAnimStack.Create(scene, "stack")

    # Create the base layer
    anim_base_layer = FbxAnimLayer.Create(scene, "layer0")
    anim_stack.AddMember(anim_base_layer)

    # Get the camera's curve node for local translation.
    anim_curve_node = camera_node.LclTranslation.GetCurveNode(
        anim_base_layer, True)

    # Index for the keys that define the curve
    key_index = 0

    # Curve for local translation on X-axis
    tran_x_curve = camera_node.LclTranslation.GetCurve(
        anim_base_layer, "KFCURVENODE_T_X", True)

    anim_curve = FbxAnimCurve.Create(scene, "curve0")
    time = FbxTime()

    # First the start keyframe
    anim_curve.KeyModifyBegin()

    # Starting time
    time.SetSecondDouble(0.0)

    # Add the start key
    key_index, key_last = anim_curve.KeyAdd(time)

    # Set the zeroth key, starting time, starting X value
    # Straight line between 2 points,
    anim_curve.KeySet(key_index, time, 0.0,
                      FbxAnimCurveDef.eInterpolationLinear)

    # Then the stop keyframe
    time.SetSecondDouble(20.0)
    key_index, key_last = anim_curve.KeyAdd(time)
    anim_curve.KeySet(key_index, time, 500.0,
                      FbxAnimCurveDef.eInterpolationLinear)

    anim_curve.KeyModifyEnd()


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

    # generate animation
    generate_camera_anim(scene)

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
