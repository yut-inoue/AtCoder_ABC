n=int(input())
hl=list(map(int,input().split()))
count=0
temp_count=0
for i in range(n-1):
    if hl[i]>=hl[i+1]:
        temp_count+=1
    else:
        if count<temp_count:
          count=temp_count
        temp_count=0
if count<temp_count:
    count=temp_count
print(count)