n = int(input())
#a, b = map(int,input().split())
al = list(map(int,input().split()))
bl = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
def prod(a, b):
    res=0
    for i in range(n):
        res+=a[i]*b[i]
    return res

if prod(al, bl)==0:
    print('Yes')        
else:
    print('No')