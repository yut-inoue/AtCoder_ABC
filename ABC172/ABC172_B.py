#n=int(input())
#a,b=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
s=list(input())
t=list(input())
count=0
for si, vi in zip(s,t):
    if si!=vi:
        count+=1
print(count)
