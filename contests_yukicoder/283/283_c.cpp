#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vec = vector<ll>;
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
#pragma GCC optimize("O3")
#pragma GCC target("avx2")
#pragma GCC optimize("unroll-loops")

int v;
ll d;
bool g[2000][2000], ans[2000][2000];
string edge[2000];
bool res[2000][2000];

void power(int sz, bool a[][2000], bool b[][2000]) {
    rep(i, sz) rep(j, sz) res[i][j] = false;
    rep(i, sz) rep(j, i, sz) rep(k, sz)
        if (a[i][k] & b[k][j]) {
            res[i][j] = res[j][i] = true;
            break;
        }
    rep(i, sz) rep(j, sz) a[i][j] = res[i][j];
}

int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);

    cin >> v >> d;
    rep(i, v) cin >> edge[i];

    rep(i, v)
        rep(j, v) {
            g[i][j] = (edge[i][j] == '1');
            ans[i][j] = (i == j);
        }

    d = min(d, (ll) 2 * v);
    
    while (d) {
        if (d & 1) {
            rep(i, v) rep(j, v) res[i][j] = false;
            rep(i, v) rep(j, i, v) rep(k, v)
                if (ans[i][k] & g[k][j]) {
                    res[i][j] = res[j][i] = true;
                    break;
                }
            rep(i, v) rep(j, v) ans[i][j] = res[i][j];
        }
        rep(i, v) rep(j, v) res[i][j] = false;
        rep(i, v) rep(j, i, v) rep(k, v)
            if (g[i][k] & g[k][j]) {
                res[i][j] = res[j][i] = true;
                break;
            }
        rep(i, v) rep(j, v) g[i][j] = res[i][j];
        d >>= 1;
    }

    rep(i, v)
        rep(j, v)
            if (!ans[i][j]) {
                puts("No");
                return 0;
            }
    puts("Yes");
}