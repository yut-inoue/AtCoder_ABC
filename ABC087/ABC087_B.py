a = int(input())
b = int(input())
c = int(input())
x = int(input())
# a,b=map(int,input().split())
# l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
count=0
for i in range(0, a+1):
    for j in range(0, b+1):
        for k in range(0, c+1):
            if i*500+j*100+k*50==x:
                count+=1
print(count)
