#n=int(input())
n,k=map(int,input().split())
#hl=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
hl=[int(input()) for i in range(n)]

hl.sort()
ans=hl[k-1]-hl[0]
for i in range(n-k+1):
    ans=min(ans,hl[i+k-1]-hl[i])
print(ans)

