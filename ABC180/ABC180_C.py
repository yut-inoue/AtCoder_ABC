n = int(input())
#a, b = map(int,input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]


def enum_divisors(n):
    res = []
    i = 1
    while i*i <= n:
        if n % i == 0:
            res.append(i)
            if n//i != i:
                res.append(n//i)
        i += 1
    res.sort()
    return res


l = enum_divisors(n)
l.sort()
for v in l:
    print(v)
