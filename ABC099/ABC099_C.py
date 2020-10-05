n = int(input())


def n_base_digit_sum(v, a):
    # 10baseの自然数vをn進数で表した時の桁和
    res = 0
    while v != 0:
        res += v % a
        v = v//a
    return res


ans = n
for i in range(n+1):
    ans = min(ans, n_base_digit_sum(i, 6)+n_base_digit_sum(n-i, 9))

print(ans)
