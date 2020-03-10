#n=int(input())
n,m=map(int,input().split())
l=[list(map(int,input().split())) for i in range(n)]

l.sort(key=lambda x: x[0])

#print(l)
money=0
count=0
for i in range(n):
    a=l[i][0];b=l[i][1]
    if (m-count)>b :
        count+=b
        money+=a*b
    else:
        money+=a*(m-count)
        count+=(m-count)
        break
print(money)
