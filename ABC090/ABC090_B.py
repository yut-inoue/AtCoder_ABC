#n=int(input())
a,b=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
count=0
for i in range(a,b+1):
    istr=str(i)
    if istr[0]==istr[4] and istr[1]==istr[3]:
        count+=1
print(count)
