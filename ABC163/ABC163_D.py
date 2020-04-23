#n=int(input())
n,k=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

mod=10**9+7
ans=0
for kval in range(k,n+2):
    mx=kval*(2*n-kval+1)//2
    mn=kval*(kval-1)//2
    add=mx-mn+1
    ans=(ans+add) % mod

print(ans)

