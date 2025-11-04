C, R = map(int, input().split())
K = int(input())
cnt = 1  # 좌석번호 1부터
def seat(R, C, a):  # a = 0 (0,0) 시작좌표
    global cnt
    for i in range(R):  # i축 증가 방향
        if cnt == K:  # K번좌석이면 좌표값리턴
            print(a + 1, i + a + 1)
            return
        cnt = cnt + 1
    for j in range(1, C):  # j축 증가 방향
        if cnt == K:  # K번좌석이면 좌표값리턴
            print(j + a + 1, R + a)
            return
        cnt = cnt + 1
    for i in range(1, R):  # i축 감소 방향
        if cnt == K:  # K번좌석이면 좌표값리턴
            print(C + a, R - i + a)
            return
        cnt = cnt + 1
    for j in range(C - 2, 0, -1):  # j축 감소 방향
        if cnt == K:  # K번좌석이면 좌표값리턴
            print(j + a + 1, a + 1)
            return
        cnt = cnt + 1
    if R - 2 > 0 and C - 2 > 0:
        seat(R - 2, C - 2, a + 1)  # 한줄아래쪽 재귀-시작좌표(1,1), 가로세로길이-2

if K > C * R:  # 번호 > 최대좌석갯수 --> 0출력
    print(0)
else:
    seat(R, C, 0)