#n = int(input())
#a, b = map(int,input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
s = list(input())
t = list(input())


def sameNum(s, t):
    res = 0
    for i in range(len(s)):
        if s[i] == t[i]:
            res += 1
    return res


ns = len(s)
nt = len(t)
mn = nt
for i in range(ns-nt+1):
    samenum = sameNum(s[i:i+nt], t)
    mn = min(mn, nt-samenum)
print(mn)
