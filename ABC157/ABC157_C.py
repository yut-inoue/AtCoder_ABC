n,m=map(int,input().split())
sl=[];cl=[]
for i in range(m):
    s,c=map(int,input().split())
    sl.append(s)
    cl.append(c)

isThere=False
#ans=10**n-1

for i in range(10**n):
    st=list(str(i))
    flag=True
    if len(st)==n:
        for j in range(m):
            if st[sl[j]-1]!=str(cl[j]):
                flag=False
                break
        if flag:
            isThere=True
            ans=i
    if isThere:
        break
if isThere:
    print(ans)
else:
    print(-1)
