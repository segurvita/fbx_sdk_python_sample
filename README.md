# fbx_sdk_python_sample
<div style="text-align:right">Language: <i>English</i> | <a href="README_JA.md">日本語</a></div>

This project is a sample program of FBX SDK Python.

# Build Setup

When using Docker, [lerignoux/python-fbx](https://hub.docker.com/r/lerignoux/python-fbx) is used, so no special installation is required.

If you do not use Docker, please install Python and FBX SDK Python 2019.x.
[FBX SDK Python Official Website](http://help.autodesk.com/view/FBX/2019/ENU/?guid=FBX_Developer_Help_scripting_with_python_fbx_installing_python_fbx_html)



# Usage

## Convert obj to FBX Binary format

You can convert `cube.obj` to `cube_binary.fbx` (FBX binary format) with the following command.

```bash
python convert_fbx/fbx_binary.py resources/cube.obj resources/cube_binary.fbx
```

If you have already installed Docker, the following command will work as well.

```bash
docker-compose run convert-fbx-binary
```



## Convert FBX Binary format to FBX ASCII format

You can convert `cube_binary.fbx` to `cube_ascii.fbx` (FBX ASCII format) with the following command.

```bash
python convert_fbx/fbx_ascii.py resources/cube_binary.fbx resources/cube_ascii.fbx
```

If you have already installed Docker, the following command will work as well.

```bash
docker-compose run convert-fbx-ascii
```



# License
The FBX SDK is under Autodesk License.
