n=int(input())
def m(s):len(s)<n and[m(s+chr(x))for x in range(97,ord(max(s))+2)]or print(s)
m("a")