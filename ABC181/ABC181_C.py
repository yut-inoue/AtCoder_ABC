import itertools
n = int(input())
#a, b = map(int,input().split())
#l = list(map(int,input().split()))
pl = [list(map(int, input().split())) for i in range(n)]

flag = 'No'
for v in itertools.permutations(pl, 3):
    p1, p2, p3 = v
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    rhs = (y3-y1)*(x2-x1)
    lhs = (y2-y1)*(x3-x1)
    if rhs == lhs:
        flag = 'Yes'
        break

print(flag)
