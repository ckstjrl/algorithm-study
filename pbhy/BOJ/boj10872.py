# 10872. 팩토리얼
'''
0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

for문 돌려서 n부터 1까지 곱하자.
'''
n = int(input())
ans = 1
for i in range(1, n+1):
    ans *= i
print(ans)