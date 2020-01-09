n,k=map(int,input().split())
ans=0
for i in range(1,n+1):
    temp=i
    count=0
    while temp<k:
        temp=temp*2
        #print(temp)
        count+=1
    ans+=0.5**count
print('{:.11f}'.format(ans/n))


