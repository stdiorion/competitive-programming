#include <iostream>
#include <vector>
#include <queue>
using namespace std;
using ll = long long;
using vec = vector<int>;
using vecvec = vector<vec>;
#define endl "\n"
#define rep_0() for (int i = 0;; i++)
#define rep_1(n) for (int _i = 0; _i < (int)(n); _i++)
#define rep_2(i, n) for (int i = 0; i < (int)(n); i++)
#define rep_3(i, s, n) for (int i = s; i < (int)(n); i++)
#define rep_4(i, s, n, d) for (int i = s; i < (int)(n); i+=d)
#define rep_x(x, a, b, c, d, F, ...) F
#define rep(...) rep_x(,##__VA_ARGS__,rep_4(__VA_ARGS__),rep_3(__VA_ARGS__),rep_2(__VA_ARGS__),rep_1(__VA_ARGS__),rep_0(__VA_ARGS__))
#define len(x) (int)((x).size())
#define all(x) (x).begin(),(x).end()
#define sum(v) accumulate(all(v))
#define MAX(v) *max_element(all(v))
#define MIN(v) *min_element(all(v))
#define append push_back
constexpr ll INF = 1'010'000'000'000'000'017LL;
constexpr ll MOD = 1'000'000'007LL;


int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);

    int n;
    cin >> n;
    vecvec g(n);
    rep(i, n - 1) {
        int u, v;
        cin >> u >> v;
        g[u - 1].push_back(v - 1);
        g[v - 1].push_back(u - 1);
    }

    vec f(n + 2, 1);
    rep(i, n) {
        f[i + 2] = f[i + 1] + f[i];
        if (f[i + 2] == n) {
            break;
        }
        else if (f[i + 2] > n) {
            cout << "NO" << endl;
            return 0;
        }
    }

    vec visited(n, 0);
    queue<int> d;

    d.push(0);

    while (!d.empty()) {
        int now = d.front();
        d.pop();
        visited[now] = 1;

        int count = 0;
        for (ll to : g[now]) {
            if (visited[to] == 1) continue;
            d.push(to);
            count++;
            if (count > 2) {
                cout << "NO" << endl;
                return 0;
            }
        }
    }
    cout << "YES" << endl;
}