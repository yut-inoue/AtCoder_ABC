n=int(input())
al=list(map(int,input().split()))

dic={}
for v in al:
    if not v in dic.keys():
        dic[v]=1
    else:
        dic[v]=dic[v]+1
count_l=[]
for v in range(min(al)-1,max(al)+2):
    count=0
    count=dic.get(v-1,0)+dic.get(v,0)+dic.get(v+1,0)
    count_l.append(count)
print(max(count_l))



