n = int(input())
# a,b=map(int,input().split())
al = list(map(int, input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

al.sort(reverse=True)
cum = [al[0]]
for i in range(1, n):
    cum.append(cum[-1]+al[i])
ans = 0
for i in range(n-2, -1, -1):
    ans += cum[i]-al[i+1]*(i+1)
print(ans)
