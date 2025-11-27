# 2675. 문자열 반복
'''
문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오.
첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다.

T : 테스트 케이스 개수
R : 반복 횟수
S : 문자열
문자열 S의 길이만큼 돌면서 R을 곱한다.
'''
t = int(input())
for tc in range(1, t+1):
    r, s = input().split()
    r = int(r)
    for i in range(len(s)):
        print(r*s[i], end='')
    print()
