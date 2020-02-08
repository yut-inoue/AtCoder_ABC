n=int(input())
dl=list(map(int,input().split()))

ans=0

for i in range(n):
    for j in range(n):
        if j <i:
            ans+=dl[i]*dl[j]
print(ans)
