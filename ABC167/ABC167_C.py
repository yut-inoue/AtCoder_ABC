#n=int(input())
n,m,x=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

price_list=[]
cl=[]
al=[]
for i in range(n):
    l=list(map(int,input().split()))
    cl.append(l[0])
    al.append(l[1:])


for i in range(2**n):
    b=bin(i)
    price=0
    score=[0 for k in range(m)]
    #print(b)
    # それぞれの組み合わせ
    for j in range(n):
        if ((i >> j) & 1):#二進数iの下から数えてj桁目が1か否か
            a=al[j]
            for k in range(m):
                score[k]=score[k]+a[k]
            price+=cl[j]
    # if x<
    if min(score)>=x:
        price_list.append(price)

if len(price_list)==0:
    print('-1')
else:
    print(min(price_list))
