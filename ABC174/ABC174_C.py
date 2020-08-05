k = int(input())

if k == 1:
    ans = 1
elif k % 2 == 0 or k % 5 == 0:
    ans = -1
else:
    l = (9*k//7) if k % 7 == 0 else 9*k
    v = 1
    for i in range(1, l+1):
        v = (v*10) % l
        if v == 1:
            ans = i
            break
print(ans)
