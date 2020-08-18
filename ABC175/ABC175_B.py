n = int(input())
#a, b = map(int,input().split())
l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

ans = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            a, b, c = l[i], l[j], l[k]
            if len(set([a, b, c])) == 3:
                if a+b > c and b+c > a and a+c > b:
                    ans += 1
print(ans)
