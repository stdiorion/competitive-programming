#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vec = vector<ll>;
using vecvec = vector<vec>;
#define endl "\n"
#define rep_0() for (ll i = 0;; i++)
#define rep_1(n) for (ll _i = 0; _i < (ll)(n); _i++)
#define rep_2(i, n) for (ll i = 0; i < (ll)(n); i++)
#define rep_3(i, s, n) for (ll i = s; i < (ll)(n); i++)
#define rep_4(i, s, n, d) for (ll i = s; i < (ll)(n); i+=d)
#define rep_x(x, a, b, c, d, F, ...) F
#define rep(...) rep_x(,##__VA_ARGS__,rep_4(__VA_ARGS__),rep_3(__VA_ARGS__),rep_2(__VA_ARGS__),rep_1(__VA_ARGS__),rep_0(__VA_ARGS__))
#define len(x) (ll)((x).size())
#define all(x) (x).begin(),(x).end()
#define sum(v) accumulate(all(v))
#define MAX(v) *max_element(all(v))
#define MIN(v) *min_element(all(v))
#define append push_back
const ll INF = 1'010'000'000'000'000'017LL;
const ll MOD = 1'000'000'007LL;


int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);

    int h, w, k;
    cin >> h >> w >> k;
    
    int x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;
    x1--; y1--; x2--; y2--;
    
    vector<string> field(h);
    rep(i, h) cin >> field[i];
    
    int dirx[] = { 1, 0, -1, 0 };
    int diry[] = { 0, 1, 0, -1 };
    
    vector<vector<int>> cost(h, vector<int>(w, 10000000));
    cost[x1][y1] = 0;
    
    queue<pair<int, int>> d;
    d.emplace(x1, y1);
    
    while(d.size()) {
        auto now = d.front();
        int x = now.first;
        int y = now.second;
        d.pop();
        
        if (x == x2 && y == y2) {
            cout << cost[x][y] << endl;
            return 0;
        }
        
        for (int dir = 0; dir < 4; ++dir) {
            for (int dis = 1; dis <= k; ++dis) {
                int x_to = x + dirx[dir] * dis;
                int y_to = y + diry[dir] * dis;
                
                if (!(0 <= x_to && x_to < h && 0 <= y_to && y_to < w) or field[x_to][y_to] == '@') {
                    break;
                }
                
                int new_cost = cost[x][y] + 1;
                if (cost[x_to][y_to] > new_cost) {
                    cost[x_to][y_to] = new_cost;
                    d.emplace(x_to, y_to);
                }
                else if (cost[x_to][y_to] < new_cost) {
                    break;
                }
            }
        }
    }
    
    cout << -1 << endl;
}