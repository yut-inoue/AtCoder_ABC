n=int(input())
al=list(map(int,input().split()))
al.sort(reverse=True)
alice=0;bob=0
for i,ai in enumerate(al):
    if i%2==0:
        alice+=ai
    else:
        bob+=ai
print(alice-bob)