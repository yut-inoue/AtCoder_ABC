nl = list(input())
#a, b = map(int,input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
total=0
for v in nl:
    v2=int(v)
    total+=v2
if total%9==0:
    print('Yes')
else:
    print('No')