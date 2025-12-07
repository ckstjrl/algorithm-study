# boj1992(D2): 쿼드트리
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())  # n: 영상크기
video = [list(input().strip()) for _ in range(n)]
result = []

# Quad Tree 압축 함수
def quad_tree(x, y, size):
    global result
    check_bw = video[x][y]  # 첫 색이 흰/검인지 확인
    for i in range(x, x + size):
        for j in range(y, y + size):
            if video[i][j] != check_bw:
                result.append('(')
                half = size // 2

                quad_tree(x, y, half)  # 좌상단
                quad_tree(x, y + half, half)  # 우상단
                quad_tree(x + half, y, half)  # 좌하단
                quad_tree(x + half, y + half, half)  # 우하단

                result.append(')')
                return

    if check_bw == '0':
        result += '0'
    else:
        result += '1'

quad_tree(0, 0, n)
print(''.join(result))