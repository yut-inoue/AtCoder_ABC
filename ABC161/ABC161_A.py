#n=int(input())
x,y,z=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

x,y=y,x
x,z=z,x

print("{0} {1} {2}".format(x,y,z))

