''' boj1406 D3 20250901 에디터
한 줄로 된 간단한 에디터를 구현하려고 한다. 
이 편집기는 영어 소문자만을 기록할 수 있는 편집기로, 최대 600,000글자까지 입력할 수 있다.

이 편집기에는 '커서'라는 것이 있는데, 커서는 문장의 맨 앞(첫 번째 문자의 왼쪽), 
문장의 맨 뒤(마지막 문자의 오른쪽), 
또는 문장 중간 임의의 곳(모든 연속된 두 문자 사이)에 위치할 수 있다. 
즉 길이가 L인 문자열이 현재 편집기에 입력되어 있으면, 
커서가 위치할 수 있는 곳은 L+1가지 경우가 있다.

이 편집기가 지원하는 명령어는 다음과 같다.

L	커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
D	커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
B	커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임
P $	: $라는 문자를 커서 왼쪽에 추가함
초기에 편집기에 입력되어 있는 문자열이 주어지고, 그 이후 입력한 명령어가 차례로 주어졌을 때, 
모든 명령어를 수행하고 난 후 편집기에 입력되어 있는 문자열을 구하는 프로그램을 작성하시오. 
단, 명령어가 수행되기 전에 커서는 문장의 맨 뒤에 위치하고 있다고 한다.

입력
첫째 줄에는 초기에 편집기에 입력되어 있는 문자열이 주어진다. 
이 문자열은 길이가 N이고, 영어 소문자로만 이루어져 있으며, 길이는 100,000을 넘지 않는다. 
둘째 줄에는 입력할 명령어의 개수를 나타내는 정수 M(1 ≤ M ≤ 500,000)이 주어진다. 
셋째 줄부터 M개의 줄에 걸쳐 입력할 명령어가 순서대로 주어진다. 
명령어는 위의 네 가지 중 하나의 형태로만 주어진다.

출력
첫째 줄에 모든 명령어를 수행하고 난 후 편집기에 입력되어 있는 문자열을 출력한다.
'''

'''
1. 커서는 문장 맨앞 or 맨 뒤 or 중간 아무데나 (그냥 아무데나 오는거 아닌가)
2. L 커서 왼쪽 
3. D 커서 오른쪽
4. B 커서 왼쪽 삭제
5. P 어쩌구  어쩌구를 커서 왼쪽에 추가
6. 문자열 주어짐
7. 초기 커서 위치는 문장 맨 뒤
'''
#추가 삭제 하더라도 커서의 오른쪽에는 문자가 그대로 있음
#왼쪽 오른쪽 하면 문자랑 커서의 위치가 바뀔듯

# 문자열을 리스트로 만들기, idx = 리스트의 길이로 설정하기
# 추가 : insert(idx, 값) 하고 idx += 1 해줘서 커서의 위치 유지
# 삭제 : pop(idx) 하고 idx -= 1 해줘서 커서의 위치 유지
# L R 은 각각 idx -= 1 += 1 해주면 될듯



# import sys
# from collections import deque
# input = sys.stdin.readline

# str_list = deque(input().strip())  #인풋을 리스트로 받기
# idx = len(str_list)
# M = int(input())
# for i in range(M):
#     oper = input().strip()  
    
#     if len(oper) == 3:      #문자를 추가하는 동작
#         str_list.insert(idx, oper[-1])
#         idx += 1
#     elif oper == 'L' and idx > 0:   #왼쪽으로 커서이동
#         idx -= 1
#     elif oper == 'D' and idx < len(str_list):   #오른쪽으로 커서이동
#         idx += 1
#     elif oper == 'B' and idx > 0:   #왼쪽 지우기
#         idx -= 1
#         # str_list.pop(idx)
#         del str_list[idx]

# print(''.join(str_list))




# 커서위치를 중심으로 스택과 큐 만들기
from collections import deque

front = list(input().strip())
back = deque()

# front 커서 back 의 구조로 구현할 것
# front에서는 pop, append
# back에서는 popleft, appendleft

M = int(input())    #명령 M개 들어옴
for i in range(M):
    oper = input()

    if len(oper) == 3:  #문자 추가
        front.append(oper[-1])
    
    elif oper == 'L':    #커서 왼쪽으로
        if front:
            back.appendleft(front.pop())
        
        else:
            continue
    
    elif oper == 'D':   #커서 오른쪽으로
        if back:
            front.append(back.popleft())
        
        else:
            continue
    
    elif oper == 'B':    #왼쪽 지우기
        if front:   #지울게 있어야 함
            front.pop()

        else:   #front 비어있으면 무시
            continue

print(*front, *back, sep='')