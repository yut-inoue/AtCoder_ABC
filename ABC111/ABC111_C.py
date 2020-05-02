n=int(input())
#a,b=map(int,input().split())
vl=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

dic1={};dic2={}

for i in range(n):
    v=vl[i]
    if i%2==0:
        dic1[v]=dic1.get(v,0)+1
    else:
        dic2[v]=dic2.get(v,0)+1

dic1=sorted(dic1.items(),reverse=True,key=lambda x:x[1])
dic2=sorted(dic2.items(),reverse=True,key=lambda x:x[1])

#dic1の最頻値
mx1_val,mx1_count=dic1[0]
if len(dic1)==1:
    mx1_count2=0
else:
    mx1_count2=dic1[1][1]

mx2_val,mx2_count=dic2[0]
if len(dic2)==1:
    mx2_count2=0
else:
    mx2_count2=dic2[1][1]

ans=0
ansl=[]
total=n//2
if n==2:
    if vl[0]==vl[1]:
        ans=1
    else:
        ans=0
    print(ans)
else:
    if mx1_val != mx2_val:
        ans=n-(mx1_count+mx2_count)
    else:
        ans=min(n-mx1_count-mx2_count2,
        n-mx1_count2-mx2_count)
    print(ans)