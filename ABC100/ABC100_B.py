#n=int(input())
d,n=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

if n==100:
    print(101*(100**d))
else:
    print(n*(100**d))