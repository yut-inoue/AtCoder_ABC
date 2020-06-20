#n=int(input())
a,b,x=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

if x-a<=b and x>=a:
    print("YES")
else:
    print("NO")

