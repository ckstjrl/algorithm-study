import sys
input = sys.stdin.readline
find = []
while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    else:
        find.append((a, b, c))
arr = [[[0] * 21 for _ in range(21)] for _ in range(21)]  # a,b,c(0~21)배열
def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if arr[a][b][c] != 0:  # 배열에 저장된 값이면 리턴
        return arr[a][b][c]
    if a < b and b < c:  # 배열에 값 저장
        arr[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
    else:
        arr[a][b][c] = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)
    return arr[a][b][c]
for i in range(len(find)):
    a, b, c = find[i]
    print(f'w({a}, {b}, {c}) = {w(a,b,c)}')