#n = int(input())
a, b, c, d = map(int, input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

l = [a*c, a*d, b*c, b*d]

print(max(l))
