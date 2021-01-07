n = int(input())
#a, b = map(int,input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
dic1 = {}
dic2 = {}
ans = 'satisfiable'
for i in range(n):
    s = input()
    if s[0] == '!':
        dic1[s[1:]] = True
        if dic2.get(s[1: ], False):
            ans = s[1:]
            #break
    else:
        dic2[s] = True
        if dic1.get(s, False):
            ans = s
            #break
print(ans)
