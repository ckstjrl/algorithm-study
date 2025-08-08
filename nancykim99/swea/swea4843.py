# 4843. 특별한 정렬 D3
# 보통의 정렬은 오름차순이나 내림차순으로 이루어지지만, 이번에는 특별한 정렬을 하려고 한다.
# N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 큰 수와 작은 수를 번갈아 정렬하는 방법이다.
# 예를 들어 1부터 10까지 10개의 숫자가 주어지면 다음과 같이 정렬한다.
# 10 1 9 2 8 3 7 4 6 5
# 주어진 숫자에 대해 특별한 정렬을 한 결과를 10개까지 출력하시오
# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
# 다음 줄에 정수의 개수 N이 주어지고 다음 줄에 N개의 정수 ai가 주어진다. 10<=N<=100, 1<=ai<=100
# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 특별히 정렬된 숫자를 10개까지 출력한다.



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 변형된 선택 정렬
    for i in range(10):  # 구간의 맨 앞
        if i % 2 == 0:  # 짝수인 경우 내림차순(구간의 최댓값)
            max_idx = i
            for j in range(i + 1, N):
                if arr[max_idx] < arr[j]:
                    max_idx = j
            arr[i], arr[max_idx] = arr[max_idx], arr[i]
        else:  # 오름차순(최솟값)
            min_idx = i
            for j in range(i + 1, N):
                if arr[min_idx] > arr[j]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print(f'#{tc}', *arr[:10])