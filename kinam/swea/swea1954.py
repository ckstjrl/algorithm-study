'''
달팽이는 1부터 N*N까지의 숫자가 시계방향으로 이루어져 있다.

다음과 같이 정수 N을 입력 받아 N크기의 달팽이를 출력하시오.
'''
#나선 그리기 규칙
# 오른쪽 아래 왼쪽 위 순서를 반복
# 몇 칸씩 가는지 ?
# 처음에 N칸 /  (N-1) (N-1)칸 / (N-2) (N-2) 칸 / ... / 1 1 칸
#       오른쪽  아래   왼쪽      위     오       아 왼...
# 처음 N칸 가고 나머지 N에서 1씩 줄여가며 재귀?


from pprint import pprint

N = 5
arr = []
for i in range(N): #반복생성
    arr.append([0]*N)

#줄이기
arr = [[0] * N for _ in range(N)]
# [[0]*N]*N  이딴식으로 만들면 같은 메모리 참조해서 숫자가 같이 바뀜 // 매우 중요



n = 0 #N칸 / (N-1) (N-1)칸 / (N-2) (N-2) 칸 / ... / 1 1 칸 을 표현하기 위한 n 선언 루프마다 +1 예정
num = 1 #달팽이 배열에 넣을 숫자
while 1:
    if N-n-1 <= 1:
        break
    if num > N*N:
        break

    for i in range(n, N-n): # 첫 줄은 채우기 오른쪽 n = 0 일때 (0,N)
        arr[n][i] = num #[0]
        num += 1
    # print(arr)
  

    for i in range(n+1, N-n): # 아래  #n= 0/range(1, 5)
        arr[i][N-n-1] = num
        num += 1
    # print(arr)

    for i in range(N-n-2, n-1, -1): #왼쪽 #n=0 / range(3, -1, -1) 3 2 1 0 [4][3] [4][2]... 
        arr[N-n-1][i] = num
        num += 1
    # print(arr)


    for i in range(N-n-2, n, -1):  #위 #n=0 / range(3, 0, -1) [3][0] [2][0] [1][0]
        arr[i][n] = num
        num += 1
    # print(arr)

    n += 1
pprint(arr)


#>> 테두리를 먼저 채우고 재귀 하려 했는데 채우고 나니 굳이 쓸 필요가 있나 싶어서 재귀는 폐기
#(N-1) (N-1)칸 / (N-2) (N-2) 칸 / ... / 1 1 칸 규칙 활용
# def 나선(N):
#     if N == 0:
#         return
#     #아래로 감
#     arr[][N]