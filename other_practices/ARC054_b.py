# sys.setrecursionlimit(10**7)
import sys
import math
p = float(input())
#n, x = map(int, input().split())
#sl = list(map(int, input().split()))
#pl = [list(map(int, input().split())) for i in range(n)]

def f(x):
    return x+p*(2**(-x/1.5))

tempx=-1.5*math.log(1.5/(p*math.log(2)))/math.log(2)
ans=f(max(0, tempx))

print('{:.11f}'.format(ans))