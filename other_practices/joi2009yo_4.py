import sys
m = int(input())
n = int(input())
c = [list(map(int, input().split())) for i in range(n)]

sys.setrecursionlimit(10**7)


def movepos(tup):
    i, j = tup
    res = []
    for vertical in [-1, 0, 1]:
        newi = i+vertical
        if newi < 0 or newi > n-1:
            continue
        for side in [-1, 0, 1]:
            if abs(vertical) == 1 and abs(side) == 1:
                continue
            newj = j+side
            if newj < 0 or newj > m-1:
                continue
            newpos = (newi, newj)
            if newpos != tup:
                res.append(newpos)
    return res


adjl = [[] for _ in range(m*n+1)]
for i in range(n):
    for j in range(m):
        if c[i][j] != 1:
            continue
        move = movepos((i, j))
        u = i*m+(j+1)
        for tup in move:
            if c[tup[0]][tup[1]] == 1:
                v = tup[0]*m+tup[1]+1
                adjl[u].append(v)
                adjl[v].append(u)

# 隣接リストから重複を除く
for i, l1d in enumerate(adjl):
    adjl[i] = list(set(adjl[i]))


def dfs(u, cur_depth):
    global color
    global mxdepth
    cur_depth += 1
    mxdepth = max(mxdepth, cur_depth)
    color[u] = color_id
    for v in adjl[u]:
        if color[v] == NIL:  # 未到達なら再帰呼び出し
            color[v] = color_id
            dfs(v, cur_depth)
            color[v] = NIL


NIL = -1
color_id = 0
ans = 0

for i in range(n):
    for j in range(m):
        if c[i][j] == 1:
            color = [NIL for i in range(m*n+1)]
            mxdepth = 0
            u = i*m+j+1
            dfs(u, 0)
            ans = max(ans, mxdepth)
# print(adjl)
print(ans)
