#n = int(input())
sx, sy, gx, gy = map(int, input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

add = abs(gx-sx)*(sy/(sy+gy))

if sx <= gx:
    ans = sx+add
else:
    ans = sx-add

print('{:.9f}'.format(ans))
