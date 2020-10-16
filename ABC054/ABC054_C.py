# n=int(input())
import itertools
import copy
n, m = map(int, input().split())
# l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
temp = [0 for _ in range(n+1)]
adjl = [copy.deepcopy(temp) for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    adjl[a][b] = 1
    adjl[b][a] = 1

node = [i for i in range(2, n+1)]
ans = 0
for v in itertools.permutations(node):
    # print(v)
    flag = True
    cur = 1
    for j in range(n-1):
        nex = v[j]
        if adjl[cur][nex] != 1:
            flag = False
            break
        cur = v[j]
    if flag:
        ans += 1
print(ans)
