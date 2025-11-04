import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# x와 y만을 각각 추출하여 중복 없이(set) 집합 생성(집합 컴프리헨션) 후 정렬
xs = sorted({x for x, _ in arr})
ys = sorted({y for _, y in arr})

min_move = [float('inf')] * N

for ex in xs:
    # x 좌표의 차이를 담은 리스트
    dx = [abs(sx - ex) for sx, _ in arr] # 각 점과 ex와의 x좌표의 차 계산
    for ey in ys:
        tmp = [dx[i] + abs(arr[i][1] - ey) for i in range(N)]   # 고려중인 x와 주어진 y 좌표들의 이동 합을 리스트
        tmp.sort() # 오름차순 정렬 (이동이 적은 경우를 앞으로) e.g. sum(tmp[:num-1]) - num개의 체커가 한 칸에 모이는 이동

        s = 0
        for k in range(N):
            s += tmp[k]
            if s < min_move[k]:
                min_move[k] = s

print(*min_move)