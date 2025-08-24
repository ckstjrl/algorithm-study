"""
N개의 숫자로 이루어진 수열
맨앞의 숫자를 맨 뒤로 보내는 작업 M번
수열의 맨 앞에 있는 숫자 출력
"""
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    print(f"#{test_case} {arr[M%N]}")