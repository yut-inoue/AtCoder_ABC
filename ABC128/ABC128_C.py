n,m=map(int,input().split())

l=[list(map(int,input().split())) for i in range(m)]

pl=list(map(int,input().split()))
ans=0
#中身を扱いやすいように加工する
kl=[]
sl=[]
for i in range(m):
    templ=l[i]
    k=templ[0]
    kl.append(k)
    sl.append(templ[1:k+1])

for i in range(2**n):
    #b=bin(i)
    pt=[0 for l in range(n)]
    for j in range(n):
        if ((i >> j) & 1):
            pt[j]=1
    flag=True#全ての電球が点灯するか
    for l in range(m):#1つの電球についてチェック
        count=0
        k=kl[l]
        s=sl[l]
        for sw in s:
            if pt[sw-1]==1:
                count+=1
        if count%2!=pl[l]:
            flag=False
            break
    if flag:
        ans+=1
    
print(ans)