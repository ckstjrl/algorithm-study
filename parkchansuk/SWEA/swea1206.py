for tc in range(1,11):
    N = int(input())
    height = list(map(int, input().split()))
    see = [0]*N # 건물 별 전망 확보 층 개수
    for i in range(2, N-2):
        # 앞 뒤로 2칸씩은 건물이 없으므로 range(2, N-2)로 설정
        if (height[i] > height[i-1]) & (height[i] > height[i-2]) & (height[i] > height[i+1]) & (height[i] > height[i+2]):
            # i번째 건물 앞으로 두칸 뒤로 두칸 모두 시야 확보되면 if 진행
            max_height = 0
            height_near = [height[i-2], height[i-1], height[i+1], height[i+2]]
            # 근처 건물중 가장 높은 건물을 찾기 위해 리스트화 시킴
            for j in height_near:
                if max_height < j:
                    max_height = j
            see[i] = height[i]- max_height
            # 건물의 전망 확보 층을 계산하려면 근처 가장 높은 건물 층수만큼 빼야함
     
    sum_s = 0
    for s in see:
        sum_s += s
        #전망확보된 층 개수 리스트를 전부 합치면 전망확보 층수를 구함 수 있음
 
    print(f'#{tc} {sum_s}')