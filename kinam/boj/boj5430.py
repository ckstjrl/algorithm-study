'''boj5430 AC
선영이는 주말에 할 일이 없어서 새로운 언어 AC를 만들었다. 
AC는 정수 배열에 연산을 하기 위해 만든 언어이다. 
이 언어에는 두 가지 함수 R(뒤집기)과 D(버리기)가 있다.

함수 R은 배열에 있는 수의 순서를 뒤집는 함수이고, D는 첫 번째 수를 버리는 함수이다. 
배열이 비어있는데 D를 사용한 경우에는 에러가 발생한다.

함수는 조합해서 한 번에 사용할 수 있다. 
예를 들어, "AB"는 A를 수행한 다음에 바로 이어서 B를 수행하는 함수이다.
예를 들어, "RDD"는 배열을 뒤집은 다음 처음 두 수를 버리는 함수이다.

배열의 초기값과 수행할 함수가 주어졌을 때, 최종 결과를 구하는 프로그램을 작성하시오.
'''

# R(뒤집기): 배열에 있는 수의 순서 뒤집기
# D(버리기): 첫 번째 수를 버리기 + 배열 비었을 때 D 사용하면 에러



# T = int(input())
# for t in range(1, T+1):
#     p = input()
#     n = int(input())
#     arr_ac = input() # [1, 2, 3, 4]같은 리스트를 문자열로 받음
#     # '[1, 2, 3, 4]'
#     arr_ac = arr_ac.strip('[]') #양 끝 대괄호 없애기 '1, 2, 3, 4'
#     arr_ac = [int(x) for x in arr_ac.split(',') if x]
#     #arr_ac.split(', ') 하면 스플릿 매서드가 문자열을 리스트로 만듦 ['1', '2', '3', '4']
#     #문자열로 된 숫자들을 정수형으로 받기 위해 map(int, ) 사용
#     # arr_ac = list(map(int, arr_ac.split(','))) >> 빈 리스트일 때 에러남 
#     for i in p:
#         if i == 'R':
#             arr_ac = arr_ac[::-1]
        
#         elif arr_ac:
#             arr_ac.pop(0)

#         else:
#             print('error')
#             break
#     if arr_ac:
#         print(arr_ac)

# >>>> arr_ac = arr_ac[::-1] 매번 하느라 시간 많이 잡아먹는듯


T = int(input())
for t in range(1, T+1):
    p = input()
    n = int(input())
    arr_ac = input() # [1, 2, 3, 4]같은 리스트를 문자열로 받음
    # '[1, 2, 3, 4]'
    arr_ac = arr_ac.strip('[]') #양 끝 대괄호 없애기 '1, 2, 3, 4'
    arr_ac = [int(x) for x in arr_ac.split(',') if x]
    #arr_ac.split(', ') 하면 스플릿 매서드가 문자열을 리스트로 만듦 ['1', '2', '3', '4']
    #문자열로 된 숫자들을 정수형으로 받기 위해 map(int, ) 사용
    # arr_ac = list(map(int, arr_ac.split(','))) >> 빈 리스트일 때 에러남 
    isreverse = False
    error = False
    left = 0 #정항향 배열의 D를 구현위해 선언
    right = len(arr_ac) #역방향 배열의 D 구현위해 선언
    for i in p:
        if i == 'R' and isreverse == False:
            isreverse = True
        
        elif i == 'R' and isreverse == True:
            isreverse = False
        
        elif i == 'D':
            if left >= right:
                print('error')
                error = True
                break
            if not isreverse: #정방향이면?
                left += 1
            else:
                right -= 1 # 역방향이먄?


    if not error:
        result = arr_ac[left:right]
        if isreverse:
            result = result[::-1]
        
        print('[' + ','.join(map(str, result)) + ']')