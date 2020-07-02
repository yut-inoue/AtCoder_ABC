#n=int(input())
n,m,k=map(int,input().split())
al=list(map(int,input().split()))
bl=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

acum=[0]
bcum=[0]

for i in range(n):
    acum.append(acum[i]+al[i])

for i in range(m):
    bcum.append(bcum[i]+bl[i])
ans=0;j=m
for i in range(n+1):
    if acum[i]>k:
        break
    while acum[i]+bcum[j]>k:
        j-=1
    ans=max(ans,i+j)
print(ans)

