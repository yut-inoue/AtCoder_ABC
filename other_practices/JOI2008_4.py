m = int(input())
target = [list(map(int, input().split())) for i in range(m)]
n = int(input())
stars = []
dic = {}
for i in range(n):
    x, y = map(int, input().split())
    stars.append([x, y])
    dic[(x, y)] = True
x, y = target[0]
for i in range(n):
    x2, y2 = stars[i]
    xmove = x2-x
    ymove = y2-y
    movedtarget = []
    for j in range(m):
        movedtarget.append([target[j][0] + xmove, target[j][1] + ymove])
    # すべて含んでいるか判定
    boollist = []
    for j in range(m):
        boollist.append(dic.get((movedtarget[j][0], movedtarget[j][1]), False))
    if all(boollist):
        break
print('{0} {1}'.format(xmove, ymove))
