# BOJ 9012. 괄호 / D2
'''
괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열이다.
그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다.
한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS 이라고 부른다.
만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은 새로운 문자열 “(x)”도 VPS 가 된다.
그리고 두 VPS x 와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS 가 된다.
예를 들어 “(())()”와 “((()))” 는 VPS 이지만 “(()(”, “(())()))” ,
그리고 “(()” 는 모두 VPS 가 아닌 문자열이다.

여러분은 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다.
'''
import sys
T = int(sys.stdin.readline())
for _ in range(T):
    arr = list(map(str, sys.stdin.readline()))
    N = len(arr)

    stk = []
    ans = 'YES'
    for i in range(N):
        if arr[i] == '(':
            stk.append(arr[i])

        elif arr[i] == ')':
            if stk:
                if stk[-1] == '(':
                    stk.pop()
                else:
                    ans = 'NO'
            else:
                ans = 'NO'

    if stk:
        ans = 'NO'

    print(ans)

'''
자주 풀어봤던 유형으로 stack을 사용하여 괄호 짝 찾기 진행
ans를 처음엔 YES로 설정하고 틀린 경우가 존재할 때 NO로 변경하는 방식을 활용하여 풀이
'''