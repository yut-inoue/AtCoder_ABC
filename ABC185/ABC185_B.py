#n = int(input())
n, m, t = map(int, input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
flag = 'Yes'
full = n
leave = 0
for i in range(m):
    a, b = map(int, input().split())
    # release
    n -= (a-leave)
    if n <= 0:
        flag = 'No'
    # charge
    n = n+(b-a)
    n = min(n, full)

    leave = b
n -= (t-leave)
if n <= 0:
    flag = 'No'
print(flag)
