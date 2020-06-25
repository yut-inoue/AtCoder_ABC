a,b,k=map(int,input().split())

ansl=[]

for i in range(a,min(b+1,a+k)):
    ansl.append(i)
for i in range(b,max(b-k,a-1),-1):
    ansl.append(i)

ansl=list(set(ansl))
ansl.sort()
for ans in ansl:
    print(ans)