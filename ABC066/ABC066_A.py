#n = int(input())
a, b, c = map(int, input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

l = [a, b, c]
l.sort()
print(l[0]+l[1])
