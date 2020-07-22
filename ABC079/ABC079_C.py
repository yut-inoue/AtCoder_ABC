# n=int(input())
# a,b=map(int,input().split())
# l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
s = list(input())
l = [int(s[0]), int(s[1]), int(s[2]), int(s[3])]

for i in range(2**3):
    opt = ['+', '+', '+']
    for j in range(3):
        if ((i >> j) & 1):
            opt[j] = '-'
    test = l[0]
    for k in range(3):
        if opt[k] == '+':
            test += l[k+1]
        else:
            test -= l[k+1]
    if test == 7 :
        break
printstr=str(l[0])
for i in range(3):
    printstr+=opt[i]+str(l[i+1])
print(printstr+'=7')