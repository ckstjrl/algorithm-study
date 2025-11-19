/*boj25558 - 내비게이션
ICPC Sinchon은 현대 오토에버로부터 차량 내비게이션의 테스트를 요청받았다. 
운영진들은 현대 오토에버의 OEM 순정 내비게이션의 성능과 그 외 
$N-1$개의 타사의 내비게이션의 성능을 비교했고, OEM 순정 내비게이션이 다른 내비게이션보다 더 효율적인 목적지까지의 최적 경로를 탐색하는 것을 확인할 수 있었다.

이에 대한 실험 데이터를 SUAPC 2022 Summer가 끝나고 나서 현대 오토에버에게 전달하고자 한다. 실험 데이터는 다음과 같은 정보들을 담고 있다.

시작점 
$(s_x, s_y)$와 도착점 
$(e_x, e_y)$ 
각 내비게이션의 시작점 
$(s_x, s_y)$에서 도착점 
$(e_x, e_y)$까지 도달하기 위해서 순차적으로 방문해야 하는 중간 지점들의 위치
두 지점 간의 거리는 맨해튼 거리로 정의된다. 즉, 
$(a,b)$와 
$(c,d)$와의 거리는 
$|a-c|+|b-d|$이다. 그리고 각 내비게이션이 안내한 목적지까지의 최적 경로의 거리는 서로 다르다.

그러나 SUAPC 2022 Summer 대회 당일에 컴퓨터의 갑작스러운 고장으로 인해 각 내비게이션에 대한 실험값들이 서로 뒤바뀌었다. 대회가 끝나기 전에 각 내비게이션의 데이터가 주어졌을 때, 어느 데이터가 OEM 순정 내비게이션인지 찾아보자
*/

#include <iostream>


long long absabs(long long x){
    // 절댓값 구현하기
    if (x < 0){
        return -x;
    }
    return x;
}

long long dist(long long x1, long long y1, long long x2, long long y2){
    return absabs(x1 - x2) + absabs(y1 - y2);
}

int main(){
    // - 10^9 ~ 10^9 범위. long long 사용하기
    // 현재 위치와 다음 위치의 dist 구하기
    // 현재 위치를 다음 위치로 갱신하고 다다음 위치와의 dist구하기
    // 반복하면 될듯
    int N;
    std::cin >> N;

    long long sx, sy, ex, ey;
    std::cin >> sx >> sy >> ex >> ey;


    long long min_dist = 2e14;
    int ans = 0;

    for (int i = 1; i <= N; i++){
        int M;
        std::cin >> M;

        long long current_x = sx; // 현재위치
        long long current_y = sy;
        long long total_dist = 0;

        for (int j = 1; j <= M; j++){
            long long tx, ty;
            std::cin >> tx >> ty;

            total_dist += dist(current_x, current_y, tx, ty);

            // 현재 위치를 다음 위치로 갱신
            current_x = tx;
            current_y = ty;
        }
        // 마지막 경유지 > 도착점 까지의 거리 추가
        total_dist += dist(current_x, current_y, ex, ey);
        
        if (total_dist < min_dist) {
            min_dist = total_dist;
            ans = i;
        }
    }

    
    std::cout << ans << "\n";

    return 0;
}