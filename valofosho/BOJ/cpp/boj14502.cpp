#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int n, m;
int answer = 0;
int di[4] = {-1, 1, 0, 0};
int dj[4] = {0, 0, -1, 1};

// 바이러스 칸, 침투가능 칸
vector<pair<int, int>> virus;
vector<pair<int, int>> blank;

//원본 맵이랑 카피용 하나

vector<vector<int>> maps;
vector<vector<int>> tempmaps;

int count_blank(){
	int cnt = 0;
	for (int i = 0; i < n; i++){
		for (int j=0; j < m; j++){
			if(tempmaps[i][j] == 0){
				cnt += 1;
			}
		}
	}
	return cnt;
}


void spread(){
	tempmaps = maps;
	queue<pair<int, int>> q;
	
	for (auto &p: virus){
		q.push(p);
	}
	while(!q.empty()){
		auto [i, j] = q.front();
		q.pop();
		for (int d = 0; d < 4; d++){
			int ni = i + di[d];
			int nj = j + dj[d];
			
			if (ni < 0 || ni >= n|| nj < 0 || nj >= m) continue;
			if (tempmaps[ni][nj] == 0){
				tempmaps[ni][nj] = 2;
				q.push({ni, nj});
			}
		}
		
	}
}
int main(){
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> n >> m;
	maps.assign(n, vector<int>(m));
	tempmaps.assign(n, vector<int>(m));
	for (int i = 0; i < n; i++){
		for (int j=0; j < m; j++){
			cin >> maps[i][j];
			
			if (maps[i][j] == 2){
				virus.push_back({i, j});
			} else if(maps[i][j] == 0){
				blank.push_back({i, j});
			}
		}
	}
	
	int bs = blank.size();
	for (int i = 0; i < bs; i++){
		for (int j = i+1; j < bs; j++){
			for (int k = j+1; k < bs; k++){
				auto [wr1, wc1] = blank[i];
				auto [wr2, wc2] = blank[j];
				auto [wr3, wc3] = blank[k];
				
				maps[wr1][wc1] = 1;
				maps[wr2][wc2] = 1;
				maps[wr3][wc3] = 1;
				
				spread();
				answer = max(answer, count_blank());
				maps[wr1][wc1] = 0;
				maps[wr2][wc2] = 0;
				maps[wr3][wc3] = 0;

			}
		}
	}
	cout << answer << '\n';
}