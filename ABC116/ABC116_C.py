n=int(input())
#a,b=map(int,input().split())
hl=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

mx=max(hl)
count=0
for height in range(1,mx+1):
    i=0
    while i<n:
        if hl[i]>=height:
            count+=1
            while i<n and hl[i]>=height :
                i+=1
        else:
            i+=1

print(count)

