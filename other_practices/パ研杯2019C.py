N,M=map(int,input().split())
#hl=list(map(int,input().split()))
A=[list(map(int,input().split())) for i in range(N)]
mx=0
for t1 in range(M-1):
    for t2 in range(t1+1,M):
        temp=0
        for i in range(N):
            temp+=max(A[i][t1],A[i][t2])
        mx=max(mx,temp)
print(mx)
