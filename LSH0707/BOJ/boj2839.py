N = int(input())
ans = -1
if N % 5 == 0:  # N을 5로나눈 나머지가 0 1 2 3 4 인 경우로 나누고 각 경우에 3으로 나눠떨어지는 
                # 가장 작은 수를 빼고 (5로나눈 몫 + 3으로 나눈 몫) 출력
    ans = N // 5
elif N % 5 == 1 and N >= 6:
    ans = (N - 6) // 5 + 2
elif N % 5 == 2 and N >= 12:
    ans = (N - 12) // 5 + 4
elif N % 5 == 3 and N >= 3:
    ans = (N - 3) // 5 + 1
elif N % 5 == 4 and N >= 9:
    ans = (N - 9) // 5 + 3
print(ans)