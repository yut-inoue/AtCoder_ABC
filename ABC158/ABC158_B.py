#n=int(input())
n,a,b=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

v=n//(a+b)
ans=v*a
mod=n%(a+b)

temp=min(mod,a)
ans+=temp
print(ans)  