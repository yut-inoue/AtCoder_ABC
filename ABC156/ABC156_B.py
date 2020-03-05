#n=int(input())
n,k=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

ans=0
while True:
    ans+=1
    shou=n//k
    amari=n%k
    if shou==0:
        break
    n=shou
print(ans)