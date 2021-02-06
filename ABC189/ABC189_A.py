#n = int(input())
#a, b = map(int,input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

c = input()
if c[0] == c[1] == c[2]:
    print('Won')
else:
    print('Lost')
