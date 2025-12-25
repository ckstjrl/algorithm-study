import sys
sys.setrecursionlimit(10 ** 6)

N, K = map(int, input().split())
arr = list(map(int, input().strip()))
ans = []

def find_max(i, k):
    if i == N:  # 모든 숫자 확인했으면 종료
        return
    num = arr[i]  # 현재 확인하고있는 숫자
    while ans and k > 0 and ans[-1] < num:
        # ans의 마지막 숫자가 현재 숫자보다 작고 제거횟수가 남은 경우 pop하고 제거횟수-1
        ans.pop()
        k = k - 1
    ans.append(num)  # 현재 숫자 append
    find_max(i + 1, k)  # find_max(다음숫자확인, 남은제거횟수)

find_max(0, K)
print(''.join(map(str, ans[:N - K])))  # 필요한 자릿수만큼 출력
