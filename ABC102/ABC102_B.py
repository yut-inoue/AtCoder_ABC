n=int(input())
#a,b=map(int,input().split())
a=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
mx=abs(a[0]-a[1])
for i in range(n):
    for j in range(i+1,n):
        mx=max(mx,abs(a[i]-a[j]))

print(mx)




