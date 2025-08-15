for test_case in range(1,11):
    N = int(input())
    arr = list(map(int, input().split()))
    max_h = max(arr)
    min_h = min(arr)
    is_equated = False # 최고, 최저 비교를 위한 불린형 변수 선언
    for i in range(N):
        # 최고와 최저점이 동일해지면 break
        if max_h == min_h:
            is_equated = True
            break
        # 그렇지 않으면 dump 실행
        else:
            arr[arr.index(max_h)] -= 1
            arr[arr.index(min_h)] += 1
        max_h = max(arr)
        min_h = min(arr)
    if is_equated:
       print(f"#{test_case} {max_h}")
    else:
        print(f"#{test_case} {max_h-min_h}")