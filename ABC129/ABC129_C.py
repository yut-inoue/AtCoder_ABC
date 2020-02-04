
n,m=map(int,input().split())
broken=[False for i in range(n+1)]
const=1000000007
for i in range(m):
    a=int(input())
    broken[a]=True
n_way=[1,1]
if broken[1]:
    n_way=[1,0]
for i in range(2,n+1):
    if not broken[i] :
        n_way.append((n_way[i-1]+n_way[i-2])%const)
    else:
        n_way.append(0)
print(n_way[n])

