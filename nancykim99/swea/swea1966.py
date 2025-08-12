T = int(input()) # 테스트 케이스

# 카운트 정렬 사용
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    COUNTS = [0] * 51
    TEMP = [0] * N

    for i in range(N): # 각 [i]값들의 발생 횟수를 세고, 정수 항복들로 직접 인덱스 되는 COUNTS에 저장
        COUNTS[arr[i]] += 1
    for i in range(1, 51): # COUNTS의 원소 조정 : 숫자 1과 숫자 2를 저장, 숫자 2와 숫자 3을 저장...
        COUNTS[i] += COUNTS[i-1]
    for i in range(N-1, -1, -1): # 마지막 원소의 발생 횟수를 감소시키고, TEMP에 발생 횟수와 같은 인덱스에 삽입
        COUNTS[arr[i]] -= 1
        TEMP[COUNTS[arr[i]]] = str(arr[i])

    print(f'#{tc}',' '.join(TEMP))
