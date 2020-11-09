#n = int(input())
a, b = map(int,input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

mx = 2*a+100

print(max(0, mx-b))
