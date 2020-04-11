#n=int(input())
n,m=map(int,input().split())
al=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

total=sum(al)

thre=total/(4*m)
count=0
for i in range(n):
    if al[i]>=thre:
        count+=1

if count>=m:
    print("Yes")
else:
    print("No")
