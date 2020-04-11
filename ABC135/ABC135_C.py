n=int(input())
#a,b=map(int,input().split())
al=list(map(int,input().split()))
bl=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
ans=0
for i in range(n):
    current=min(bl[i],al[i])
    bl[i]=bl[i]-current
    al[i]=al[i]-current
    ans+=current
    nex=min(al[i+1],bl[i])
    al[i+1]=al[i+1]-nex
    ans+=nex

print(ans)
