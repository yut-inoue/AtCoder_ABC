n = int(input())
#a, b = map(int,input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
ans = 0
for i in range(n):
    a, b = map(int, input().split())
    ans += (b-a+1)*(a+b)//2
print(ans)
