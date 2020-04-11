#n=int(input())
n,m=map(int,input().split())
al=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

import math 
import heapq
#hq=heapq.heapify(list)#リストを優先度付きキューに変換
#val=heapq.heappop(q)#優先度付きキューから最小値を取り出して削除
#heapq.heappush(q,val)#優先度付きキューに要素を挿入

hq=[(-1)*val for val in al]
heapq.heapify(hq)

for i in range(m):
    mx=(-1)*(heapq.heappop(hq))
    newval=math.floor(mx/2)
    heapq.heappush(hq,(-1)*newval)

print(-sum(hq))

