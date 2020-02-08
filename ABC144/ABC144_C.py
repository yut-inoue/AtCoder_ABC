n=int(input())
import math
ans=n+1-2
for i in range(1,int(math.sqrt(n))+1):
    if n%i==0:
        ans=min(ans,i+n//i-2)
print(ans)


