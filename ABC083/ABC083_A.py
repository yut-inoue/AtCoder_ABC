#n=int(input())
a,b,c,d=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

l=a+b;r=c+d
if l<r:
    print('Right')
elif l==r:
    print('Balanced')
else:
    print('Left')


