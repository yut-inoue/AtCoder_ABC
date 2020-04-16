k=int(input())
#a,b=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

import math 

def gcds(l):
    res=0
    for val in l:
        res=math.gcd(res,val)
    return res
ans=0
for i in range(1,k+1):
    for j in range(1,k+1):
        for m in range(1,k+1):
            ans+=gcds([i,j,m])
print(ans)
