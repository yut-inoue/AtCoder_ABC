n=int(input())
dic={}
dist=[]

#def other2points()

for i in range(n):
    x,y = map(int,input().split())
    dic[(x,y)]=1
    dist.append([x,y])
mx=0
for i in range(n-1):
    xi,yi=dist[i]
    for j in range(i,n):
        xj,yj=dist[j]
        q=(xj-yj+yi,yj+xj-xi)
        r=(xi-yj+yi,yi+xj-xi)
        if dic.get(q,0) and dic.get(r,0):
            mx=max(mx,(xj-xi)**2+(yj-yi)**2)
print(mx)
