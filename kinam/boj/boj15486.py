'''boj15486 - 퇴사
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	512 MB	36828	15410	10937	40.298%
문제
상담원으로 일하고 있는 백준이는 퇴사를 하려고 한다.

오늘부터 N+1일째 되는 날 퇴사를 하기 위해서, 남은 N일 동안 최대한 많은 상담을 하려고 한다.

백준이는 비서에게 최대한 많은 상담을 잡으라고 부탁을 했고, 비서는 하루에 하나씩 서로 다른 사람의 상담을 잡아놓았다.

각각의 상담은 상담을 완료하는데 걸리는 기간 Ti와 상담을 했을 때 받을 수 있는 금액 Pi로 이루어져 있다.

N = 7인 경우에 다음과 같은 상담 일정표를 보자.

 	1일	2일	3일	4일	5일	6일	7일
Ti	3	5	1	1	2	4	2
Pi	10	20	10	20	15	40	200
1일에 잡혀있는 상담은 총 3일이 걸리며, 상담했을 때 받을 수 있는 금액은 10이다. 5일에 잡혀있는 상담은 총 2일이 걸리며, 받을 수 있는 금액은 15이다.

상담을 하는데 필요한 기간은 1일보다 클 수 있기 때문에, 모든 상담을 할 수는 없다. 예를 들어서 1일에 상담을 하게 되면, 2일, 3일에 있는 상담은 할 수 없게 된다. 2일에 있는 상담을 하게 되면, 3, 4, 5, 6일에 잡혀있는 상담은 할 수 없다.

또한, N+1일째에는 회사에 없기 때문에, 6, 7일에 있는 상담을 할 수 없다.

퇴사 전에 할 수 있는 상담의 최대 이익은 1일, 4일, 5일에 있는 상담을 하는 것이며, 이때의 이익은 10+20+15=45이다.

상담을 적절히 했을 때, 백준이가 얻을 수 있는 최대 수익을 구하는 프로그램을 작성하시오.
'''
# 조건 걸고 완전 탐색?
# 현재 날짜 + 상담 날짜 - 1 이 N보다 크면 안됨 
# ex) N = 7 일 때, 지금 6일인데 1일짜리 상담은 가능 2일짜리 상담은 불가
# 순회를 돌 때 상담에 걸리는 날짜 - 1 만큼 패스하고 그 이후 상담들을 고려

''' 시간초과남
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
N = int(input().strip())

counseling = [list(map(int, input().split())) for _ in range(N)]

max_profit = 0

def fix(day, current_profit):
    # 날짜 고정하기
    # 날짜 고정됐으면 수익 합 구하고 다음 날짜 구하기
    # 조건은 현재 날짜 + 상담 날짜 - 1 이 N보다 크면 안됨
	global max_profit 
	max_profit = max(max_profit, current_profit)

	for next_day in range(day, N):
		t, p = counseling[next_day]

		if next_day + t <= N:
			fix(next_day + t, current_profit + p)


fix(0, 0)

print(max_profit)
'''

# 이전날짜 계산정보로 다음날짜 계산 해볼만하니 dp 해보기

N = int(input().strip())

counseling = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (N + 1) #dp[i] : i일까지 벌 수 있는 최대 수익으로 가정

for i in range(N):
	time, profit = counseling[i]
    
	# 상담 안하는 경우
	dp[i + 1] = max(dp[i + 1], dp[i])

	# 상담하는 경우
	if i + time <= N:
		dp[i + time] = max(dp[i + time], dp[i] + profit)
	
	

print(dp[N])