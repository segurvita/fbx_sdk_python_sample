import sys
from fbx import *


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
