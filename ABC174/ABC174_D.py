n = int(input())
cl = list(input())

ans = cl.count('R')
r = cl.count('R')
w = 0
for i in range(n):
    if cl[i] == 'W':
        w += 1
    else:
        r -=1
    ans=min(max(r,w),ans)
print(ans)