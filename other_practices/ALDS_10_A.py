n = int(input())
F = [0]*45
F[0], F[1] = 1, 1


def fib(n):
    if n == 1 or n == 0:
        return F[n]
    if F[n] != 0:
        return F[n]
    F[n] = fib(n-1)+fib(n-2)
    return F[n]


print(fib(n))
