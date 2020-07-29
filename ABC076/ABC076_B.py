n = int(input())
k = int(input())
#a,b=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
v=1
for i in range(n):
    v = min(v+k, 2*v)
print(v)
