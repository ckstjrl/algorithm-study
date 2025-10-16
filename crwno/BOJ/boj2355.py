A, B = map(int, input().split())
x = abs(A - B) + 1
ans = (x * (x - 1)) // 2 + min(A, B) * x
print(ans)