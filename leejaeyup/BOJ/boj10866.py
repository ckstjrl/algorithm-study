'''
문제
정수를 저장하는 덱(Deque)를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
명령은 총 여덟 가지이다.
push_front X: 정수 X를 덱의 앞에 넣는다.
push_back X: 정수 X를 덱의 뒤에 넣는다.
pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 덱에 들어있는 정수의 개수를 출력한다.
empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

입력
첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

출력
출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.
'''



N = int(input())

# 비어있는 리스트 선언.
empty_list = []

# 여기에 정답을 모아두었다가 출력하자.
result = []

# 주어진 예제들을 받아들이자.
for _ in range(N):
    lets_do_this = input().split()  # 예제 1의 3번 줄 입력 예시) ["push_front", "2"]

    # 그냥 문제 조건에서 주어진 해야되는 일들을 하나 하나 입력해보자.
    if lets_do_this[0] == "push_front":
        # push_front X: 정수 X를 덱의 앞에 넣는다.
        x = int(lets_do_this[1])
        empty_list.insert(0, x)

    elif lets_do_this[0] == "push_back":
        # push_back X: 정수 X를 덱의 뒤에 넣는다.
        x = int(lets_do_this[1])
        empty_list.append(x)

    elif lets_do_this[0] == "pop_front":
        # pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다
        if empty_list:
            result.append(str(empty_list.pop(0)))
        else:
            result.append("-1")

    elif lets_do_this[0] == "pop_back":
        if empty_list:
            # pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
            result.append(str(empty_list.pop()))
        else:
            result.append("-1")

    elif lets_do_this[0] == "size":
        # size: 덱에 들어있는 정수의 개수를 출력한다.
        result.append(str(len(empty_list)))

    elif lets_do_this[0] == "empty":
        # empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
        result.append("1" if not empty_list else "0")

    elif lets_do_this[0] == "front":
        # front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if empty_list:
            result.append(str(empty_list[0]))
        else:
            result.append("-1")

    elif lets_do_this[0] == "back":
        # back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if empty_list:
            result.append(str(empty_list[-1]))
        else:
            result.append("-1")



# 정답 출력
print("\n".join(result))