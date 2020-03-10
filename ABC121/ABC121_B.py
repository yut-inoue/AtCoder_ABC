#n=int(input())
n,m,c=map(int,input().split())
bl=list(map(int,input().split()))
al=[list(map(int,input().split())) for i in range(n)]

ans=0

for i in range(n):
    templ=al[i]
    total=c
    for j in range(m):
        total+=templ[j]*bl[j]
    if total>0:
        ans+=1

print(ans)
        

