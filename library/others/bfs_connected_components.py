# 幅優先探索で連結成分を求めるプログラム
from collections import deque
# n = int(input())# ノードの数
n, m = map(int, input().split())

# 隣接リストで格納する
adjl = [[] for _ in range(n+1)]
for i in range(m):  # 隣接関係を受け取る
    s, t = map(int, input().split())
    adjl[s].append(t)
    adjl[t].append(s)

NIL = -1  # 未発見を示す値
d = [-1 for i in range(n+1)]  # 頂点1からの距離を格納するリスト
color = [NIL for i in range(n+1)]  # 未到達かを示すリスト


def bfs(start_node, color_id):  # start_nodeは探索の開始点
    global color, d
    q = deque([start_node])
    d[start_node] = 0
    color[start_node] = color_id
    while len(q) != 0:
        u = q.popleft()
        for v in adjl[u]:
            if color[v] == NIL:
                d[v] = d[u]+1
                color[v] = color_id
                q.append(v)


color_id = 0
for u in range(n):  # node全てからスタートする
    if color[u] == NIL:
        color_id += 1
        bfs(u, color_id)

#print(color)
q=int(input())
for i in range(q):
    s, t = map(int, input().split())
    if color[s]==color[t]:
        print('yes')
    else:
        print('no')