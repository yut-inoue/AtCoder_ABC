a,b,c=map(int,input().split())

l=[a,b,c]
l.sort(reverse=True)
x_max=l[0]
x_mid=l[1]
x_min=l[2]
count=0
count+=l[0]-l[1]
dif=l[0]-(l[2]+count)
if dif%2==0:
    count+=dif//2
else:
    count+=dif//2+2
print(count)



