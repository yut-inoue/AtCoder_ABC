n=int(input())

def func(cur,use):
    global res
    if cur>n:
        return
    if use==0b111:
        res+=1
    func(cur*10+7,use | 0b001)
    func(cur*10+5,use | 0b010)
    func(cur*10+3,use | 0b100)

res=0
func(0,0)
print(res)

