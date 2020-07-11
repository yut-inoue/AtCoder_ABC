#n=int(input())
n,Y=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
x,y,z=-1,-1,-1
for i in range(n+1):
    for j in range(n+1):
        k=max(0,n-(i+j))
        if i+j+k==n:
            if i*1000+j*5000+k*10000 == Y:
                x,y,z=k,j,i
                #break
print("{0} {1} {2}".format(x,y,z))
