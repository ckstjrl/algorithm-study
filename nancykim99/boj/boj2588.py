# BOJ2588. 곱셈 D1

N = int(input())
M = int(input())

n_str = list(str(N))
m_str = list(str(M))

multiply_level = []

for i in range(2, -1, -1):
    multiply_level.append(N * int(m_str[i]))

multiply_level.append(N*M)

for i in range(4):
    print(multiply_level[i])








