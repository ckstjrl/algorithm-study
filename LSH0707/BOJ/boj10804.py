arr = [i for i in range(21)]
def reverse(s, e):  # 시작, 끝 좌표 기준 뒤집기
    global arr
    x = arr[:s]
    y = arr[e:s-1:-1]
    z = arr[e+1:]
    arr = x + y + z
for _ in range(10):
    a, b = map(int, input().split())
    reverse(a, b)
print(*arr[1:])