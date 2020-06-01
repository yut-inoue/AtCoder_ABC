#n=int(input())
a,b=map(str,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

a=int(a)
b=int(b[0]+b[2]+b[3])

ans=(a*b)//100

print(ans)
