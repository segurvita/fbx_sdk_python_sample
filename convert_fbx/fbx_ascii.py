import sys
from fbx import *


def main(obj_path, fbx_path):
    # Create
    manager = FbxManager.Create()
    scene = FbxScene.Create(manager, "fbxscene")
    importer = FbxImporter.Create(manager, "")
    exporter = FbxExporter.Create(manager, "")

    # Import the file to the scene
    importer.Initialize(obj_path, -1)
    importer.Import(scene)

    # Default format is auto
    fileFormat = -1

    # Search file format ID of ASCII
    for formatId in range(manager.GetIOPluginRegistry().GetWriterFormatCount()):
        if manager.GetIOPluginRegistry().WriterIsFBX(formatId):
            if "ascii" in manager.GetIOPluginRegistry().GetWriterFormatDescription(formatId):
                fileFormat = formatId
                break

    # Export the scene to the file.
    exporter.Initialize(fbx_path, fileFormat)
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
        print('Atguments are too short')
    else:
        main(args[1], args[2])
