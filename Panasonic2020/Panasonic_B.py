# n=int(input())
h, w = map(int, input().split())
# l=list(map(int,input().split()))
al = [list(map(int, input().split())) for i in range(h)]
mn = 100
for ai in al:
    mn = min(mn, min(ai))
ans = 0
for i in range(h):
    for j in range(w):
        ans += abs(al[i][j]-mn)
print(ans)
