n=int(input())
dic={}

for i in range(n):
    s=input()
    count=dic.get(s,0)
    count+=1
    dic[s]=count
mx=1
for v in dic.values():
    mx=max(v,mx)
ans=[]
for k,v in dic.items():
    if v==mx:
        ans.append(k)
ans.sort()
#print("---")
for st in ans:
    print(st)


