A = int(input())
B = int(input())
print(A * ((B % 100) % 10))  # A * B[2] 출력
print(A * ((B // 10) % 10))  # A * B[1] 출력
print(A * (B // 100))  # A * B[0] 출력
print(A * B)  