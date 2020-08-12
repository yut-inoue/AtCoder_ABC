import copy
n = int(input())
l1d = [0]*(n+1)
M = [copy.deepcopy(l1d) for _ in range(n+1)]
for i in range(n):
    temp = list(map(int, input().split()))
    u = temp[0]
    k = temp[1]
    for j in range(k):
        M[u][temp[2+j]] = 1

d = [0 for _ in range(n+1)]
f = [0 for _ in range(n+1)]
color = [True for _ in range(n+1)]
t = 0


def dfs(u):
    global t
    global f, d, color
    t += 1
    d[u] = t
    color[u] = False
    for v in range(1, n+1):
        if M[u][v] and color[v]:
            dfs(v)
    t += 1
    f[u] = t
    return


for u in range(1, n+1):
    if color[u]:
        dfs(u)


for u in range(1, n+1):
    print("{0} {1} {2}".format(u, d[u], f[u]))
