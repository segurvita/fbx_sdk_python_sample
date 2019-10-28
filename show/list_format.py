from fbx import *


def list_writer_format(manager):
    print('# Writer Format List')
    for formatIndex in range(manager.GetIOPluginRegistry().GetWriterFormatCount()):
        description = manager.GetIOPluginRegistry().GetWriterFormatDescription(formatIndex)
        print(formatIndex, description)


def list_reader_format(manager):
    print('# Reader Format List')
    for formatIndex in range(manager.GetIOPluginRegistry().GetReaderFormatCount()):
        description = manager.GetIOPluginRegistry().GetReaderFormatDescription(formatIndex)
        print(formatIndex, description)


def main():
    # Create
    manager = FbxManager.Create()
    scene = FbxScene.Create(manager, "fbxScene")

    # List
    list_writer_format(manager)
    list_reader_format(manager)

    # Destroy
    scene.Destroy()
    manager.Destroy()


if __name__ == '__main__':
    main()
