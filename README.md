# 環境立ち上げ手順
遊ぶための環境をDockerで立ち上げる。

```
cd python-vec-sample
bin/run-playground.sh
```

*実行権限がない場合はbinのshellファイルに権限を付加してください。*

```
chmod -R 755 bin
```

# 遊び終わったら

立ち上げた環境を消す。

```
bin/close-playground.sh
```

# ライブラリ管理
requirements.txtでライブラリのバージョン管理をしている。
そのため、pipでのライブラリの追加・削除時にはそちらも以下のように更新すること。

ライブラリをインストール

```
pip install [ライブラリ名]
pip freeze > requirements.txt 
```

ライブラリをアンインストール

```
pip uninstall [ライブラリ名]
pip freeze > requirements.txt 
```
