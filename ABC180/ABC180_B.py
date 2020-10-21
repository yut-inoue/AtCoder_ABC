import math
n = int(input())
#a, b = map(int,input().split())
xl = list(map(int, input().split()))
# l = [list(map(int,inp
man, eu, ch = 0, 0, abs(xl[0])

for x in xl:
    man += abs(x)
    eu += abs(x)**2
    ch = max(ch, abs(x))

eu = math.sqrt(eu)

print('{:.11f}'.format(man))
print('{:.11f}'.format(eu))
print('{:.11f}'.format(ch))
