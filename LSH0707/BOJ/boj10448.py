T = int(input())
Tn = [i * (i+1) // 2 for i in range(1, 45)]  # 1000보다 작은 모든 삼각수 리스트
for _ in range(1, 1+T):
    N = int(input())
    ans = 0
    for x in Tn:  # 모든 조합 검사(x, y, z)
        for y in Tn:
            for z in Tn:
                if x + y + z == N:
                    ans = 1
                    break
            if ans == 1:
                break
        if ans == 1:
            break
    print(ans)
