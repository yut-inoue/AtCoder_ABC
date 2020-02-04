n,k=map(int,input().split())
hl=list(map(int,input().split()))
ans=0
if n<=k:
    print(0)
else:
    hl.sort(reverse=True)
    temp=hl[(k+1)-1:n]
    for v in temp:
        ans+=v
    print(ans)
