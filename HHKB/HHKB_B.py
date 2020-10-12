#n = int(input())
import copy
h, w = map(int, input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#s=[list(map(int,input().split())) for i in range(n)]
dic = {}
s = [['#' for _ in range(w+2)]]
for i in range(h):
    temp = list(input())
    temp.insert(0, '#')
    temp.append('#')
    s.append(copy.deepcopy(temp))
s.append(['#' for _ in range(w+2)])
# print(s)
ans = 0

for i in range(1, h+1):
    for j in range(1, w+1):
        if s[i][j] == '.' and s[i][j+1] == '.':
            ans += 1

for j in range(1, w+1):
    for i in range(1, h+1):
        if s[i][j] == '.' and s[i+1][j] == '.':
            ans += 1


print(ans)
