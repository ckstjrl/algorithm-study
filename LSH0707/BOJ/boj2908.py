A, B = map(str, input().split())
AA = int(A[2] + A[1] + A[0])
BB = int(B[2] + B[1] + B[0])  # 숫자 뒤집기
if AA > BB:  # 비교해서 더 큰 수 출력
    print(AA)
elif AA < BB:
    print(BB)