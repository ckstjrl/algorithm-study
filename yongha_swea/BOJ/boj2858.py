# BOJ2858 기숙사 바닥

outer, inner = map(int, input().split())

# outer = 2(가로 + 세로) -4 -> 가로 + 세로 = (outer + 4) / 2
# inner = (가로 - 2) * (세로 - 2) -> 가로세로 -2(가로 + 세로) + 4 -> 가로세로 -2((outer + 4) / 2) + 4 ->
# 가로세로 = outer + inner

h_plus_w = (outer + 4) // 2

h_time_w = (outer + inner)

# 위 두 개 식을 통해서 이미 구하기 위한 준비는 다 된 상황
# 수를 하나씩 변경해가며 위 식 두개에 맞는 값을 구하는 방식으로 찾으면 된다.
# 다만, 항상 높이가 더 크게 나와야 하기 때문에 해당 조건을 부합하기 위한 if문 추가
for w in range(1, h_plus_w):
    h = h_plus_w - w

    if h * w == h_time_w:
        if h >= w:
            print(h, w)
            break
