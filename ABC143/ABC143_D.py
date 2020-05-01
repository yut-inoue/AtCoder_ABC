n=int(input())
#a,b=map(int,input().split())
l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

import bisect

l.sort()
ans=0
for i in range(n):
    for j in range(i+1,n):
        a=l[i]
        b=l[j]
        index=bisect.bisect_left(l,a+b)
        ans+=max(index-(j+1),0)
print(ans)