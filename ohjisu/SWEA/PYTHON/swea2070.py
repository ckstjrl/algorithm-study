"""
2070. 큰 놈, 작은 놈, 같은 놈 D1

2개의 수를 입력 받아 크기를 비교하여 등호 또는 부등호를 출력하는 프로그램을 작성하라.
"""

T = int(input())
for test_case in range(1, T+1) :
    N, M = list(map(int, input().split()))
    # 삼항연산자 [연산] if [condition] else [연산] if [condition] else [연산] 
    print(f"#{test_case} {'>' if N > M else'<' if N < M else '='}")