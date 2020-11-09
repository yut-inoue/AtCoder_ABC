n = int(input())
#a, b = map(int,input().split())
al = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
mx = max(al)
ans = {}
for i in range(2, mx+1):
    count = 0
    for ai in al:
        if ai % i == 0:
            count += 1
    ans[i] = count
l = sorted(ans.items(), key=lambda x: x[1])
print(l[-1][0])
