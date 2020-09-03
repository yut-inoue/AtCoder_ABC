#n = int(input())
d, t, s = map(int, input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

if t*s >= d:
    print('Yes')
else:
    print('No')
