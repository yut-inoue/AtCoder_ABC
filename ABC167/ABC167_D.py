#n=int(input())
n,k=map(int,input().split())
al=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

trans=[1]
dic={}
bef=1
dic[bef]=0
for i in range(n):
    trans.append(al[bef-1])
    bef=trans[-1]
    if dic.get(bef,-1)>=0:
        st=dic[bef]
        ed=i
        break
    dic[bef]=i+1
pattern=trans[st:ed+1]
until_num=st
if k<st:
    ans=trans[k]
else:
    ans=pattern[(k-st)%(ed-st+1)]
print(ans)
