# sys.setrecursionlimit(10**7)
import sys
n = int(input())
#n, x = map(int, input().split())
#sl = list(map(int, input().split()))
#pl = [list(map(int, input().split())) for i in range(n)]
hl = []
sl = []
for i in range(n):
    h, s = map(int, input().split())
    hl.append(h)
    sl.append(s)


def possible(x):
    res = True
    # 何秒かかるかソート
    times = [(i, (x-hl[i])/sl[i]) for i in range(n)]
    times.sort(key=lambda x: x[1])
    # print(times)
    for i in range(n):
        ind = times[i][0]
        if hl[ind]+sl[ind]*i > x:
            res = False
            break
    return res


left = 0
right = max(hl)+max(sl)*n
while right-left > 1:
    mid = (left+right)//2
    if possible(mid):
        right = mid
    else:
        left = mid
print(right)