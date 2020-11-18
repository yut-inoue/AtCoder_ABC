#n = int(input())
import itertools
n, k = map(int, input().split())
#l = list(map(int,input().split()))
tl = [list(map(int, input().split())) for i in range(n)]

ans = 0
cities = [i for i in range(n)]
for v in itertools.permutations(cities):
    t = 0
    if v[0] != 0:
        continue
    for j in range(1, n):
        t += tl[v[j]][v[j-1]]
    t += tl[v[-1]][0]
    if t == k:
        ans += 1
print(ans)
