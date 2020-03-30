#n=int(input())
n,x=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
ml=[int(input()) for i in range(n)]
dif=x-sum(ml)
if dif==0:
    ans=n
else:
    ans=n+dif//min(ml)

print(ans)