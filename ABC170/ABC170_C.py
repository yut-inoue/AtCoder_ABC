#n=int(input())
x,n=map(int,input().split())
pl=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
ans=x
if not x in pl:
    ans=x
else:
    for i in range(1,1000):
        x1=x+i
        x2=x-i
        if not x2 in pl:
            ans=x2
            break
        elif not x1 in pl:
            ans=x1
            break
print(ans)
