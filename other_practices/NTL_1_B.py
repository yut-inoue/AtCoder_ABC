m, n = map(int, input().split())
mod = 10**9 + 7


def modpow(a, n, mod):
    # a^nをmodでわったあまり 二分累乗法O(logn)
    res = 1
    while n > 0:
        if n & 1:
            res = (res*a) % mod
        a = (a*a) % mod
        n = n >> 1
    return res


print(modpow(m, n, mod))
