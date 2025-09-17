# 스위치 켜고 끄기
import sys
input = sys.stdin.readline


def turn_switch(num):
    if switch[num] == 1:
        switch[num] = 0
    else:
        switch[num] = 1


N = int(input())    # 스위치 개수
switch = list(map(int, input().split()))  # 스위치 상태 배열
M = int(input())    # 학생 수
student = [list(map(int, input().split())) for _ in range(M)]

for i in student:
    if i[0] == 1:   # 남학생인 경우
        for j in range(1, N+1):
            if j % i[1] == 0:
                turn_switch(j-1)
    elif i[0] == 2:   # 여학생인 경우
        if N - i[1] > i[1]:
            cnt = i[1]
        else:
            cnt = N - i[1] + 1
        turn_switch(i[1]-1)
        for j in range(1, cnt):
            if switch[i[1]-1-j] == switch[i[1]-1+j]:
                turn_switch(i[1]-j-1)
                turn_switch(i[1]+j-1)
            else:
                break
for i in switch:
    print(i)