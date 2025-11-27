T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]   # N * N 리스트 만들기
    # 만든 리스트에 입력값 넣기
    for i in range(N):
        arr[i] = list(map(int, input()))
    # 총 이익 0 초기화
    profit = 0
    # 중간값 계산
    middle_num = N // 2 + 1
    # 0번부터 중간값까지 좌우 1칸씩 늘려가며 이익에 더하고,
    # 마지막부터 중간값 전까지 좌우 1칸씩 늘려가며 이익에 더하기
    for i in range(middle_num):
        profit += sum(arr[i][middle_num - 1 - i : middle_num + i])
    for i in range(N - 1, middle_num - 1, -1):
        profit += sum(arr[i][middle_num - 1 - (N - i - 1) : middle_num + (N - i - 1)])
    # 출력
    print(f'#{tc} {profit}')