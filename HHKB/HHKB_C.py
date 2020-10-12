n = int(input())
#a, b = map(int,input().split())
pl = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

dic = {}

mn = 0
mx = pl[0]
for i in range(n):
    dic[pl[i]] = True
    if pl[i] == mn:
        while True:
            if not dic.get(mn, False):
                break
            mn += 1
        print(mn)
    else:
        print(mn)
