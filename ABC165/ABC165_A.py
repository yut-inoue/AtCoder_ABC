k=int(input())
a,b=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
flag=False
for i in range(a,b+1):
    if i%k==0:
        flag=True
        break
if flag:
    print("OK")
else:
    print("NG")
    



