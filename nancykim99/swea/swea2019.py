N = int(input())

a = 1
arr = ['1']
for _ in range(N):
    a *= 2
    arr.append(str(a))

print(' '.join(arr))