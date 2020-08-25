n = int(input())
#a, b = map(int,input().split())
a = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
ans=0
for i in range(1,n):
    if a[i-1]<=a[i]:
        pass
    else:
        dif=a[i-1]-a[i]
        ans+=dif
        a[i]=a[i]+dif

print(ans)

