a=[list(map(int,input().split())) for i in range(3)]
n=int(input())
bl=[int(input()) for i in range(n)]

for i in range(3):
    for j in range(3):
        if a[i][j] in bl:
            a[i][j]=0
flag=False
for i in range(3):
    total=0
    if sum(a[i])==0:
        flag=True
        break
    for j in range(3):
        total+=a[j][i]
    if total==0:
        flag=True
        break
    if flag:
        break
if a[0][0]+a[1][1]+a[2][2]==0:
    flag=True
elif a[2][0]+a[1][1]+a[0][2]==0:
    flag=True
if flag:
    print("Yes")
else:
    print("No")