#n = int(input())
h, w = map(int, input().split())
ch, cw = map(int, input().split())
dh, dw = map(int, input().split())
#a = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
s = []
s.append(['#' for i in range(w+2)])
for i in range(h):
    s.append(['#'])
# s=[['#'] for i in range(h)]
s.append(['#' for i in range(w+2)])
for i in range(1, h+1):
    temp = list(input())
    s[i].extend(temp)
    s[i].append('#')

ans = 0
adjdic = {}
color = {}

for i in range(1, h+1):
    for j in range(1, w+1):
        if s[i][j]=='#':
            continue
        adjdic[(i, j)] = []
        if s[i+1][j] == '.':
            adjdic[(i, j)].append((i+1, j))
        if s[i-1][j] == '.':
            adjdic[(i, j)].append((i-1, j))
        if s[i][j+1] == '.':
            adjdic[(i, j)].append((i, j+1))
        if s[i][j-1] == '.':
            adjdic[(i, j)].append((i, j-1))
        color[(i, j)] = True

# let's start dfs.
d = {}
ispos=False
def dfs(u):
    global color
    global ispos
    global mxtel
    color[u] = False
    i,j=u
    #mxtel=min(mxtel,)
    if u==(dh,dw):
        ispos=True
    for v in adjdic[u]:
        if color[v]:
            dfs(v)

dfs((ch,cw))
print(ispos)
