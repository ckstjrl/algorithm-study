'''
# [Gold IV] 알파벳 - 1987

[문제 링크](https://www.acmicpc.net/problem/1987)

### 성능 요약

메모리: 191888 KB, 시간: 6204 ms

### 분류

그래프 이론, 그래프 탐색, 깊이 우선 탐색, 백트래킹, 격자 그래프

### 제출 일자

2025년 9월 19일 00:43:59

### 문제 설명

<p>세로 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D445 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$R$</span></mjx-container>칸, 가로 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D436 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$C$</span></mjx-container>칸으로 된 표 모양의 보드가 있다. 보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸 (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1$</span></mjx-container>행 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1$</span></mjx-container>열) 에는 말이 놓여 있다.</p>

<p>말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데, 새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다. 즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.</p>

<p>좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오. 말이 지나는 칸은 좌측 상단의 칸도 포함된다.</p>

### 입력

 <p>첫째 줄에 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D445 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$R$</span></mjx-container>과 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D436 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$C$</span></mjx-container>가 빈칸을 사이에 두고 주어진다. (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D445 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D436 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>R</mi><mo>,</mo><mi>C</mi><mo>≤</mo><mn>20</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 ≤ R,C ≤ 20$</span></mjx-container>) 둘째 줄부터 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D445 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>R</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$R$</span></mjx-container>개의 줄에 걸쳐서 보드에 적혀 있는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D436 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>C</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$C$</span></mjx-container>개의 대문자 알파벳들이 빈칸 없이 주어진다.</p>

### 출력

 <p>첫째 줄에 말이 지날 수 있는 최대의 칸 수를 출력한다.</p>

'''
'''
처음 (set 사용 + PyPy3): 짐(연산)이 너무 많아 시간 초과
list 대비 set 연산 자체가 많아서 시간 초과

두번째 (list 사용 + PyPy3): 트럭이 짐(최적화된 코드)을 싣고 너무 빨리 달린 나머지,
기름(메모리)이 먼저 바닥나 버린 메모리 초과

세번째 (list 사용 + Python 3): 연산도 적고, 연비가 좋은 Python 3를 사용
했지만 시간 초과
--> 원인은? 재귀의 깊이를 10**6 로 설정해서 과도한 메모리를 요청한 것
-->       sys.setrecursionlimit(1000)으로 변경해서 통과함
'''

'''
1트: set 사용 버전
'''
import sys
sys.setrecursionlimit(1000)
input = lambda: sys.stdin.readline().rstrip()

dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def dfs(now_dist, i, j) :
    global max_dist
    max_dist = max(max_dist, now_dist)
    for di, dj in dirs :
        ni, nj = i + di, j + dj
        if not (0 <= ni < R and 0 <= nj < C) or graph[ni][nj] in visited : # 범위 체크
            continue
        visited.add(graph[ni][nj]) # 방문 표시
        dfs(now_dist + 1, ni, nj)  # 재귀 호출
        visited.remove(graph[ni][nj]) # 방문 취소

R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]
visited = set(graph[0][0]) # 시작 지점을 넣고 시작
max_dist = 1               # 그래서 거리도 1
dfs(now_dist=1, i=0, j=0)  # 함수 호출
print(max_dist)


'''
2트: ord()를 사용해 유니코드의 차를 idx로 사용하는 list 활용 버전
'''
import sys
sys.setrecursionlimit(1000)
input = lambda: sys.stdin.readline().rstrip()

dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def dfs(now_dist, i, j) :
    global max_dist
    max_dist = max(max_dist, now_dist)
    for di, dj in dirs :
        ni, nj = i + di, j + dj

        if not (0 <= ni < R and 0 <= nj < C) : # 범위 체크
            continue
        next_idx = ord(graph[ni][nj]) - ord('A') # 알파벳을 숫자로 변환해서 idx로 사용
        if visited[next_idx] : # 방문 체크
            continue
        visited[next_idx] = True  # 방문 표시
        dfs(now_dist + 1, ni, nj) # 재귀 호출
        visited[next_idx] = False # 방문 취소


R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]

visited = [False] * 26 # set 대신 26칸짜리 리스트 사용 (알파벳 26자)
visited[ord(graph[0][0]) - ord('A')] = True # 출발지점 방문 체크
max_dist = 1               # 그래서 거리도 1

dfs(now_dist=1, i=0, j=0)  # 함수 호출
print(max_dist)
