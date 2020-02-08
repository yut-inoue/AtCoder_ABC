n=int(input())
sl=list(input())

ch=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
ans=""
for s in sl:
    ind=ch.index(s)
    ans+=ch[(ind+n)% 26]
print(ans)