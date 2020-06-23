#n=int(input())
n,k=map(int,input().split())
pl=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

pl.sort()
print(sum(pl[:k]))

