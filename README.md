# competitive-programming
競技プログラミングで提出したコード・自分用ツール等のまとめ

以下自分用

## filegen.pyの使い方

あらかじめコンテストサイトごとにcontests_atcoderのようなディレクトリを作っておく。

filegen.pyを実行すると、

```
Type the contest holder name:
```

と言われるのでコンテストサイトの名前を入力する（空にするとatcoderが入る）。

```
Type the contest name:
```

と言われるのでコンテスト名（ex. abc999）を入力する。

```
Sure? [ abc999 ] (y/n)
```

確認されるのでyを入力して`Enter`。

`contests_xx\abc999\`フォルダがなければ作成され、その中に`abc999_a.py`～`abc999_f.py`が作成される。ファイルの中身は`contest_xx\template.py`があらかじめ入れられる。おまけにVSCodeで開いてくれる。