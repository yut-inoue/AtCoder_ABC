#n = int(input())
a, b, c, d = map(int, input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
ans = 'No'
if a <= c:
    if c <= b:
        ans = 'Yes'
else:
    if a <= d:
        ans = 'Yes'
print(ans)
