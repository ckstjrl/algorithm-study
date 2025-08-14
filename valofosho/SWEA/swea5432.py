# 쇠막대기는 (     ) 멀어요
# 레이저는 () 인접
# () ((( () () ) (()) ())) (())
"""
하나씩 꺼내면서 괄호 체크
괄호가 바로 닫히면 레이저
괄호가 닫히지 않으면 + 1
괄호가 닫히지 않은 상태에서 레이저면 STOP 지금까지 +1만큼 한 번 더
닫힌 괄호가 또 나오면 + 1
로직 정리
"""
T = int(input())
for test_case in range(1, T+1):
    arr = list(input())
    cnt = 0
    total = 0
    for i in range(len(arr)-1):
        # 괄호가 열려 있고, 다음 괄호도 열린 괄호라면 cnt + 1
        if arr[i] == '(' and arr[i+1] == arr[i]:
            cnt += 1
        # 괄호가 열려 있지만 바로 닫힌다면 레이저
        # 레이저는 이전까지 담아둔 카운트를 전체 횟수에 더해준다
        elif arr[i] == '(' and arr[i+1] != arr[i]:
            total += cnt
        # 괄호가 닫혀있는데 다음 괄호도 닫힌다면 쇠막대기의 길이 끝
        # 전체에 하나를 더해주고, cnt에서는 하나를 빼준다.
        elif arr[i] == ')' and arr[i+1] == arr[i]:
            total += 1
            cnt -= 1
        else:
            pass
    print(f"#{test_case} {total}")

