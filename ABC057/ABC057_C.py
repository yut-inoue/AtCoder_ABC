n=int(input())
#a,b=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

import math
ans=len(str(n))
for i in range(1,int(math.sqrt(n))+1):
    if n%i==0:
        ans=max(len(str(i)),len(str(n//i)))

print(ans)


