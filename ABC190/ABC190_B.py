#n = int(input())
n,s,d = map(int,input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

ans='No'

for i in range(n):
    x,y= map(int,input().split())
    if x<s and y>d:
        ans='Yes'
print(ans)