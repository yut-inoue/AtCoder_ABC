import bisect
d = int(input())
n = int(input())
m = int(input())
dl = [int(input()) for _ in range(n-1)]
ml = [int(input()) for _ in range(m)]

dl.append(0)
dl.append(d)
dl.sort()
dis = 0

for m in ml:
    ind = bisect.bisect_left(dl, m)
    dis += min(abs(dl[ind]-m), abs(dl[ind-1]-m))
print(dis)
