#n=int(input())
import copy
h,w,K=map(int,input().split())
#l=list(map(int,input().split()))
l=[list(input()) for i in range(h)]
rowl=[]
coll=[]

def count_black(l2d):
    res=0
    for l in l2d:
        res+=l.count('#')
    return res

for i in range(2**h):
    temp=[]
    for k in range(h):
        if ((i >> k) & 1):#二進数iの下から数えてj桁目が1か否か
            temp.append(k)
    rowl.append(temp)
for j in range(2**w):
    temp=[]
    for k in range(w):
        if ((j >> k) & 1):
            temp.append(k)
    coll.append(temp)

count=0
# 全探索
rowall=["r" for i in range(w)]
for row in rowl:
    for col in coll:
        test=copy.deepcopy(l)
        for i in row:
            test[i]=rowall
        for j in col:
            for i in range(h):
                test[i][j]='r'
        if count_black(test)==K:
            count+=1

print(count)
