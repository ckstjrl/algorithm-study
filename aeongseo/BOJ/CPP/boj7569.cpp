/*** 7569. 토마토 ***/

#include<iostream>
#include<vector>
#include<deque>
#include<tuple>
#include<algorithm>
using namespace std;

int bfs(deque<tuple<int, int, int>> dq);

vector<vector<vector<int>>> tomato;
vector<vector<vector<int>>> visited;	// 일수를 세기 위한 방문 배열

// 인접한 토마토 델타
int dk[6] = { -1, 0, 0, 0, 0, 1 };
int di[6] = { 0, 0, 1, 0, -1, 0 };
int dj[6] = { 0, 1, 0, -1, 0, 0 };

int M, N, H;

int main() {
	cin >> M >> N >> H;
	tomato.assign(H, vector<vector<int>>(N, vector<int>(M)));
	visited.assign(H, vector<vector<int>>(N, vector<int>(M, 0)));

	deque<tuple<int, int, int>> dq;	// 익은 토마토의 3차원 좌표 받기 위한 덱

	for (int h = 0; h < H; h++) {
		for (int n = 0; n < N; n++) {
			for (int m = 0; m < M; m++) {
				cin >> tomato[h][n][m];	// 토마토 상자 정보 입력
				if (tomato[h][n][m] == 1) {	// 익은 토마토면 덱에 저장, 방문 1 표시
					dq.push_back({ h, n, m });
					visited[h][n][m] = 1;
				}
			}
		}
	}

	int ans = bfs(dq);
	cout << ans;

	return 0;
}

int bfs(deque<tuple<int, int, int>> dq) {
	while (!dq.empty()) {	// 덱이 빌 때까지 반복
		int tk, ti, tj;
		tie(tk, ti, tj) = dq.front();	// 덱의 처음값 좌표 꺼내기
		dq.pop_front();

		for (int i = 0; i < 6; i++) {	// 6방향의 토마토 (위, 아래, 왼쪽, 오른쪽, 앞, 뒤)
			int wk = tk + dk[i];
			int wi = ti + di[i];
			int wj = tj + dj[i];
			if (0 <= wk && wk < H && 0 <= wi && wi < N && 0 <= wj && wj < M && tomato[wk][wi][wj] != -1 && visited[wk][wi][wj] == 0) {	// 배열을 벗어나지 않고 토마토가 빈 상자가 아니면서 방문한 적이 없다면
				dq.push_back({ wk, wi, wj });	// 덱에 추가
				visited[wk][wi][wj] = visited[tk][ti][tj] + 1;	// 영향받은 토마토 상자에서 1일 늘려 저장
				tomato[wk][wi][wj] = 1;	// 익은 토마토로 변경
			}
		}
	}

	// 최소 필요한 일수 확인
	int max_day = 0;
	for (int h = 0; h < H; h++) {
		for (int n = 0; n < N; n++) {
			for (int m = 0; m < M; m++) {
				if (tomato[h][n][m] == 0) {	// 토마토 상자에서 안익은 토마토가 있다면 -1 반환
					return -1;
				}
				max_day = max(max_day, visited[h][n][m] - 1);	// 안익은 토마토가 없다면 최대 일수-1 저장 (시작이 1일부터였기 때문에 1 뺌)
			}
		}
	}
	return max_day;

}