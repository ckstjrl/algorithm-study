import sys
input = sys.stdin.readline

# 뒤집는 위치(인덱스), 해당 위치의 리스트는 뒤집혀지는 비트 (0번 인덱스는 더미데이터)
# 보드 위치    비트
#  1 2 3     9 8 7
#  4 5 6     6 5 4
#  7 8 9     3 2 1(LSB)
mask = [[], [9, 8, 6], [9, 8, 7, 5], [8, 7, 4], [9, 6, 5, 3], [8, 6, 5, 4, 2],
        [7, 5, 4, 1], [6, 3, 2], [5, 3, 2, 1], [4, 2, 1]]

# 각 칸이 눌린 후의 상태를 XOR로 사전 계산
mask_switch = [0] * 10
for i in range(1, 10):
    tmp = 0
    for j in mask[i]:
        tmp ^= (1 << (j-1))
    mask_switch[i] = tmp


T = int(input())
for _ in range(T):
    board = 0
    for _ in range(3):
        row = input().strip()
        for x in row:
            board <<= 1 # 비트 시프팅, LSB에 0 추가
            if x == '.': # 흰 색인 경우 LSB 1로 변경
                board |= 1

    ans = 10 # 최댓값 (칸이 3x3이므로 10이상은 나올 수 없음)
    for state in range(1, 1 << 9): # 스위치를 누르는 모든 패턴 (0b000000000 ~ 0b111111111)
        start = 0b111111111 # 초기 상태
        cnt = 0

        for i in range(9): # 각 스위치 실행(패턴에서 스위치가 어디에 켜져있는지 확인하기 위한 반복문)
            if state & (1 << i): # 해당 위치의 칸을 눌러야 할 경우 AND 연산을 하면 1이 되므로
                start ^= mask_switch[i+1] # 해당 마스크와 시작 비트 XOR 연산
                cnt += 1
            if ans < cnt: # 구하려는 답보다 커지는 경우
                break
            if start == board: # 시작과 주어진 보드가 일치하는 경우
                ans = cnt

    print(ans)

"""
첫 시도는 조합을 사용하여 해결하려했다.
답은 나오지만 런타임에러.......

아래는 조합을 사용한 코드
import sys
input = sys.stdin.readline
from itertools import combinations

mask = [[], [9, 8, 6], [9, 8, 7, 5], [8, 7, 4], [9, 6, 5, 3], [8, 6, 5, 4, 2],
        [7, 5, 4, 1], [6, 3, 2], [5, 3, 2, 1], [4, 2, 1]]


def bit_masking(choice, bit):
    for i in mask[choice]:
        if (bit >> (i-1)) & 1:
            bit -= 1 << (i-1)
        else:
            bit += 1 << (i-1)
    return bit


def comb(n):
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = list(combinations(nums, n)) # 조합의 결과를 담은 리스트
    return result


def check(choice, n):
    for i in range(len(choice)):
        start = 0b111111111
        for j in range(n):
            start = bit_masking(choice[i][j], start)
        if start == board:
            return True
    return False


T = int(input())
for _ in range(T):
    board = 0
    for _ in range(3):
        row = input().strip()
        for x in row:
            board <<= 1
            if x == '.': # 흰 색: 1
                board |= 1

    ans = 10
    for i in range(1, 10):
        choice = comb(i)
        if check(choice, i):
            cnt = i
            if ans < cnt:
                break
    print(ans)
"""