#n=int(input())
a,b,c=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

if 4*a*b<(c-a-b)**2 and (c-a-b)>0:
    print("Yes")
else:
    print("No")
