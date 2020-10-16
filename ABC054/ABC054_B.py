#n = int(input())
a, b = map(int, input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

l = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1]
aind = l.index(a)
bind = l.index(b)

if aind == bind:
    print('Draw')
elif aind < bind:
    print('Bob')
else:
    print('Alice')
