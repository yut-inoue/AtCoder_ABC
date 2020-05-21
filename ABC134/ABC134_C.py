n=int(input())
dic={}
mx=0
al=[]
for i in range(n):
    a=int(input())
    al.append(a)

order=sorted(al,reverse=True)
mx1=order[0]
mx2=order[1]

for a in al:
    if a==mx1:
        print(mx2)
    else:
        print(mx1)
