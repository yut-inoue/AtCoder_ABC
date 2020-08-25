#n = int(input())
from collections import deque
r, c = map(int, input().split())
sx, sy = map(int, input().split())
gx, gy = map(int, input().split())
#c = list(map(int,input().split()))
C = [list(input()) for i in range(r)]

adjdic = {}
color = {}
d = {}

for row in range(2, r):
    for col in range(2, c):
        tempr = row-1
        tempc = col-1
        adjdic[(row, col)] = []
        if C[tempr-1][tempc] == '.':
            adjdic[(row, col)].append((row-1, col))
        if C[tempr+1][tempc] == '.':
            adjdic[(row, col)].append((row+1, col))
        if C[tempr][tempc+1] == '.':
            adjdic[(row, col)].append((row, col+1))
        if C[tempr][tempc-1] == '.':
            adjdic[(row, col)].append((row, col-1))
        color[(row, col)] = True
        d[(row, col)] = 0


q = deque([(sx, sy)])
d[(sx, sy)] = 0
color[(sx, sy)] = False

while len(q) != 0:
    u = q.popleft()
    for v in adjdic[u]:
        if color[v]:
            d[v] = d[u]+1
            color[v] = False
            q.append(v)

print(d[(gx, gy)])
