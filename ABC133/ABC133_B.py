#n=int(input())
n,d=map(int,input().split())
#l=list(map(int,input().split()))
xl=[list(map(int,input().split())) for i in range(n)]

ans=0
import math
for i in range(n):
    for j in range(n):
        if i>=j:
	        continue
        total=0
        for k in range(d):
            total+=(xl[i][k]-xl[j][k])**2
        total=math.sqrt(total)
        if total==int(total):
            ans+=1
print(ans)

