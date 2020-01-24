n=int(input())
al=list(map(int,input().split()))

import fractions
ans=0
left=[0]
for i in range(1,n):
    ans=fractions.gcd(ans,al[i-1])
    left.append(ans)
#print(left)
right=[0 for i in range(n+1)]
for i in range(1,n+1):
    right[n-i]=fractions.gcd(right[n-i+1],al[n-i])
#print(right)

ans=0

for i in range(n):
    ans=max(ans,(fractions.gcd(left[i],right[i+1])))
print(ans)

