#n=int(input())
k,n=map(int,input().split())
al=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

mn=min(al)
mx=max(al)
dis=[]
for i in range(n-1):
    dis.append(al[i+1]-al[i])
dis.append(mn+(k-mx))

dis.sort(reverse=False)
ans=0
for i in range(n-1):
    ans+=dis[i]
print(ans)
