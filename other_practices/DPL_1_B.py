#n = int(input())
import copy
n, w = map(int, input().split())
#al = list(map(int, input().split()))
#al=[list(input()) for i in range(n)]
vl = [0]*n
wl = [0]*n
for i in range(n):
    vl[i], wl[i] = map(int, input().split())
temp = [0]*(w+1)
dp = [copy.deepcopy(temp) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(w+1):
        if j < wl[i-1]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-wl[i-1]]+vl[i-1], dp[i-1][j])

print(dp[n][w])
