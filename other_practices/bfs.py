from collections import deque
#n,m=map(int,input().split())
n=int(input())
G=[[] for i in range(n+1)]# 隣接リスト
"""
for i in range(m):# 隣接リストを格納
    a,b=map(int,input().split())
    templ=G[a]
    templ.append(b)
    G[a]=templ
    templ=G[b]
    templ.append(a)
    G[b]=templ
"""

for i in range(n):
    l=list(map(int,input().split()))
    G[l[0]]=l[2:]


dist=[-1 for i in range(n+1)]
q=deque([1])
dist[1]=0

while len(q)!=0:
    v=q.popleft()
    for nv in G[v]:
        if dist[nv]!=-1:
            continue
        dist[nv]=dist[v]+1
        q.append(nv)

for i in range(1,n+1):
    print("{0} {1}".format(i,dist[i]))


