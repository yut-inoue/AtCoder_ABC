n = int(input())
#a, b = map(int,input().split())
al = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
ans = 0
for l in range(n):
    mn = al[l]
    for r in range(l, n):
        mn = min(mn, al[r])
        ans = max(ans, (r-l+1)*mn)

print(ans)
