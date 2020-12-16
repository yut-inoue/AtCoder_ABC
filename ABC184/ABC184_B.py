#n = int(input())
n, x = map(int, input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
s = input()

for si in s:
    if si == 'x':
        x = max(x-1, 0)
    else:
        x += 1
print(x)
