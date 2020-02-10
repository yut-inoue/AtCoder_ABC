n,k=map(int,input().split())
pl=list(map(int,input().split()))

cuml=[]
cum=0
for i in range(n):
    cum+=(pl[i]+1)/2
    cuml.append(cum)
mx=0
#cumsum
for i in range(n-(k-1)):
    if i==0:
        mx=max(cuml[i+k-1],mx)
    else:
        mx=max(cuml[i+k-1]-cuml[i-1],mx)
print('{:.9f}'.format(mx))

