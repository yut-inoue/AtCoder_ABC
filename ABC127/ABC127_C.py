n,m=map(int,input().split())
left=[]
right=[]
for i in range(m):
    l,r=map(int,input().split())
    left.append(l)
    right.append(r)

if max(left)>min(right):
    print(0)
else:
    print(min(right)-max(left)+1)







