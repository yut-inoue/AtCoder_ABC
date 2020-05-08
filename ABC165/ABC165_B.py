x=int(input())
#a,b=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
dep=100
import math
ans=0
while True:
    ans+=1
    dep=math.floor(dep*1.01)
    if dep>=x:
        break
print(ans)




