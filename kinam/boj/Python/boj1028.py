'''boj1028 - 다이아몬드 광산
다이아몬드 광산은 0과 1로 이루어진 R행*C열 크기의 배열이다.

다이아몬드는 1로 이루어진 정사각형의 경계선을 45도 회전시킨 모양이다. 크기가 1, 2, 3인 다이아몬드 모양은 다음과 같이 생겼다.

size 1:    size 2:    size 3:
                         1
              1         1 1
   1         1 1       1   1
              1         1 1
                         1
다이아몬드 광산에서 가장 큰 다이아몬드의 크기를 출력하는 프로그램을 작성하시오.

'''

# 완전 탐색 : R, C <= 750, 750^2 = 562500 / 시간 제한 0.75초
# 마름모 공식 |x| + |y| = r 이용하기?
# -> r = min(R, C) 부터 1씩 줄여나가면서 완전 탐색...?
# 다이아몬드 size = 3이면 다이아몬드의 중심에서 꼭짓점까지의 거리 자체는 2임
# r = size - 1 이런느낌


import sys
input = sys.stdin.readline

R, C = map(int, input().split())
diamonds = [list(map(int, list(input().strip()))) for _ in range(R)]
# print(diamonds)
def check_diamond(cr, cc, size):
    # |r - cr| + |c - cc| = size

    # 범위체크
    if cr - size < 0 or cr + size >= R or cc - size < 0 or cc + size >= C:
        return False
    
    for r in range(cr - size, cr + size + 1):
        for c in range(cc - size, cc + size + 1):
            if abs(r - cr) + abs(c - cc) == size:
                if diamonds[r][c] != 1: # diamonds값이 1이어야 다이아임
                    return False
            
    return True

ans = 0

radius = (min(R, C) // 2) + 1

for r in range(radius, 0, -1):
    found = False
    for cr in range(r - 1, R - r + 1):
        for cc in range(r - 1 , C - r + 1):
            if check_diamond(cr, cc, r - 1):
                ans = r
                found = True
                break
        if found:
            break
    if found:
        break

print(ans)


