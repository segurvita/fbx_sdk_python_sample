# fbx_sdk_python_sample
<div style="text-align:right">Language: <a href="README.md">English</a> | <i>日本語</i></div>

FBX SDK Python Bindingsのサンプルプログラムです。



## obj を FBX バイナリ形式 に変換する

以下のコードで、 `cube.obj` を `cube_binary.fbx` (FBX バイナリ形式) に変換できます。

```bash
python convert_fbx/fbx_binary.py resources/cube.obj resources/cube_binary.fbx
```

Dockerを導入していたら、以下のコマンドでもできます。

```bash
docker-compose run convert-fbx-binary
```



## FBX binary を FBX ASCII 形式に変換する

以下のコードで、 `cube_binary.fbx` を `cube_ascii.fbx` (FBX ASCII 形式) に変換できます。

```bash
python convert_fbx/fbx_ascii.py resources/cube_binary.fbx resources/cube_ascii.fbx
```

Dockerを導入していたら、以下のコマンドでもできます。

```bash
docker-compose run convert-fbx-ascii
```



# Licensing
FBX SDK は Autodesk License下にあります。
