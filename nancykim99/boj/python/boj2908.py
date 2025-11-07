arr = list(map(int, input().split()))

f = []
for i in range(len(arr)):
    b = str(arr[i])
    a = list(b)
    d = []
    for j in range(2, -1, -1):
        c = a.pop(j)
        d.append(c)
    e = ''.join(d)
    f.append(int(e))

print(max(f))
