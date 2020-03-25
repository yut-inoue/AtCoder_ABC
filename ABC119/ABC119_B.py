n=int(input())
#a,b=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
ans=0
for i in range(n):
    x,u=map(str,input().split())
    x=float(x)
    if u=="BTC":
        x=380000.0*x
    ans+=x
print('{:.7f}'.format(ans))
