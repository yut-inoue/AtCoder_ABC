n,k,m=map(int,input().split())
al=list(map(int,input().split()))

t=sum(al)


flag=False
for i in range(0,k+1):
    if (t+i)/n >=m:
        flag=True
        break

if flag:
    print(i)
else:
    print("-1")