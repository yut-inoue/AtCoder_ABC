#n=int(input())
a,b,n=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

x=min(b-1,n)
ans=(a*x)//b - a*(x//b)

print(ans)
