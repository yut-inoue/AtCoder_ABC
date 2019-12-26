n=int(input())
s,t=map(str,input().split())
s=list(s);t=list(t)
ans=[]

for i in range(n):
    ans.append(s[i])
    ans.append(t[i])
print("".join(ans))
