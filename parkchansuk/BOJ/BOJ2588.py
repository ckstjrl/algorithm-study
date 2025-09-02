# BOJ 2588. 곱셈 / D1
'''
(세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.

(1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.
'''
import sys
A = sys.stdin.readline()
B = sys.stdin.readline()

C = int(A) * int(B[2]) # B의 1의 자리와 A 곱
D = int(A) * int(B[1]) # B의 10의 자리와 A 곱
E = int(A) * int(B[0]) # B의 100의 자리와 A 곱

ans = int(A) * int(B) # 둘이 그냐 곱한거

print(C)
print(D)
print(E)
print(ans) #순서대로 출력