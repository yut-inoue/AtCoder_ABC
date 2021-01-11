#n = int(input())
x,y = map(int,input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

if min(x, y)+3>max(x, y):
    print('Yes')
else:
    print('No')