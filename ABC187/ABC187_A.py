#n = int(input())
a, b = map(int,input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

def s(v):
    res=0
    v=str(v)
    for vi in v:
        res+=int(vi)
    return res

print(max(s(a), s(b)))
