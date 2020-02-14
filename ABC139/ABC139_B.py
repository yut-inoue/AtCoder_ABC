a,b=map(int,input().split())

socket=1
tap=0
while socket<b:
    tap+=1
    socket-=1
    socket+=a
print(tap)
