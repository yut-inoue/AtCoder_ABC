#n=int(input())
a,b=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
if (a*b)%2==0:
    print('Even')
else:
    print('Odd')