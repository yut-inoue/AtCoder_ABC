x = int(input())
#a, b = map(int,input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
d=0
while True:
    d=d+100
    if x<d:
        ans=d-x
        break

print(ans)

