n=int(input())
#a,b=map(int,input().split())
al=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

thre=10**18

if al.count(0)>=1:
    ans=0
else:
    ans=al[0]
    for i in range(1,n):
        ans=ans*al[i]
        if ans >thre:
            ans=-1
            break
print(ans)

