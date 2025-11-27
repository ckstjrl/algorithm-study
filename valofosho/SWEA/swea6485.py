T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [0] * 5001
    for i in range(N):
        start, stop = map(int, input().split())
        # 시작 정류장과 끝 정류장까지 들림 표시
        for j in range(start, stop+1):
            arr[j] += 1
    P = int(input())
    new_arr = []
    for i in range(P):
        # 들어온 입력값을 인덱스로 하는 값 추가
        new_arr.append(str(arr[int(input())]))
    ans = ' '.join(new_arr)
    print(f"#{test_case} {ans}")
