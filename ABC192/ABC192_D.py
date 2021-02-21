x = int(input())
m = int(input())
#n,k = map(int,input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
import sys
def f(x, n):
    i=0
    res=0
    while x>0:
        res+=(x%10)*(n**i)
        x=x//10
        i+=1
    return res

d=1
for si in str(x):
    d=max(d, int(si))

left=0
right=m+1
while right-left > 1:
    mid = (left+right)//2
    if f(x, mid) > m:
        right = mid
    else:
        left = mid

if x<10:
    if x<=m:
        ans=1
    else:
        ans=0
    print(ans)
    sys.exit()
print(max(0, left-(d+1)+1))
