#n = int(input())
a, b, c = map(int,input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

if a == b :
    print(c)
elif b == c :
    print(a)
else:
    print(b)
