
T = 10

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(8)]

    # 가로일 때 회문 구하기
    all_subset = []
    sub_set_n = 0
    for i in range(8):
        for j in range(8 -N +1): # 유효한 시작점만 사용
            sub_set = []
            for k in range(j, j+N):
                if (j+N) > 8:
                    break
                else:
                    sub_set += [arr[i][k]]
            sub_set_r = sub_set[::-1]
            if sub_set == sub_set_r:
                all_subset.append(sub_set)
                sub_set_n += 1
            else:
                continue

    for i in range(8 -N +1):
        for j in range(8):
            # 세로일때 회문 구하기
            sub_set = []
            for k in range(i, i+N):
                if (i+N) > 8:
                    continue
                else:
                    sub_set += [arr[k][j]]
            sub_set_r = sub_set[::-1]
            if sub_set == sub_set_r:
                all_subset.append(sub_set)
                sub_set_n += 1
            else:
                continue

    print(f'#{tc} {sub_set_n}')

# 새롭게 배운 것 : 그냥 얕은 복사해서 reverse해도 회문 확인이 가능

