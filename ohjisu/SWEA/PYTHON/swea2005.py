"""
2005. 파스칼의 삼각형 D2

크기가 N인 파스칼의 삼각형을 만들어야 한다.
파스칼의 삼각형이란 아래와 같은 규칙을 따른다.

1. 첫 번째 줄은 항상 숫자 1이다.
2. 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성된다.

[제약 사항]
파스칼의 삼각형의 크기 N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)

[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스에는 N이 주어진다.
"""

"""
완성!
"""
# arr의 인접 요소를 합해주고 결과로 1 + 인접항 합산값 + 1을 출력하는 함수
def sum_arr(arr) :
    # 기본 요소 1 더하기
    result = [1]
    # arr로 받은 값의 합산 더하기
    for idx in range(len(arr)-1) :
        result.append(arr[idx] + arr[idx+1])
    # 기본 요소 1 더하기
    result.append(1)
    return result
# T 값 받기
T = int(input())
    

for tc in range(1, T+1) :
    # input 받기
    N = int(input())
    # 길이 N인 배열 정의  
    arr = [[1] for _ in range(N)]
    # N-1번 반복하면서 함수 호출 및 다음 값 찍어주기
    for i in range(N-1) :
        result = sum_arr(arr[i])
        arr[i+1] = result
    
    print(f'#{tc}')
    for item in arr :
        print(*item) 





"""
채점용 input 파일로 채점한 결과 fail 입니다.
(오답 : 10개의 테스트케이스 중 5개가 맞았습니다.)
"""
# T = int(input())

# def sum_arr(arr) :
#     result = [1]
#     for idx in range(len(arr)) :
#         if idx == len(arr)-1 :
#             result.append(arr[idx])
#             return result
#         else :            
#             result.append(arr[idx] + arr[idx+1])
    
#     return result
    

# for tc in range(1, T+1) :
#     N = int(input())
#     arr = [[1, 1]] + [[0] for _ in range(N)]
    
#     for i in range(N) :
#         result = sum_arr(arr[i])
#         arr[i+1] = result
#     print(f'#{tc}')
#     print(1)
#     for item in arr :
#         print(*item) 
