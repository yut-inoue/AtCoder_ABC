from collections import deque
import gc
h, w, n = map(int, input().split())
l = [['X' for j in range(w+2)]]
for i in range(1, h+1):
    l.append(['X'])
    l[i].extend(list(input()))
    l[i].append('X')

l.append(['X' for j in range(w+2)])
# print(l)


def tonode(i, j):
    return ((w+2)*i)+j+1


adjl = [[] for _ in range((h+2)*(w+2)+1)]
chplace = {}
#chlevel = {}
# adjlを作成する
for i in range(1, h+1):
    for j in range(1, w+1):
        u = tonode(i, j)
        if l[i][j+1] != 'X':
            adjl[u].append(tonode(i, j+1))
        if l[i][j-1] != 'X':
            adjl[u].append(tonode(i, j-1))
        if l[i+1][j] != 'X':
            adjl[u].append(tonode(i+1, j))
        if l[i-1][j] != 'X':
            adjl[u].append(tonode(i-1, j))
        if l[i][j] != '.' and l[i][j] != 'X':
            chplace[l[i][j]] = u
            #if l[i][j] != 'S':
            #    chlevel[u] = int(l[i][j])

del l
gc.collect()
# bfs

def bfs(start_node, color_id):  # start_nodeは探索の開始点
    global color, d
    q = deque([start_node])
    d[start_node] = 0
    color[start_node] = color_id
    while len(q) != 0:
        u = q.popleft()
        for v in adjl[u]:
            if color[v] == NIL :
                d[v] = d[u]+1
                if v == goal:
                    return
                color[v] = color_id
                q.append(v)


start = chplace['S']
NIL = -1  # 未発見を示す値
maxnode = (h+2)*(w+2)
ans = 0
for i in range(1, n+1):
    goal = chplace[str(i)]
    #print(start, goal)
    d = [-1 for i in range(maxnode+1)]  # 頂点1からの距離を格納するリスト
    color = [NIL for i in range(maxnode+1)]  # 未到達かを示すリスト
    hp = i
    bfs(start, 1)
    #print(i, d[goal])
    start = chplace[str(i)]
    ans += d[goal]

print(ans)
