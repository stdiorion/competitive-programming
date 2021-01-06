import os
import subprocess

# 実行ファイルのディレクトリに移動
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# どこのコンテストか入力
print("Type the contest holder name: ", end="")
contest_holder: str = input()

# 空だったらAtCoderにする
if contest_holder == "":
    contest_holder = "atcoder"

# contests_xxディレクトリに移動 存在しなかったら終了
if os.path.isdir("contests_" + contest_holder):
    os.chdir("contests_" + contest_holder)
else:
    print(f"The directory contests_{contest_holder} does not found.")
    exit()

# コンテスト名を入力
print(f"[ {contest_holder} ]")
print("Type the contest name: ", end="")
contest_name: str = input()

# 問題番号はとりあえずA～F
problems = [chr(97 + i) for i in range(6)]

# abc999_x.py のようなフォーマットでファイル名をつける
files = [f"{contest_name}_{problem}.py" for problem in problems]

# template読み込み
with open("template.py", "r", encoding="UTF-8") as f:
    template = f.read()

# 確認
print(f"Sure? [ {contest_name} ] (y/n) ", end="")
if input() != "y":
    exit()

# コンテスト名のディレクトリ作成
if not os.path.isdir(contest_name):
    os.makedirs(contest_name)

os.chdir(contest_name)

# ファイルの生成
for file in files:
    try:
        with open(file, "x") as f:
            f.write(template)
    except FileExistsError:
        print(f"{file} already exists.")
        pass

# VSCodeでファイルを開く
for file in files:
    print(f"Opening {file}")
    subprocess.run(["code", file], shell=True)
