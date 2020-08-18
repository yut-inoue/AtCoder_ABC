#n = int(input())
x, k, d = map(int, input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

x_abs = abs(x)
movenum = x_abs//d
if movenum >= k:
    ans = x_abs-d*k
else:
    x_abs -= d*movenum
    numleft = k-movenum
    if numleft % 2 == 0:
        ans = x_abs
    else:
        ans = abs(x_abs-d)
print(ans)
