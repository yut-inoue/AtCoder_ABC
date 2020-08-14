# 隣接リストを使った深さ優先探索
# グラフの連結成分を求める
import sys
sys.setrecursionlimit(10 ** 7)
n, m = map(int, input().split())
adjl = [[] for _ in range(n+1)]
NIL = -1
for i in range(m):
    s, t = map(int, input().split())
    adjl[s].append(t)
    adjl[t].append(s)

color = [NIL for i in range(n+1)]
color_id = 0


def dfs(u, color_id):
    global color
    color[u] = color_id
    for v in adjl[u]:
        if color[v] == NIL:  # 未到達なら再起呼び出し
            color[v] = color_id
            dfs(v, color_id)


for u in range(n):
    if color[u] == NIL:
        color_id += 1
        dfs(u, color_id)

q = int(input())

for i in range(q):
    s, t = map(int, input().split())
    if m == 0:
        print('no')
    else:
        if color[s] == color[t]:
            print('yes')
        else:
            print('no')
