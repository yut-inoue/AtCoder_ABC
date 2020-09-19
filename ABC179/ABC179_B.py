n = int(input())
#a, b = map(int,input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
count = 0
mx = 0
for i in range(n):
    d1, d2 = map(int, input().split())
    if d1 == d2:
        count += 1
    else:
        count = 0
    mx = max(count, mx)
if mx >= 3:
    print('Yes')
else:
    print('No')
