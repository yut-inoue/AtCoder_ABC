n=int(input())
dic={}
ans=0
for i in range(n):
    s=list(input())
    s.sort()
    s="".join(s)
    dic[s]=dic.get(s,0)
    if dic[s]==0:
        pass
    else:
        ans+=dic[s]
    dic[s]=dic[s]+1

print(ans)