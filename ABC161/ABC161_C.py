#n=int(input())
n,k=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
if n>=k:
    ans=min(n%k,abs(k-n%k))
else:
    ans=min(k-n,n)
print(ans)

