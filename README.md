# competitive-programming
競技プログラミングで提出したコード・自分用ツール等のまとめ

以下自分用

## filegen.pyの使い方

あらかじめコンテストサイトごとにcontests_atcoderのようなディレクトリを作っておく

filegen.pyを実行すると、

```
Type the contest holder name:
```

と言われるのでコンテストサイトの名前を入力（空白だとatcoderが勝手に入る）そしたら

```
Type the contest name:
```

と言われるのでコンテスト名（abc999とか）を入力

```
Sure? [ abc999 ] (y/n)
```

確認されるのでyを入力してエンターする。するとcontests_xx下にabc999フォルダが作成され、その中にabc999_a.pyからabc999_f.pyまで作成される。ファイルの中身はcontest_xxフォルダ直下のtemplate.pyがそのまま入る。あと勝手にVSCodeで開いてくれる。