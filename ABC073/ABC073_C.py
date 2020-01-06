n=int(input())
dic={}
for i in range(n):
    v=int(input())
    dic[v]=dic.get(v,0)+1
count=0

for k in dic.keys():
    if dic[k]%2!=0:
        count+=1
print(count)
