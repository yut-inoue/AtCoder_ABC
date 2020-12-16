l = int(input())
#a, b = map(int,input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
import math

def combinations_count(n, k):
    if k == 0 or k == n:
        return 1
    elif n < k or k < 0:
        return 0
    else:
        return math.factorial(n)//(math.factorial(n-k)*math.factorial(k))

print(combinations_count(l-1, 11))