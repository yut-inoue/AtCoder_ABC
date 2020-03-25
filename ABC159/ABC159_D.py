n=int(input())
#a,b=map(int,input().split())
al=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

dic={}

for a in al:
    dic[a]=dic.get(a,0)+1
total=0
for k in dic.keys():
    total+=dic[k]*(dic[k]-1)//2

for k in range(n):
    count=dic[al[k]]
    ans=total-count*(count-1)//2+(count-1)*(count-2)//2
    print(ans)
