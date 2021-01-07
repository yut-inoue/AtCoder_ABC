n = int(input())
#a, b = map(int,input().split())
#l = list(map(int,input().split()))
dl = [list(map(int, input().split())) for i in range(n)]
count = 0

for i in range(n):
    for j in range(i+1, n):
        x1, y1 = dl[i]
        x2, y2 = dl[j]
        if x1 == x2:
            continue
        count += int(abs((y2-y1)/(x2-x1)) <= 1)

print(count)
