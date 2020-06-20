#n=int(input())
n,m,x=map(int,input().split())
al=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

right=len([a for a in al if a <=x])
left=len([a for a in al if a>=x])

print(min(right,left))

