#n=int(input())
x,y=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
flag=False
for i in range(x+1):
    j=x-i
    foot=i*2+j*4
    if foot==y:
        flag=True
        break
if flag:
    print("Yes")
else:
    print("No")