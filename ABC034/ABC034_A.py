#n = int(input())
x, y = map(int, input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
if x < y:
    print('Better')
else:
    print('Worse')
