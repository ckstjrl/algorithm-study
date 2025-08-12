"""
1954. 달팽이 숫자
"""

def make_snail_arr(size, start=1):

    # 원소가 모두 0으로 초기화된 size * size 배열을 생성한다.
    snail_arr = [[0] * size for _ in range(size)]

    # 종료 조건 : size == 1 이면 그대로 반환
    if size == 1:
        return [[start]]

    # 바깥쪽 테두리 채우기
    num = start

    # 상단 테두리 채우기
    for i in range(size):       # 0, 1, ... , size - 1(size개)만큼 왼쪽에서 오른쪽으로
        snail_arr[0][i] = num   # 상단 테두리에 num을 1씩 누적하며 배열한다.
        num += 1
    # 우측 테두리 채우기
    for i in range(1, size):            # 1, 2, ... , size - 1((size - 1)개)만큼 위쪽에서 아래쪽으로
        snail_arr[i][size - 1] = num    # 우측 테두리에 num을 1씩 누적하며 배열한다.
        num += 1
    # 하단 테두리 채우기
    for i in range(size - 2, -1, -1):   # size - 2, size - 1, ... , 1, 0((size - 1)개)만큼 오른쪽에서 왼쪽으로
        snail_arr[size - 1][i] = num    # 아래 테두리에 num을 1씩 누적하며 배열한다.
        num += 1
    # 좌측 테두리 채우기
    for i in range(size - 2, 0, -1):    # size - 2, size - 1, ... , 1 ((size - 2)개)만큼 아래쪽에서 위쪽으로
        snail_arr[i][0] = num           # 왼쪽 테두리에 num을 1씩 누적하며 배열한다.
        num += 1

    # 내부 재귀 호출 (중심 기준으로 size-2 배열)
    if size > 2:

        inner = make_snail_arr(size - 2, num) # 내부 달팽이 배열은 size-2 크기 배열을 num부터 start한 모양과 같다!
        for i in range(size - 2):
            for j in range(size - 2):
                snail_arr[i + 1][j + 1] = inner[i][j] # inner를 테두리 내부 배열에 복사한다.

    return snail_arr # 완성된 달팽이 배열을 반환한다.

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    snail = make_snail_arr(N)

    print(f'#{test_case}')
    for row in snail:
        print(' '.join(map(str, row)))
