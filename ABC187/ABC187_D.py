n = int(input())
#a, b = map(int,input().split())
#l = list(map(int,input().split()))
l = [list(map(int, input().split())) for i in range(n)]
total_a = 0
temp = []
for a, b in l:
    total_a += a
    temp.append(2*a+b)

temp.sort(reverse=True)
take = 0
for i in range(n):
    take += temp[i]
    if take-total_a > 0:
        break
print(i+1)
