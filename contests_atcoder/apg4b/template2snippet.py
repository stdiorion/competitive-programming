with open("contests_atcoder/apg4b/template.cpp", "r") as f:
    template = f.readlines()

res = ""

for line in template:
    line = line.replace("\"", "\\\"").replace("\\n", "\\\\n")
    res += "\"" + line.rstrip() + "\",\n"

res = res[:-2]

with open("contests_atcoder/apg4b/snippet.txt", "w") as f:
    f.write(res)