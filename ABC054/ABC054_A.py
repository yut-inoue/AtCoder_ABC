#n = int(input())
n, m = map(int, input().split())
#l = list(map(int,input().split()))
al = [list(input()) for i in range(n)]
bl = [list(input()) for i in range(m)]


def same(i, j):
    res = True
    for row in range(m):
        for col in range(m):
            if al[i+row][j+col] != bl[row][col]:
                res = False
    return res


ans = 'No'
for i in range(n-m+1):
    for j in range(n-m+1):
        if same(i, j):
            ans = 'Yes'
print(ans)
