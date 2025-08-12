"""
2001. 파리 퇴치
"""

# 테스트 케이스의 수 입력
T = int(input())

# 각 테스트 케이스에 대해 반복
for test_case in range(1, T + 1):

    # 배열의 크기 N과 파리채의 크기 M 입력
    N, M = map(int, input().split())

    # N x N 배열 입력 받기 (파리 개수 정보)
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 죽인 파리의 최대 수를 저장할 변수
    max_sum = 0

    # 파리채가 내릴 수 있는 모든 위치에 대해 반복
    # i는 시작 행, j는 시작 열
    for i in range(N - M + 1):
        for j in range(N - M + 1):

            # 현재 파리채가 덮는 M x M 영역의 파리 수를 저장할 변수
            sum = 0

            # M x M 영역의 모든 칸을 더함
            for k in range(M):
                for l in range(M):
                    sum += arr[i + k][j + l]

                    # 매번 비교하며 최댓값 갱신
                    if sum > max_sum:
                        max_sum = sum

    # 결과 출력
    print(f'#{test_case} {max_sum}')
    