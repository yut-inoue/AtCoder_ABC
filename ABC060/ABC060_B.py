a,b,c=map(int,input().split())

l=[(a*i)%b for i in range(1,b+1)]

if l.count(c)>=1:
    print("YES")
else:
    print("NO")

