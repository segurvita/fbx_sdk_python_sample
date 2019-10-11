# fbx_sdk_python_sample
<div style="text-align:right">Language: <a href="README.md">English</a> | <i>日本語</i></div>

FBX SDK Python Bindingsのサンプルプログラムです。

# 開発環境構築

Dockerを使う場合は、 [lerignoux/python-fbx](https://hub.docker.com/r/lerignoux/python-fbx) を使いますので、特に事前のインストールは必要ありません。

Dockerを使わない場合は、 Python と FBX SDK Python 2019.x のインストールをお願いします。
[FBX SDK Python Official Website](http://help.autodesk.com/view/FBX/2019/ENU/?guid=FBX_Developer_Help_scripting_with_python_fbx_installing_python_fbx_html)



# 使い方

## obj を FBX バイナリ形式 に変換する

以下のコマンドで、 `cube.obj` を `cube_binary.fbx` (FBX バイナリ形式) に変換できます。

```bash
python convert_fbx/fbx_binary.py resources/cube.obj resources/cube_binary.fbx
```

Dockerを導入していたら、以下のコマンドでもできます。

```bash
docker-compose run convert-fbx-binary
```



## FBX binary を FBX ASCII 形式に変換する

以下のコマンドで、 `cube_binary.fbx` を `cube_ascii.fbx` (FBX ASCII 形式) に変換できます。

```bash
python convert_fbx/fbx_ascii.py resources/cube_binary.fbx resources/cube_ascii.fbx
```

Dockerを導入していたら、以下のコマンドでもできます。

```bash
docker-compose run convert-fbx-ascii
```



# Licensing
FBX SDK は Autodesk License下にあります。
