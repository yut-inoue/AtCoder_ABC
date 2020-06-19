n=int(input())
#a,b=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
nst=list(str(n))
total=0
for ni in nst:
    total+=int(ni)
if n%total ==0:
    print("Yes")
else:
    print("No")