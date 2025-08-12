# 1209. Sum D3
# 다음 100X100의 2차원 배열이 주어질 때, 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램을 작성하여라.
# 다음과 같은 5X5 배열에서 최댓값은 29이다.
# [제약 사항]
# 총 10개의 테스트 케이스가 주어진다.
# 배열의 크기는 100X100으로 동일하다.
# 각 행의 합은 integer 범위를 넘어가지 않는다.
# 동일한 최댓값이 있을 경우, 하나의 값만 출력한다.
# [입력]
# 각 테스트 케이스의 첫 줄에는 테스트 케이스 번호가 주어지고 그 다음 줄부터는 2차원 배열의 각 행 값이 주어진다.
# [출력]
# '#'부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 답을 출력한다.

T = 10

for tc in range(1, T+1):
    N = int(input()) # 각 테스트 케이스의 숫자
    arr = [list(map(int,input().split())) for _ in range(100)]

    max_v = []

    max_r = 0
    for i in range(100): # 최대 행의 합 찾기
        s = 0
        for j in range(100):
            s += arr[i][j]
        if max_r < s:
            max_r = s
    max_v += [max_r]

    max_c = 0
    for j in range(100): # 최대 열의 합 찾기
        s = 0
        for i in range(100):
            s += arr[i][j]
        if max_c < s:
            max_c = s
    max_v += [max_c]

    max_d = 0
    s = 0
    for i in range(100): # 최대 대각선의 합 찾기
        s += arr[i][i]
        if max_d < s:
            max_d = s
    max_v += [max_d]

    max_d_r = 0
    s = 0
    for i in range(100): # 최대 반대 대각선의 합 찾기
        s += arr[i][99-i]
        if max_d_r < s:
            max_d_r = s
    max_v += [max_d_r]

    # 최대합
    result = max_v[0]
    for i in range(len(max_v)):
        if result < max_v[i]:
            result = max_v[i]

    print(f'#{N}', result)

# 시행착오 1 : 거꾸로 갈때는 N-1-i -> 차이가 N-1만큼 나기 때문 => 거꾸로 갈때는 -i
# 시행착오 2 : 대각선은 이중for문이 아니기 때문에 s=0이 for문 밖에 나와있어야 한다!



