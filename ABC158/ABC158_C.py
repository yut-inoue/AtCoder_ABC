#n=int(input())
a,b=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

import math
flag=False
ans=-1
for i in range(1,10001):
    a2=i*0.08
    a1=int(i*0.08)
    b1=int(i*0.1)

    if a1==a and b1==b:
        ans=i
        break
print(ans)



