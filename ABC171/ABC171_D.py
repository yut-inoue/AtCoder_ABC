n=int(input())
#a,b=map(int,input().split())
al=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
q=int(input())
dic={}
for a in al:
    dic[a]=dic.get(a,0)+1

total=sum(al)
ansl=[]
for i in range(q):
    b,c=map(int,input().split())
    b_num=dic.get(b,0)
    total=total+b_num*(c-b)
    ansl.append(total)
    dic[b]=0
    dic[c]=dic.get(c,0)+b_num

for ans in ansl:
    print(ans)
