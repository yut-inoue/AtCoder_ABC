#n=int(input())
#a,b=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
x=int(input())

ans=(x//500)*1000
md=x%500
ans+=(md//5)*5

print(ans)
