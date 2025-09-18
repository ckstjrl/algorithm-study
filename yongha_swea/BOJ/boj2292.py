target = int(input())

target_idx = target - 1

idx = 0

room = 1

room_val = 1

if room < target:
    for i in range(1, 1000000000):
        room += 1
        #이 부분이 풀이의 핵심이었는데 단순히 +6이 아닌 각 하나씩 중심에서 멀어질수록 배율이 된다
        room_val = room_val + (i * 6)
        #그리고 그렇게 늘어난 방의 수가 목표와 같거나 커지는 시점에서 멈추면 된다
        if room_val >= target:
            break