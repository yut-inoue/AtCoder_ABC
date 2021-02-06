x = int(input())
#a, b = map(int,input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
ans = (x//11)*2
if 0< x % 11 <= 6:
    ans += 1
elif x%11 > 6 :
    ans += 2

print(ans)
