'''boj1863 20250902 스카이라인 쉬운거
도시에서 태양이 질 때에 보이는 건물들의 윤곽을 스카이라인이라고 한다. 
스카이라인만을 보고서 도시에 세워진 건물이 몇 채인지 알아 낼 수 있을까? 
건물은 모두 직사각형 모양으로 밋밋하게 생겼다고 가정한다.

정확히 건물이 몇 개 있는지 알아내는 것은 대부분의 경우에 불가능하고, 
건물이 최소한 몇 채 인지 알아내는 것은 가능해 보인다. 이를 알아내는 프로그램을 작성해 보자.

입력
첫째 줄에 n이 주어진다. (1 ≤ n ≤ 50,000) 다음 n개의 줄에는 왼쪽부터 스카이라인을 보아 갈 때 
스카이라인의 고도가 바뀌는 지점의 좌표 x와 y가 주어진다. (1 ≤ x ≤ 1,000,000. 0 ≤ y ≤ 500,000) 
첫 번째 지점의 x좌표는 항상 1이다.

출력
첫 줄에 최소 건물 개수를 출력한다.
'''

# #직사각형을 어떻게 찾을 것인가?
# N = int(input())

# change_height = [list(map(int, input().split())) for _ in range(N)]

# # print(change_height)

# height_stack = []
# another_stack = []
# cnt = 0
# min = 0
# for change in change_height:    #바뀐 고도 y를 높이 스택에 저장

#     if change[1] in height_stack:   #만약 같은 고도 높이가 있으면?
#         while change[1] in height_stack:    #없어질때까지 pop
#             another_stack.append(height_stack.pop())    #pop한거는 다른 스택에 넣음
#             #마지막에는 change[1]과 같은 숫자가 들어가있음

#         another_stack.pop() #마지막에 들어간 같은 고도 빼버림
#         cnt += 1    #고도가 같으면 건물 하나로 취급해서 카운트 + 1
        
#         while another_stack:    #빼놨던 숫자들 다시 고도y 스택으로
#             height_stack.append(another_stack.pop())

#     else:   #같은 고도의 높이가 없으면 그냥 넣음
#         height_stack.append(change[1])

# cnt += len(height_stack)    #스택에 남아있는 각각의 고도y는 건물에 해당함



# print(cnt)



# N = int(input())

# change_height = [list(map(int, input().split())) for _ in range(N)]

# height_stack = []
# cnt = 0

# for change in change_height:    #바뀐 고도 y를 높이 스택에 저장
#     height_stack.append(change[1])

# # print(height_stack)


# height_list = []
# temp = []

# #[1, 2, 1, 3, 1, 0, 2, 3, 2, 1] 이런식으로 고도 y가 저장된 리스트를 0(가장 낮은 고도?)을 기준으로 나눠줄 것
# #[[1, 2, 1, 3, 1], [2, 3, 2, 1]] 형태
# for n in height_stack:
#     if n == min(height_stack):
#         if temp:
#             height_list.append(temp)
#             temp = []

#     else:
#         temp.append(n)

# if temp:    #temp 남아있으면 마저 추가해줌
#     height_list.append(temp)

# # print(height_list)

# for each in height_list:
#     cnt += len(each)    #서로 다른 높이 = 서로 다른 건물

# print(cnt)


N = int(input())

stack = []
cnt = 0
for i in range(N):
    x, y = map(int, input().split())

    while stack and stack[-1] > y:  #스택이 비어있지 않고 스택의 마지막 수가 y보다 크면 제거하면서 카운트 증가
        stack.pop()
        cnt += 1

    # y == 0일때는 무시하면서 스택이 비어있거나 새로운 높이가 큰 높이이면 
    if y > 0 and (not stack or stack[-1] < y):
        stack.append(y)

        
cnt += len(stack) #스택에 남아있는 건물 수 합해줌

print(cnt)