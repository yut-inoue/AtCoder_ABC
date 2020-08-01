n = int(input())
#k, x = map(int, input().split())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))
cl = list(map(int, input().split()))
import bisect
al.sort();bl.sort();cl.sort()
ans=0
for bi in bl:
    c1 = bisect.bisect_right(al, bi-1)
    c2 = n-bisect.bisect_left(cl, bi+1)
    ans += c1*c2
print(ans)