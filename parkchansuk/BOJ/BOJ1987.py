# BOJ 1987. 알파벳
'''
세로 R칸, 가로 C칸으로 된 표 모양의 보드가 있다.
보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸 (1행 1열) 에는 말이 놓여 있다.

말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데,
새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다.
즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.

좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오.
말이 지나는 칸은 좌측 상단의 칸도 포함된다.

입력
첫째 줄에 R과 C가 빈칸을 사이에 두고 주어진다. (1 ≤ R,C ≤ 20) 둘째 줄부터
R개의 줄에 걸쳐서 보드에 적혀 있는 C개의 대문자 알파벳들이 빈칸 없이 주어진다.

출력
첫째 줄에 말이 지날 수 있는 최대의 칸 수를 출력한다.
'''
import sys
R, C = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().strip()) for _ in range(R)]

visited = [0]*26 # 알파벳 총 26개

def alph_idx(a): # 알파벳을 숫자로 변경해주는 함수 'ord('A')' 는 65이므로 65를 빼주면 visited 인덱스로 표현 가능
    idx = ord(a) - 65
    return idx

ans = 1

def dfs(i, j, length):
    global ans
    ans = max(ans, length)

    for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        ni, nj = i + di, j + dj
        if 0 <= ni < R and 0 <= nj < C:
            k = alph_idx(arr[ni][nj])
            if visited[k] == 0:
                visited[k] = 1        # 사용
                dfs(ni, nj, length + 1)
                visited[k] = 0       # 백트래킹

visited[alph_idx(arr[0][0])] = 1
dfs(0, 0, 1)
print(ans)

'''
DFS와 백트래킹 활용하여 문제 풀이
ord('A') = 65라는 점을 활용하여 인덱스로 사용함
'''