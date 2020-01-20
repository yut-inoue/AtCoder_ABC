n=int(input())
pl=list(map(int,input().split()))

count=1
temp=pl[0]
l=[pl[0]]
for i in range(1,n):
    if pl[i]<temp:
        temp=pl[i]
        l.append(temp)
    else:
        l.append(temp)
    if pl[i]<=temp:
        count+=1
print(count)

   
