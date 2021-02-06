#n = int(input())
n, x = map(int, input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
x = 100*x
ans = -1
total = 0
for i in range(n):
    v, p = map(int, input().split())
    total += v*p
    if total > x:
        ans = i+1
        break
print(ans)
