# n=int(input())
import sys
sys.setrecursionlimit(10**7)
n, q = map(int, input().split())
# vl=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
adjl = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    adjl[a].append(b)
    adjl[b].append(a)
c = [0 for _ in range(n+1)]
point = [0 for _ in range(n+1)]


def dfs(p, u, add):
    global point
    point[u] = c[u]+add
    for v in adjl[u]:
        if v == p:
            continue
        dfs(u, v, point[u])


for i in range(q):
    p, x = map(int, input().split())
    c[p] = c[p]+x


dfs(0, 1, 0)
point.remove(0)
print(*point, sep=" ")
