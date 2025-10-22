'''
BOJ15486 / D3): 퇴사 2

해결 방법 :
고려해야 하는 부분 : N+1일에는 근무를 안 함 : (N - i) + T > N -> 어차피 일을 하지 못하니 skip
하루씩 순회하면서, 전날까지 번 돈과 그날까지 번 돈 중에 더 큰 값을 저장하기 (아직 그날 수익을 추가한건 아니라서, 그냥 전날 수익 일단 갱신)
돈을 받는 날을 확인하면서, 돈을 받는 날이 N+1을 벗어나지 않는 경우에만, 그날 수익을 추가해서 그날 번 돈으로 저장
모든 수익을 고려한 최댓값 == 답
'''

N = int(input()) # 근무하는 총 날짜
work = [(0, 0)]

for _ in range(1, N+1):
    T, P = map(int, input().split())
    work.append((T, P))

earned = [0] * (N+2)
for i in range(1, N+1):
    time, profit = work[i]
    earned[i] = max(earned[i], earned[i-1])
    pay_day = i + time
    if pay_day <= N + 1:
        earned[pay_day] = max(earned[pay_day], earned[i] + profit)

print(max(earned)) 