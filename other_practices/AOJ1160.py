import sys
sys.setrecursionlimit(10 ** 7)
def movePos(i, j, w, h):
    res = []
    for difi in [-1, 0, 1]:
        if i+difi > h-1 or i+difi < 0:
            continue
        for difj in [-1, 0, 1]:
            if difi == 0 and difj == 0:
                continue
            if j+difj > w-1 or j+difj < 0:
                continue
            res.append((i+difi, j+difj))
    return res

def reduction(tup,w,h):
    i,j=tup
    return i*w + j+1


def dfs(u, color_id):
    global color
    color[u] = color_id
    for v in adjl[u]:
        if color[v] == NIL:  # 未到達なら再起呼び出し
            color[v] = color_id
            dfs(v, color_id)


def solve(adjl,groundl):
    global color
    color_id = 0
    for u in range(1,h*w+1):
        if color[u] == NIL:
            color_id += 1
            dfs(u, color_id)
    dic={}
    for v in groundl:
        dic[color[v]]=1
    print(len(dic))



while True:
    w,h=map(int,input().split())
    if w==0 and h==0:
        break
    c=[list(map(int, input().split())) for i in range(h)]
    adjl=[[] for _ in range(h*w+1)]
    groundl=[]
    NIL = -1
    color = [NIL for i in range(h*w+1)]
    for i in range(h):
        for j in range(w):
            if c[i][j] == 0:
                continue
            groundl.append(reduction((i,j),w,h))
            move=movePos(i,j,w,h)
            for tup in move:
                if c[tup[0]][tup[1]] == 1:
                    adjl[reduction((i,j),w,h)].append(reduction(tup,w,h))

    for i, l1d in enumerate(adjl):
        adjl[i]=list(set(l1d))
    solve(adjl,groundl)
