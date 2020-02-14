n=int(input())
al=list(map(int,input().split()))
bl=list(map(int,input().split()))
cl=list(map(int,input().split()))

ans=0
dish=al[0]
ans+=bl[dish-1]
bef_dish=dish
for i in range(1,n):
    dish=al[i]
    ans+=bl[dish-1]
    if dish== bef_dish+1:
        ans+=cl[bef_dish-1]
    bef_dish=dish
print(ans)
