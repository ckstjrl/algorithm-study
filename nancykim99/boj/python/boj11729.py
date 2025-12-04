'''
BOJ11729 : 하노이 탑 이동 순서 (G5)

해결 방법 : 
거꾸로 푼다고 생각하면 쉬움
재귀로 돌면서, 맨 위 반, 중간, 맨 아래 반 이렇게 진행 순서를 나눠서 재귀
'''

n = int(input())
moved = []

def reversed_move(n, s, e, h):
    if n == 0:
        return 
    reversed_move(n-1, s, h, e)
    moved.append((s, e))
    reversed_move(n-1, h, e, s)

reversed_move(n, 1, 3, 2)

ans = len(moved)
print(ans)

for i in range(ans):
    print(*moved[i])