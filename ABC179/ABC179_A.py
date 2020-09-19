#n = int(input())
#a, b = map(int,input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
s = input()
if s[-1] != 's':
    ans = s+'s'
else:
    ans = s+'es'
print(ans)
