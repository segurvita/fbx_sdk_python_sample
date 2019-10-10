# fbx_sdk_python_sample
<div style="text-align:right">Language: <i>English</i> | <a href="README_JA.md">日本語</a></div>

This project is a sample program of FBX SDK Python Bindings.



## Convert obj to FBX binary

You can convert `cube.obj` to `cube_binary.fbx` (FBX binary format) with the following command.

```bash
python convert_fbx/fbx_binary.py resources/cube.obj resources/cube_binary.fbx
```

If you have already installed Docker, the following command will work as well.

```bash
docker-compose run convert-fbx-binary
```



## Convert FBX binary to FBX ASCII

You can convert `cube_binary.fbx` to `cube_ascii.fbx` (FBX ASCII format) with the following command.

```bash
python convert_fbx/fbx_ascii.py resources/cube_binary.fbx resources/cube_ascii.fbx
```

If you have already installed Docker, the following command will work as well.

```bash
docker-compose run convert-fbx-ascii
```



# Licensing
The FBX SDK is under Autodesk License.
