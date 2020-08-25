#n = int(input())
n,x,t = map(int,input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
v=0
if n%x==0:
    ans=(n//x)*t
else:
    ans=(n//x)*t+t
print(ans)