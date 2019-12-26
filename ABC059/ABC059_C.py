n=int(input())
a=list(map(int,input().split()))

def sig(v):
    if v >0:
        return "+"
    elif v<0:
        return "-"
    else:
        return "0"

c_total_sig="+"
c_total=0
cost1=0

for i in range(n):
    temp_total=c_total+a[i]
    temp_total_sig=sig(temp_total)
    #print(i,c_total,temp_total)
    plus=a[i]
    if c_total_sig==temp_total_sig:
        #print(i,c_total,temp_total)
        dif=abs(temp_total)+1
        cost1+=dif
        if temp_total_sig=="-":
            plus=a[i]+dif
        elif temp_total_sig=="+":
            plus=a[i]-dif
    if temp_total_sig=="0" and c_total_sig=="-":
        dif=abs(temp_total)+1
        cost1+=dif
        plus=a[i]+dif
    elif temp_total_sig=="0" and c_total_sig=="+":
        dif=abs(temp_total)+1
        cost1+=dif
        plus=a[i]-dif
    c_total+=plus
    c_total_sig=sig(c_total)

c_total_sig="-"
c_total=0
cost2=0
#print("---------------")
for i in range(n):
    temp_total=c_total+a[i]
    temp_total_sig=sig(temp_total)
    #print(i,c_total,temp_total)
    plus=a[i]
    if c_total_sig==temp_total_sig:
        #print(i,c_total,temp_total)
        dif=abs(temp_total)+1
        cost2+=dif
        if temp_total_sig=="-":
            plus=a[i]+dif
        elif temp_total_sig=="+":
            plus=a[i]-dif
    if temp_total_sig=="0" and c_total_sig=="-":
        dif=abs(temp_total)+1
        cost2+=dif
        plus=a[i]+dif
    elif temp_total_sig=="0" and c_total_sig=="+":
        dif=abs(temp_total)+1
        cost2+=dif
        plus=a[i]-dif
    c_total+=plus
    c_total_sig=sig(c_total)
print(min(cost1,cost2))
