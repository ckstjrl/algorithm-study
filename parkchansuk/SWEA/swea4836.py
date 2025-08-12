# 색칠하기 / D2
T = int(input())
arr = [[0]*10 for _ in range(10)]
for tc in range(1, T+1):
    N = int(input())
    red = [] # 빨간색 인덱스 값 모으기
    blue = [] # 파란색 인덱스 값 모으기
    for n in range(N):
        idx1_x, idx1_y, idx2_x, idx2_y, color = map(int, input().split())

        if color == 1:
            for i in range(idx1_x, idx2_x + 1):
                for j in range(idx1_y, idx2_y + 1):
                    red.append((i,j))   # 빨간색 인덱스 값을 튜플로 리스트에 추가
                                        # 튜플로 하는 이유는 리스트 중복 요소를 삭제하기 위해 set을 하는데
                                        # 리스트의 원소가 변환타입에러를 막기 위해 사용
        if color == 2:
            for i in range(idx1_x, idx2_x + 1):
                for j in range(idx1_y, idx2_y + 1):
                    blue.append((i,j)) # 파란색 인덱스 값을 튜플로 리스트에 추가

    red_ = list(set(red)) # 빨간색 인덱스 값 중 중복된 원소 삭제
    blue_ = list(set(blue)) # 파란색 인덱스 값 중 중복된 원소 삭제
    cnt = 0
    for s in range(len(red)):
        if red_[s] in blue_:
            cnt += 1

    print(f'#{tc} {cnt}')
