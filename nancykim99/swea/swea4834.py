T = int(input()) # 테스트 케이스

for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int, input())) #여백이 없기 때문에, split이 필요 없음

    COUNTS = [0] * 101 # 100까지

    for i in range(N): # ai[i]의 발생 횟수 기록
        COUNTS[ai[i]] += 1

    a = 0
    for i in range(10):  # COUNTS의 가장 많은 카드의 장 수
        if a <= COUNTS[i]: # 가장 크거나 같은 경우 더하기 -> 가장 큰 수이자 많은 카드 숫자를 찾기 위해
            a = COUNTS[i]

    b = -1
    for i in range(10): # 인덱스를 통해 숫자 찾기
        if COUNTS[i] == a:
            b = i

    print(f'#{tc}', b, a)


# 카운팅 정렬의 모든 부분을 쓰는게 아니라 COUNTS의 발생 횟수만 찾는 부분만 사용해서 당황했었음
# 인덱스를 통해 값 찾는게 아직 안 익숙해서 익숙해져야겠음
# 가장 많은 카드의 장 수가 1일 때가 아니라 같을 때 어떻게 할지 고민해야할 듯
