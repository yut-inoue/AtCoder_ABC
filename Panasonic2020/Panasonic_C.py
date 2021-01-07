n = int(input())
# a,b,c=map(int,input().split())
# l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]


def n_base_digit(v, n):
    res = []
    while v != 0:
        c = v % n
        res.append(c)
        v = v//n
    res = res[::-1]
    return (''.join(map(str, res)))


total = 0
for i in range(1, n+1):
    if '7' in str(i) or '7' in n_base_digit(i, 8):
        total += 1
print(n-total)
