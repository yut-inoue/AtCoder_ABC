n=int(input())
sl=list(input())

count=1

for i in range(n-1):
    if sl[i]!=sl[i+1]:
        count+=1
print(count)



