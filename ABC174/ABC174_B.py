#n = int(input())
n, d = map(int, input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
ans = 0
for i in range(n):
    x, y = map(int, input().split())
    if x**2 + y**2 <= d**2:
        ans += 1
print(ans)
