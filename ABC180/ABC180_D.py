#n = int(input())
x, y, a, b = map(int, input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

i = 0
mx = 0
while x*(a**i) < y:
    mx = max(mx, i+(y-x*(a**i)-1)//b)
    i += 1
print(mx)
