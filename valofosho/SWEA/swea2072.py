T = int(input())
for test_case in range(1, T+1):
    # 정수형으로 이루어진 리스트 입력받기
    arr = list(map(int, input().split()))
    # 홀수만을 더할 변수 초기값 설정
    cnt = 0
    # arr의 길이는 10으로 제한
    for i in range(10):
        # 2로 나눈 나머지가 0이 아니라면, 즉 홀수만 해당
        if arr[i] % 2 != 0:
            # 기존 설정한 변수에 홀수만을 더해준다.
            cnt += arr[i]
    # 문제의 출력 포맷에 맞춰 문자열로 형변환
    print('#'+str(test_case)+' '+str(cnt))