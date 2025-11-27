"""
[문제]
눈금의 간격이 1인 M×N(M,N≤100)크기의 모눈종이가 있다. 
이 모눈종이 위에 눈금에 맞추어 K개의 직사각형을 그릴 때, 이들 K개의 직사각형의 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어진다.

M, N과 K 그리고 K개의 직사각형의 좌표가 주어질 때, K개의 직사각형 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어지는지, 
그리고 분리된 각 영역의 넓이가 얼마인지를 구하여 이를 출력하는 프로그램을 작성하시오.

[입력]
첫째 줄에 M과 N, 그리고 K가 빈칸을 사이에 두고 차례로 주어진다. M, N, K는 모두 100 이하의 자연수이다. 
둘째 줄부터 K개의 줄에는 한 줄에 하나씩 직사각형의 왼쪽 아래 꼭짓점의 x, y좌표값과 
오른쪽 위 꼭짓점의 x, y좌표값이 빈칸을 사이에 두고 차례로 주어진다. 
모눈종이의 왼쪽 아래 꼭짓점의 좌표는 (0,0)이고, 오른쪽 위 꼭짓점의 좌표는(N,M)이다. 
입력되는 K개의 직사각형들이 모눈종이 전체를 채우는 경우는 없다.

[출력]
첫째 줄에 분리되어 나누어지는 영역의 개수를 출력한다. 둘째 줄에는 각 영역의 넓이를 오름차순으로 정렬하여 빈칸을 사이에 두고 출력한다.
"""
import sys
input = sys.stdin.readline

M, N, K = map(int, input().split())
grid = [[0]*N for _ in range(M)]
visitd = [[False]*N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(y1, y2):
        for i in range(x1, x2):
            grid[j][i] = 1

cnt = 0
space_list = []
dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def find_ans(j, i):
    stack = [(j, i)]
    visitd[j][i] = True
    space = 1

    while stack:
        cj, ci = stack.pop()
        for dj, di in dirs:
            nj, ni = cj+dj, ci+di
            if 0 <= nj < M and 0 <= ni < N:
                if grid[nj][ni] == 0 and not visitd[nj][ni]:
                    visitd[nj][ni] = True
                    stack.append((nj, ni))
                    space += 1
    return space

for j in range(M):
    for i in range(N):
        if grid[j][i] == 0 and not visitd[j][i]:
            cnt += 1
            space_list.append(find_ans(j, i))

space_list = sorted(space_list)
print(cnt)
print(*space_list)