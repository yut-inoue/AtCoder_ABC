n=int(input())
t,a=map(int,input().split())
hl=list(map(int,input().split()))
gap=abs(a-(t-hl[0]*0.006))
#print(gap)
city=1
for i in range(2,n+1):
    temp_gap=abs(a-(t-hl[i-1]*0.006))
    #print(i,temp_gap)
    if temp_gap<gap:
        gap=temp_gap
        city=i
print(city)



