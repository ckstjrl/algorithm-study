# BOJ10804 카드 역배치

deck = [0] * 20

#카드 덱 받기, 1-20
for i in range(20):
    deck[i] = i + 1

#카드 순서 변경 구간
for _ in range(10):
    start, end = map(int, input().split())

    # index
    start = start - 1
    end = end - 1

    for i in range((end - start + 1) // 2):
        # 첫과 끝, 첫에서 2번째 끝에서 2번째 방식으로 서로 카드를 스왑해준다, 이때 스왑 횟수는 전체 교환 카드의 절반 횟수 (//2)
        deck[start + i], deck[end - i] = deck[end - i], deck[start + i]
    
print(*deck)
