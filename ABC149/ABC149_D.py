n,k=map(int,input().split())
r,s,p=map(int,input().split())
tl=list(input())

win={"r":"p","s":"r","p":"s"}
score={"r":r,"s":s,"p":p}
total=0
already=[]
for i in range(k):
    win_hand=win[tl[i]]
    already.append(win_hand)
    total+=score[win_hand]
temp=["r","s","p"]
for j in range(k,n):
    temp=["r","s","p"]
    win_hand=win[tl[j]]
    #print(j-k)
    if already[j-k]==win_hand:
        temp.remove(win_hand)
        if j+k <= n-1:
            keep=win[tl[j+k]]
            if not keep in temp:
                already.append(temp[0])
            else:
                temp.remove(keep)
                already.append(temp[0])
        else:
            already.append(temp[0])
        pass
    else:
        already.append(win_hand)
        total+=score[win_hand]
print(total)






