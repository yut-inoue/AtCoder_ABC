n=int(input())
#a,b=map(int,input().split())
al=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

ans=0

for i in range(n):
    ans+=1.0/al[i]

ans=1.0/ans

print('{:.9f}'.format(ans))