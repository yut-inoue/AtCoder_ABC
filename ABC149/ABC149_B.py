a,b,k=map(int,input().split())
takahashi=0
if a>= k:
    #a=a-k
    takahashi=a-k
else:
    dif=k-a
    takahashi=0    
    #print(dif)
    b=b-dif
    if b<0:
        b=0
print("{0} {1}".format(takahashi,b))
