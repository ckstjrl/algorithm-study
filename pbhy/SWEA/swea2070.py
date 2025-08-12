# 2070. 큰 놈, 작은 놈, 같은 놈

# 2수를 입력 받아 크기를 비교
## 등호 또는 부등호 출력

# 테스트 케이스 T
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    if N > M:
        result = '>'
    elif N == M:
        result = '='
    else:
        result = '<'

    print(f'#{tc} {result}')