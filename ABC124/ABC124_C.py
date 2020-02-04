s=list(input())
n=len(s)
dic={"0":"1","1":"0"}

temp=[]
temp.append(s[0])
ans=0
for i in range(1,n):
    temp.append(dic[temp[i-1]])

for i in range(n):
    if temp[i]!=s[i]:
        ans+=1
print(ans) 