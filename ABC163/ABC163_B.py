#n=int(input())
n,m=map(int,input().split())
al=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

total=sum(al)
if total>n:
    ans=-1
else:
    ans=n-total
print(ans)


