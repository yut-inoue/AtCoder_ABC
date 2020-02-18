a,b,c=map(int,input().split())

l=[a,b,c]

l2=list(set(l))

if len(l2)==2:
    print("Yes")
else:
    print("No")


