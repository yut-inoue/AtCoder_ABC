k=int(input())
s=input()

add="..."

if len(s)<=k:
    ans=s
else:
    ans=s[:k]+add

print(ans)

