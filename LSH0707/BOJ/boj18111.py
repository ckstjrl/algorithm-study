N, M, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
a = 0
for i in range(N):
    for j in range(M):
        a = a + arr[i][j]
max_h = (a + B) // (N * M)  # 사용할수있는블럭갯수 // 칸수 --> 높이의 최댓값
min_t = float('inf')  # 최소시간
height = 0  # 높이
def g(h):
    global min_t
    global height
    t = 0
    for i in range(N):
        for j in range(M):
            if t > min_t:  # 현재누적시간이 최소시간 넘으면 종료
                return
            if arr[i][j] >= h:  
                t = t + 2 * (arr[i][j] - h)
            else:
                t = t + h - arr[i][j]
    if t < min_t:  # 최소시간, 높이 갱신
        min_t = t
        height = h
for x in range(max_h, -1, -1):  # 높이의 최댓값부터 거꾸로 함수실행
    g(x)
print(min_t, height)