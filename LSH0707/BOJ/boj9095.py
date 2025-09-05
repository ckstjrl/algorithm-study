T = int(input())
for test_case in range(1, 1+T):
    N = int(input())
    cnt = 0
    visited = set()
    def a(n):  # a(0부터시작)
        global cnt
        if n > N:  # 매개변수값이 만들수N보다 크면 종료
            return
        if n == N:  # 정확히 N이면 global cnt + 1 종료
            cnt = cnt + 1
            return
        for i in [1,2,3]:  # 1 2 3중하나 더하고 재귀
            a(n+i)
    a(0)
    print(cnt)        