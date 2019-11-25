from fbx import FbxManager, FbxScene, FbxAnimStack


def extract_anim(scene):
    print ('# Extract animation data')
    num = scene.GetSrcObjectCount()
    print("num", num)
    for index in range(num):
        obj = scene.GetSrcObject(index)

        print (index, obj.GetName())


def main():
    # Create
    manager = FbxManager.Create()
    scene = FbxScene.Create(manager, "fbxScene")

    # List
    extract_anim(scene)

    # Destroy
    scene.Destroy()
    manager.Destroy()


if __name__ == '__main__':
    main()
