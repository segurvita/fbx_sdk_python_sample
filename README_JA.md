# fbx_sdk_python_sample
<div style="text-align:right">Language: <a href="README.md">English</a> | <i>日本語</i></div>

FBX SDK Python のサンプルプログラムです。



# 開発環境構築

Dockerを使う場合は、 [lerignoux/python-fbx](https://hub.docker.com/r/lerignoux/python-fbx) を使いますので、特に事前のインストールは必要ありません。

Dockerを使わない場合は、 Python と FBX SDK Python 2019.x のインストールをお願いします。

- [FBX SDK Python 公式サイト](http://help.autodesk.com/view/FBX/2019/ENU/?guid=FBX_Developer_Help_scripting_with_python_fbx_installing_python_fbx_html)
- [Python版FBX SDKをWindowsにインストールする](https://qiita.com/segur/items/5d0dff790e784760a547)
- [Python版FBX SDKをMacにインストールする](https://qiita.com/segur/items/e09d464b5e2ff0c8725e)



# 使い方

## obj を FBX バイナリ形式に変換する

以下のコマンドで、 `cube.obj` を `cube_binary.fbx` (FBX バイナリ形式) に変換できます。

```bash
python convert_fbx/fbx_binary.py resources/cube.obj resources/cube_binary.fbx
```

Dockerを導入していたら、以下のコマンドでもできます。

```bash
docker-compose run convert-fbx-binary
```



## FBX バイナリ形式を FBX ASCII 形式に変換する

以下のコマンドで、 `cube_binary.fbx` を `cube_ascii.fbx` (FBX ASCII 形式) に変換できます。

```bash
python convert_fbx/fbx_ascii.py resources/cube_binary.fbx resources/cube_ascii.fbx
```

Dockerを導入していたら、以下のコマンドでもできます。

```bash
docker-compose run convert-fbx-ascii
```



# ラインセンス
FBX SDK は Autodesk License下にあります。
