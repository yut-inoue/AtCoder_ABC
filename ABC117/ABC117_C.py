#n=int(input())
n,m=map(int,input().split())
xl=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
cuml=[]
if n>=m:
    print(0)
else:
    xl.sort()
    rng=xl[m-1]-xl[0]
    ans=rng
    for i in range(1,m):
        cuml.append(xl[i]-xl[i-1])
    cuml.sort()
    for i in range(n-1):
        ans-=cuml[m-2-i]
    print(ans)

        
        


