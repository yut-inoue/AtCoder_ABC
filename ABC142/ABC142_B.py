n,k=map(int,input().split())
hl=list(map(int,input().split()))
count=0
for i in range(n):
    if k<=hl[i]:
        count+=1
print(count)
