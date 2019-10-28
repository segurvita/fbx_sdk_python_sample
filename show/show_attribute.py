"""
This code was based on the following website.
https://help.autodesk.com/view/FBX/2019/ENU/?guid=FBX_Developer_Help_getting_started_your_first_fbx_sdk_program_html
"""

import sys
from fbx import *


num_tabs = 0


def print_tabs():
    """
    Print the required number of tabs.
    """

    global num_tabs

    for i in range(num_tabs):
        sys.stdout.write("  ")


def get_attribute_type_name(type):
    """
    Return a string-based representation based on the attribute type.
    """

    if type == FbxNodeAttribute.eUnknown:
        return "unidentified"
    elif type == FbxNodeAttribute.eNull:
        return "null"
    elif type == FbxNodeAttribute.eMarker:
        return "marker"
    elif type == FbxNodeAttribute.eSkeleton:
        return "skeleton"
    elif type == FbxNodeAttribute.eMesh:
        return "mesh"
    elif type == FbxNodeAttribute.eNurbs:
        return "nurbs"
    elif type == FbxNodeAttribute.ePatch:
        return "patch"
    elif type == FbxNodeAttribute.eCamera:
        return "camera"
    elif type == FbxNodeAttribute.eCameraStereo:
        return "stereo"
    elif type == FbxNodeAttribute.eCameraSwitcher:
        return "camera switcher"
    elif type == FbxNodeAttribute.eLight:
        return "light"
    elif type == FbxNodeAttribute.eOpticalReference:
        return "optical reference"
    elif type == FbxNodeAttribute.eOpticalMarker:
        return "marker"
    elif type == FbxNodeAttribute.eNurbsCurve:
        return "nurbs curve"
    elif type == FbxNodeAttribute.eTrimNurbsSurface:
        return "trim nurbs surface"
    elif type == FbxNodeAttribute.eBoundary:
        return "boundary"
    elif type == FbxNodeAttribute.eNurbsSurface:
        return "nurbs surface"
    elif type == FbxNodeAttribute.eShape:
        return "shape"
    elif type == FbxNodeAttribute.eLODGroup:
        return "lodgroup"
    elif type == FbxNodeAttribute.eSubDiv:
        return "subdiv"
    else:
        return "unknown"


def print_attribute(attribute):
    """
    Print an attribute.
    """

    if not attribute:
        return

    typeName = get_attribute_type_name(attribute.GetAttributeType())
    attrName = attribute.GetName()
    print_tabs()

    sys.stdout.write(
        "<attribute type='" + typeName +
        "' name='" + attrName + "'/>\n"
    )


def PrintNode(node):
    """
    Print a node, its attributes, and all its children recursively.
    """

    global num_tabs

    print_tabs()
    nodeName = node.GetName()
    translation = node.LclTranslation.Get()
    rotation = node.LclRotation.Get()
    scaling = node.LclScaling.Get()

    # Print the contents of the node.
    sys.stdout.write(
        "<node name='" + nodeName + "' "
        + "translation='("
        + str(translation[0]) + ", "
        + str(translation[1]) + ", "
        + str(translation[2]) + ")' "
        + "rotation='("
        + str(rotation[0]) + ", "
        + str(rotation[1]) + ", "
        + str(rotation[2]) + ")' "
        + "scaling='("
        + str(scaling[0]) + ", "
        + str(scaling[1]) + ", "
        + str(scaling[2]) + ")'>\n"
    )

    num_tabs += 1

    # Print the node's attributes.
    for i in range(node.GetNodeAttributeCount()):
        print_attribute(node.GetNodeAttributeByIndex(i))

    # Recursively Print the children.
    for j in range(node.GetChildCount()):
        PrintNode(node.GetChild(j))

    num_tabs -= 1
    print_tabs()
    sys.stdout.write("</node>\n")


def main(file_name):
    """
    Main function - loads the fbx file,
    and prints its contents in an xml format to stdout.
    """

    # Create
    manager = FbxManager.Create()
    scene = FbxScene.Create(manager, "fbxscene")
    importer = FbxImporter.Create(manager, "")

    # Use the first argument as the filename for the importer.
    if not importer.Initialize(file_name, -1, manager.GetIOSettings()):
        sys.stdout.write("Call to FbxImporter.Initialize() failed.\n")
        sys.stdout.write(
            "Error returned: "
            + importer.GetStatus().GetErrorString() + "\n"
        )
        exit(-1)

    # Import the contents of the file into the scene.
    importer.Import(scene)

    # The file is imported so get rid of the importer.
    importer.Destroy()

    # Print the nodes of the scene and their attributes recursively.
    # Note that we are not printing the root node because it should
    # not contain any attributes.
    root_node = scene.GetRootNode()
    if(root_node):
        for i in range(root_node.GetChildCount()):
            PrintNode(root_node.GetChild(i))

    # Destroy the SDK manager and all the other objects it was handling.
    manager.Destroy()
    return 0


if __name__ == '__main__':
    # get argument
    args = sys.argv

    if len(args) < 2:
        sys.stdout.write('Atguments are too short\n')
    else:
        main(args[1])
