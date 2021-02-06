#n = int(input())
a, b, c = map(int, input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

while True:
    if c == 0:
        if a == 0:
            ans = 'Aoki'
            break
        elif b == 0:
            ans = 'Takahashi'
            break
    else:
        if b == 0:
            ans = 'Takahashi'
            break
        elif a == 0:
            ans = 'Aoki'
            break
    a -= 1
    b -= 1
print(ans)
