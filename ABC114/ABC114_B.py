s=list(input())
n=len(s)
v=753
ans=[]
for i in range(n-2):
  temp=int("".join(s[i:i+3]))
  ans.append(abs(temp-v))
print(min(ans))
