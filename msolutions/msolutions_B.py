#n=int(input())
a,b,c=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
k=int(input())
ans='No'
for i in range(0,k+1):
    cnew = c*(2**(i))
    bnew = b*(2**(k-i))
    if a < bnew and bnew < cnew:
        ans='Yes'
print(ans)
