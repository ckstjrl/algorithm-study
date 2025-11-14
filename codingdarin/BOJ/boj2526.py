# BOJ 2526. 싸이클 (D1 / B1)

n, p = map(int, input().split())

arr = [n]
first = n

while True:
    second = (first * n) % p
    if second in arr:
        # 사이클 시작 지점 찾기
        cycle_start = arr.index(second)
        print(len(arr) - cycle_start)
        break
    arr.append(second)
    first = second