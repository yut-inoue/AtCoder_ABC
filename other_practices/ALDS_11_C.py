from collections import deque
n = int(input())# ノードの数

# 隣接リストで格納する
adjl = [[] for _ in range(n+1)]
for i in range(n):
    temp = list(map(int, input().split()))
    u, k = temp[0], temp[1]
    adjl[i+1] = temp[2:]

d = [-1 for i in range(n+1)]# 頂点1からの距離を格納するリスト
color = [True for i in range(n+1)]#発見したらFalseになるリスト
q = deque([1])
d[1] = 0
color[1] = False

while len(q) != 0:
    u = q.popleft()
    for v in adjl[u]:
        if color[v]:
            d[v] = d[u]+1
            color[v] = False
            q.append(v)

for i in range(1, n+1):
    print(i, d[i])
