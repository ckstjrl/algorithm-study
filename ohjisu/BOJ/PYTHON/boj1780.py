'''
# [Silver II] 종이의 개수 - 1780

[문제 링크](https://www.acmicpc.net/problem/1780)

### 성능 요약

메모리: 163832 KB, 시간: 1056 ms

### 분류

분할 정복, 재귀

### 제출 일자

2025년 11월 5일 00:15:32

### 문제 설명

<p>N×N크기의 행렬로 표현되는 종이가 있다. 종이의 각 칸에는 -1, 0, 1 중 하나가 저장되어 있다. 우리는 이 행렬을 다음과 같은 규칙에 따라 적절한 크기로 자르려고 한다.</p>

<ol>
	<li>만약 종이가 모두 같은 수로 되어 있다면 이 종이를 그대로 사용한다.</li>
	<li>(1)이 아닌 경우에는 종이를 같은 크기의 종이 9개로 자르고, 각각의 잘린 종이에 대해서 (1)의 과정을 반복한다.</li>
</ol>

<p>이와 같이 종이를 잘랐을 때, -1로만 채워진 종이의 개수, 0으로만 채워진 종이의 개수, 1로만 채워진 종이의 개수를 구해내는 프로그램을 작성하시오.</p>

### 입력

 <p>첫째 줄에 N(1 ≤ N ≤ 3<sup>7</sup>, N은 3<sup>k</sup> 꼴)이 주어진다. 다음 N개의 줄에는 N개의 정수로 행렬이 주어진다.</p>

### 출력

 <p>첫째 줄에 -1로만 채워진 종이의 개수를, 둘째 줄에 0으로만 채워진 종이의 개수를, 셋째 줄에 1로만 채워진 종이의 개수를 출력한다.</p>

'''

# 설정
import sys
input = lambda :sys.stdin.readline().rstrip()

# 함수 + 초기설정
def solve(i, j, size):
    default = graph[i][j]
    for si in range(i, i + size):
        for sj in range(j, j + size):
            if not check(si, sj, default):
                new_size = size // 3
                # 1
                solve(i, j, new_size)
                solve(i, j + new_size, new_size)
                solve(i, j + 2 * new_size, new_size)
                # 2
                solve(i + new_size, j, new_size)
                solve(i + new_size, j + new_size, new_size)
                solve(i + new_size, j + 2 * new_size, new_size)
                # 3
                solve(i + 2 * new_size, j, new_size)
                solve(i + 2 * new_size, j + new_size, new_size)
                solve(i + 2 * new_size, j + 2 * new_size, new_size)
                return
    else:
        paper_dict[default] += 1
    return

def check(i, j, default):
    return default == graph[i][j]

paper_dict = {
    -1 : 0,
    0 : 0,
    1 : 0
}

# 인풋
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
# 함수호출
solve(0, 0, N)
# 출력
for i in paper_dict.values():
    print(i)