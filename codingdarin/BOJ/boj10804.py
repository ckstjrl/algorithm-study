# BOJ 10804. 카드 역배치 (D1 / B2)

# 1~20 카드 정배치
card_list = list(range(21))  # 0 패딩, 1~20 카드

# 입력 받고 각 줄 역배치 처리
for _ in range(10):
    s, e = map(int, input().split())
    
    # s~e 구간 역배치
    card_list[s:e+1] = card_list[s:e+1][::-1]

print(*card_list[1:])  # 0 패딩 제외 출력