'''파스칼의 삼각형
크기가 N인 파스칼의 삼각형을 만들어야 한다.

파스칼의 삼각형이란 아래와 같은 규칙을 따른다.

1. 첫 번째 줄은 항상 숫자 1이다.

2. 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성된다.

N이 4일 경우,

N을 입력 받아 크기 N인 파스칼의 삼각형을 출력하는 프로그램을 작성하시오.
'''


T = int(input())
for t in range(1, T+1):
    N = int(input())
    stack1 = []
    stack2 = []
    print(f"#{t}")
    for i in range(N):
        if i % 2 == 0: #짝수번째 시행
            if len(stack1) == 0:#비어있으면 1 넣어줌
                stack1.append(1)
            for p in range(len(stack2)):
                if len(stack2) == 1: # stack2가 1개만 있으면 그냥 스택 1으로 옮겨줌
                    stack1.append(stack2.pop())
                else:#stack2에 있는거 뒤에서부터 하나씩 뺀것과 그 왼쪽꺼 더한 값을 stack1으로
                    stack1.append(stack2.pop()+stack2[-1])
            print(*stack1)

        elif i % 2 != 0: #홀수번째 시행
            if len(stack2) == 0:
                stack2.append(1)#비어있으면 1 넣어줌
            for q in range(len(stack1)):
                if len(stack1) == 1:
                    stack2.append(stack1.pop()) #스택1이 1개만 남으면 스택2로 넘겨줌
                else:#스택1에서 pop한 것과 그 왼쪽 값 더해서 넘겨줌
                    stack2.append(stack1.pop()+stack1[-1])
            print(*stack2)

