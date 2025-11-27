# BOJ 2447. 별 찍기 - 10 / D3
'''
문제
재귀적인 패턴으로 별을 찍어 보자. N이 3의 거듭제곱(3, 9, 27, ...)이라고 할 때, 크기 N의 패턴은 N×N 정사각형 모양이다.

크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.

***
* *
***
N이 3보다 클 경우, 크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)×(N/3) 정사각형을 크기 N/3의 패턴으로 둘러싼 형태이다.
예를 들어 크기 27의 패턴은 예제 출력 1과 같다.

입력
첫째 줄에 N이 주어진다. N은 3의 거듭제곱이다. 즉 어떤 정수 k에 대해 N=3k이며, 이때 1 ≤ k < 8이다.

출력
첫째 줄부터 N번째 줄까지 별을 출력한다.
'''
import sys
input = sys.stdin.readline

N = int(input().strip())

B = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
def find_power(N):
    cnt = 0
    while N != 1:
        N //= 3
        cnt += 1
    return cnt

def kronk(A, B):
    hA, wA = len(A), len(A[0])
    hB, wB = len(B), len(B[0])
    C = [[0]*(wA * wB) for _ in range(hA * hB)]
    for i in range(hA):
        for j in range(wA):
            if A[i][j]:
                for y in range(hB):
                    for x in range(wB):
                        C[i*hB+y][j*wB+x] = B[y][x]
    return C

K = find_power(N)
ans=[[1]]
for _ in range(K):
    ans = kronk(ans, B)

for u in range(len(ans)):
    for v in range(len(ans[0])):
        if ans[u][v] == 1:
            ans[u][v] = '*'
        else:
            ans[u][v] = ' '

for i in range(len(ans)):
    print(''.join(ans[i]))

'''
행렬 연산 중 크로네커 곱이라는 연산이 존재함
ex.
A = [[1, 4], 
     [2, 5], 
     [3, 6]]
B = [[1, 0], 
     [2, 3]]
A ⊗ B = 
[[1, 0, 4, 0],
 [2, 3, 8, 12],
 [2, 0, 5, 0],
 [4, 6, 10, 15], 
 [3, 0, 6, 0], 
 [6, 9, 12, 18]]

A[i][j] * B 가 새로운 2차원 행렬로 계산됨

이 연산을 kronk라는 함수로 표현
새로 만들어지는 함수의 크기는 A가 M X N, B가 P X Q이면 M*P X N*Q 가 된다.
이를 활용하여
입력 정수를 3의 몇 승인지 확인하여
그만큼 for 문을 진행하여 구한 후
1을 '*'로, 0을 ' '로 변경하는 과정을 거쳐 한 줄씩 출력함
'''