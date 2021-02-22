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
constexpr ll INF = 10100000000000017LL;
constexpr ll MOD = 1000000007LL;

ll n;
vec a(200000, 0);
ll dp[200000][3];
int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);

    cin >> n;
    rep(i, n) cin >> a[i];
    
    rep(i, n)
        rep(j, 3)
            dp[i][j] = (i == j) ? a[i] : -INF;
    
    rep(i, n) {
        dp[i + 2][0] = max(dp[i + 2][0], dp[i][0] + a[i + 2]);
        dp[i + 2][1] = max(dp[i + 2][1], dp[i][1] + a[i + 2]);
        dp[i + 2][2] = max(dp[i + 2][2], dp[i][2] + a[i + 2]);
        dp[i + 3][1] = max(dp[i + 3][1], dp[i][0] + a[i + 3]);
        dp[i + 3][2] = max(dp[i + 3][2], dp[i][1] + a[i + 3]);
        dp[i + 4][2] = max(dp[i + 4][2], dp[i][0] + a[i + 4]);
    }
    
    ll ans = max({ dp[n - 1][2], dp[n - 2][1], dp[n - 1][1], dp[n - 2][0] });
    if (n - 3 >= 0)
        ans = max(ans, dp[n - 3][0]);
    cout << ans << endl;
}