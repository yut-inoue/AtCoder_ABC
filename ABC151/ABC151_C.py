n,m=map(int,input().split())
sl=[]
pl=[]
pena=0
ac=0
ac_p=[]
wa={}
acdic={}

for i in range(m):
    #p,s=map(str,input().split())
    li = input().split()
    p=int(li[0])
    s=li[1]
    #p=int(p)
    if s=="WA":
        wa[p]=wa.get(p,0)+1
    else:#もしACなら
        #acdic[p]=True
        if acdic.get(p,False)==False:
            ac+=1
            acdic[p]=True
            pena+=wa.get(p,0)

print("{0} {1}".format(ac,pena))

