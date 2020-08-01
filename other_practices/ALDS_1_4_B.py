import bisect

n = int(input())
sl = list(map(int, input().split()))
q = int(input())
tl = list(map(int, input().split()))
count = 0


def binary_search(A, key):
    ind = bisect.bisect_left(A, key)
    if ind > len(A)-1:  # もしkeyが配列の最大値よりも大きいなら
        return "not found"
    elif A[ind] == key:
        return "found"
    else:
        return "not found"


for t in tl:
    if binary_search(sl, t) == 'found':
        count += 1

print(count)
