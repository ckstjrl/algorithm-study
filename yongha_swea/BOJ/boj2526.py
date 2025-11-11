#BOJ2526 싸이클

#제곱할 수(A) 나눠줄 수 (B)
A, B = map(int, input().split())

change_num = A

left = []

loop = []

# 규칙성을 갖는다는 건 어느 순간 반복되는 수가 나타난다는 것
# 이에 기반해서 단순히 한 번 본 수를 모두 세는 게 아니라 반복되는 수가 나타난 시점에 다른 리스트에 넣고, loop 리스트
# 한번의 사이클이 끝나서 같은 수가 또다시 나오는 시점에 반목문을 깨고 loop리스트에 들어가 있는 item의 수를 출력
while True:
    num = (change_num * A % B)

    change_num = num
    if num in loop:
            break

    if num in left:
        loop.append(num)

    left.append(num)

print(len(loop))