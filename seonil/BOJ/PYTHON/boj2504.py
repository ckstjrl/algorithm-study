"""
BOJ2504. 괄호의 값

[문제]
4개의 기호 ‘(’, ‘)’, ‘[’, ‘]’를 이용해서 만들어지는 괄호열 중에서 올바른 괄호열이란 다음과 같이 정의된다.

1. 한 쌍의 괄호로만 이루어진 ‘()’와 ‘[]’는 올바른 괄호열이다.
2. 만일 X가 올바른 괄호열이면 ‘(X)’이나 ‘[X]’도 모두 올바른 괄호열이 된다.
3. X와 Y 모두 올바른 괄호열이라면 이들을 결합한 XY도 올바른 괄호열이 된다.
예를 들어 ‘(()[[]])’나 ‘(())[][]’ 는 올바른 괄호열이지만 ‘([)]’ 나 ‘(()()[]’ 은 모두 올바른 괄호열이 아니다. 우리는 어떤 올바른 괄호열 X에 대하여 그 괄호열의 값(괄호값)을 아래와 같이 정의하고 값(X)로 표시한다.

1. ‘()’ 인 괄호열의 값은 2이다.
2. ‘[]’ 인 괄호열의 값은 3이다.
3. ‘(X)’ 의 괄호값은 2×값(X) 으로 계산된다.
4. ‘[X]’ 의 괄호값은 3×값(X) 으로 계산된다.
5. 올바른 괄호열 X와 Y가 결합된 XY의 괄호값은 값(XY)= 값(X)+값(Y) 로 계산된다.
예를 들어 ‘(()[[]])([])’ 의 괄호값을 구해보자. ‘()[[]]’ 의 괄호값이 2 + 3×3=11 이므로 ‘(()[[]])’의 괄호값은 2×11=22 이다. 그리고 ‘([])’의 값은 2×3=6 이므로 전체 괄호열의 값은 22 + 6 = 28 이다.

여러분이 풀어야 할 문제는 주어진 괄호열을 읽고 그 괄호값을 앞에서 정의한대로 계산하여 출력하는 것이다.

[입력]
첫째 줄에 괄호열을 나타내는 문자열(스트링)이 주어진다. 단 그 길이는 1 이상, 30 이하이다.

[출력]
첫째 줄에 그 괄호열의 값을 나타내는 정수를 출력한다. 만일 입력이 올바르지 못한 괄호열이면 반드시 0을 출력해야 한다.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

# 닫는 괄호 → 여는 괄호 매핑
mapping = {
    ')': '(',
    ']': '[',
}

# 괄호열의 값을 계산하는 함수
def cal_parentheses_value(input_str):

    stack = []

    # 괄호열의 앞부터 차례대로 검사
    for ch in input_str:

        # 여는 괄호이면 스택에 push
        if ch in mapping.values():
            stack.append(ch)
        
        # 닫는 괄호이면
        elif ch in mapping.keys():

            # 스택이 비어 있으면 올바르지 않은 괄호열임
            if not stack:
                return 0
            
            # 스택이 비어 있지 않으면 괄호값 계산
            temp = 0
            
            # 스택이 빌 때까지 다음을 반복:
            while stack:
    
                top = stack.pop()   # 스택 top 꺼내기

                # 숫자가 나오면 합산
                if isinstance(top, int):
                    temp += top

                # 문자가 나오면
                else:
                    if top == mapping[ch]:  # 닫는 괄호가 스택 top의 여는 괄호와 올바른 쌍을 이루는 경우
                        if ch == ')':       # '()'
                            stack.append(2 if temp == 0 else 2 * temp)  # 최초 괄호값 () = 2, (temp) = 2 * temp으로 계산하고 스택에 push
                        else:               # '[]'
                            stack.append(3 if temp == 0 else 3 * temp)  # 최초 괄호값 [] = 3, [temp] = 3 * temp으로 계산하고 스택에 push
                        break
                    # 올바른 쌍을 이루지 못하면 올바르지 않은 괄호열임
                    else:
                        return 0
                    
            # while이 break 없이 끝났다면 여는 괄호가 없던 것이므로 올바르지 않은 괄호열임
            else:
                return 0
    
    # 괄호열의 모든 문자 처리 후 스택의 괄호값 계산
    value = 0
    # 스택에 남아 있는 것들을 순회
    for item in stack:
        # 괄호가 남아 있다면 올바르지 않은 괄호열임
        if not isinstance(item, int):
            return 0
        # 스택에 남은 숫자들을 최종적으로 합산
        value += item
    # 최종 괄호값 반환
    return value

# main
s = list(input())   # 입력 문자열 받기
answer = cal_parentheses_value(s)   # 괄호값 계산하기
print(answer)   # 결과 출력
