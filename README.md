# minenohara-dic

VueとEelで作った、デスクトップ辞書アプリ

# 配布パッケージ

TBD

## 作り方

(env-38) $ python -m eel gui.py front --onefile --noconsole --hidden-import pkg_resources.py2_warn -n minanohara-dic --add-data db/ejdict.sqlite3:db --version-file version.txt 


```
usage: __main__.py [-h] [-v] [-D] [-F] [--specpath DIR] [-n NAME]
                   [--add-data <SRC;DEST or SRC:DEST>]
                   [--add-binary <SRC;DEST or SRC:DEST>] [-p DIR]
                   [--hidden-import MODULENAME]
                   [--additional-hooks-dir HOOKSPATH]
                   [--runtime-hook RUNTIME_HOOKS] [--exclude-module EXCLUDES]
                   [--key KEY] [-d {all,imports,bootloader,noarchive}] [-s]
                   [--noupx] [--upx-exclude FILE] [-c] [-w]
                   [-i <FILE.ico or FILE.exe,ID or FILE.icns>]
                   [--version-file FILE] [-m <FILE or XML>] [-r RESOURCE]
                   [--uac-admin] [--uac-uiaccess] [--win-private-assemblies]
                   [--win-no-prefer-redirects]
                   [--osx-bundle-identifier BUNDLE_IDENTIFIER]
                   [--runtime-tmpdir PATH] [--bootloader-ignore-signals]
                   [--distpath DIR] [--workpath WORKPATH] [-y]
                   [--upx-dir UPX_DIR] [-a] [--clean] [--log-level LEVEL]
                   scriptname [scriptname ...]
```


# 利用技術とパッケージ

- 辞書: パブリックドメインの英和辞書データ (ejdict-hand) : https://kujirahand.com/web-tools/EJDictFreeDL.php
- JSフレームワーク Vue : https://jp.vuejs.org/index.html / Vuex : https://vuex.vuejs.org/
- マテリアルデザインフレームワーク : vuetify : https://vuetifyjs.com/ja/
- Pythonデスクトップアプリ構築 Eel : https://pypi.org/project/Eel/

# 機能

- 英和辞書
- スペルミスを編集距離(2)までの候補を10個表示する
- 簡易意味表示
- クリックによる詳細意味表示

# 開発用Install

```
 $ cd front
 $ npm run serve
 $ npm run build
 $ cd ..
```

```
$ python3 -m venv env
$ . env/bin/activate
(env) $ pip install -r requirements.txt
```

```
(env) $ python gui.py
```

# 将来

- 日英にも対応させたい

# 謝辞

- Vue及びVuexについては、 @hirokiky さんにたくさんの指導を受けました。
- Eelについては、 @ftnext さんのEuroPython 2020のトークで存在をしりました。
- 編集距離(Levenshtein distance) については、 2012年に、 @rokujyouhitoma さんからアイデアをいただき、実装面では @hiratara から指導を受けました。