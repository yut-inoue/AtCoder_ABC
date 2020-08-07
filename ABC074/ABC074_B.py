n = int(input())
k = int(input())
#n, k = map(int,input().split())
xl = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
dis=0
for xi in xl:
    dis+=min(xi, abs(k-xi))*2

print(dis)
