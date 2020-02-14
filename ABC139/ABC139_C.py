n=int(input())
hl=list(map(int,input().split()))
mx=0
count=0
for i in range(n-1):
    if hl[i]>=hl[i+1]:
        count+=1
    else:
        mx=max(mx,count)
        count=0
mx=max(mx,count)
print(mx)
