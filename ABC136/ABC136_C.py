n=int(input())
#a,b=map(int,input().split())
hl=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
mx=hl[0]
flag=True
for i in range(n):
    mx=max(mx,hl[i])
    if hl[i]>=mx-1:
        pass
    else:
        flag=False
        break
if flag:
    print("Yes")
else:
    print("No")





