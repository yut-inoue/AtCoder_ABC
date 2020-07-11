n=int(input())
#a,b=map(int,input().split())
al=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

count=0

for i in range(1,n+1):
    a=al[i-1]
    if i%2!=0 and a%2!=0:
        count+=1
print(count)


