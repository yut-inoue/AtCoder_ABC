#n = int(input())
n, k = map(int, input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
dic = {}
for i in range(n):
    a, b = map(int, input().split())
    dic[a] = dic.get(a, 0)+b

l = sorted(dic.items())

for a, b in l:
    if k <= b:
        ans = a
        break
    k -= b
print(ans)
