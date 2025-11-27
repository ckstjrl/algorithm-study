# BOJ 9935. 문자열 폭발 / D3
'''
문제
상근이는 문자열에 폭발 문자열을 심어 놓았다. 폭발 문자열이 폭발하면 그 문자는 문자열에서 사라지며, 남은 문자열은 합쳐지게 된다.
폭발은 다음과 같은 과정으로 진행된다.
- 문자열이 폭발 문자열을 포함하고 있는 경우에, 모든 폭발 문자열이 폭발하게 된다.
  남은 문자열을 순서대로 이어 붙여 새로운 문자열을 만든다.
- 새로 생긴 문자열에 폭발 문자열이 포함되어 있을 수도 있다.
- 폭발은 폭발 문자열이 문자열에 없을 때까지 계속된다.
상근이는 모든 폭발이 끝난 후에 어떤 문자열이 남는지 구해보려고 한다. 남아있는 문자가 없는 경우가 있다. 이때는 "FRULA"를 출력한다.
폭발 문자열은 같은 문자를 두 개 이상 포함하지 않는다.

입력
첫째 줄에 문자열이 주어진다. 문자열의 길이는 1보다 크거나 같고, 1,000,000보다 작거나 같다.
둘째 줄에 폭발 문자열이 주어진다. 길이는 1보다 크거나 같고, 36보다 작거나 같다.
두 문자열은 모두 알파벳 소문자와 대문자, 숫자 0, 1, ..., 9로만 이루어져 있다.

출력
첫째 줄에 모든 폭발이 끝난 후 남은 문자열을 출력한다.
'''
import sys
input = sys.stdin.readline

s = input().strip()
bomb = input().strip()
m = len(bomb)
l = bomb[-1]
# 스텍 사용
stack = []

for i in s:
    stack.append(i)

    if i == l and len(stack) >= m:
        if ''.join(stack[-m:]) == bomb:
            del stack[-m:]

if stack:
    print(''.join(stack))
else:
    print('FRULA')

'''
메모리 초과
def poppop(string, bomb):
    if string:
        a = string.find(bomb)
        if a != -1:
            string_ = string[:a] + string[a+len(bomb):]
            return poppop(string_, bomb)

        else:
            return string
    else:
        return 'FRULA'

ans = poppop(s, bomb)
print(ans)
'''
'''
처음 문제 풀이
문자열에 폭발 문자열이 존재하면 슬라이싱을 통해 제거한 문자열을 제작하고 재귀
문자열에 폭발 문자열이 없으면 함수의 입력으로 받은 문자열 리턴
문자열이 없으면 'FRULA' 리턴
이러한 로직의 poppop 함수 제작

이 풀이는 답은 나오지만, find 함수 과정에서 과도한 메모리 소모

두번째 문제 풀이
스텍활용
폭발 문자열의 마지막 문자를 미리 l이라는 변수에 저장하고 시작
문자열을 하나씩 stack에 넣는 과정에서
들어가는 문자가 l과 동일한 경우 + stack의 길이가 폭발 문자열보다 길거나 같은 경우
stack에 있는 원소를 뒤에서 부터 폭발 문자열 길이만큼 뽑아서 폭발문자열과 비교
같은 경우 del진행
이걸 모든 문자가 stack에 들어올때까지 반복
이후 stack을 출력
'''