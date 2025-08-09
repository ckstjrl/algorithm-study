# 2001. 파리 퇴치 D2
# N x N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개수를 의미한다.
# 아래는 N=5 의 예이다.
# M x M 크기의 파리채를 한 번 내리쳐 최대한 많은 파리를 죽이고자 한다.
# 죽은 파리의 개수를 구하라!
# 예를 들어 M=2 일 경우 위 예제의 정답은 49마리가 된다.
# [제약 사항]
# 1. N 은 5 이상 15 이하이다.
# 2. M은 2 이상 N 이하이다.
# 3. 각 영역의 파리 갯수는 30 이하 이다.
#
# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에 N 과 M 이 주어지고,
# 다음 N 줄에 걸쳐 N x N 배열이 주어진다.
#
# [출력]
# 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 최대 파리 M*M 구하기
    sum_list = []
    sum_n = 0
    for i in range(0, N-M+1):
        for j in range(0, N-M+1):
            sum = 0
            for p in range(i, i+M):
                for q in range(j, j+M):
                    sum += arr[p][q]
            sum_list += [sum]
            sum_n += 1

    # 최대 파리 값 구하기
    max_fly = sum_list[0]
    for i in range(sum_n):
        if max_fly < sum_list[i]:
            max_fly = sum_list[i]

    print(f'#{tc}', max_fly)

# 해결 방법 : N*N에서 최댓값의 M*M을 찾아야 한다
#     M*M을 N*N에서 하나씩 순회하면서 찾아보자.
#     2차원에서 부분 배열을 순회할 때
#     for i: 0 -> n - 3  # 부분배열 기준 i,j
#         for j: 0 -> m - 4
#             for p: i -> i + 2
#                 for q: j -> j + 3
#                     arr[p][q]
# 시행착오 1 : N-M+1을 해야 인덱싱으로 내가 원하는 값까지 가는데, N-M을 해서 답이 안 나옴