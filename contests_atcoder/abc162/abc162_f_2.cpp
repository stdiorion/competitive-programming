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
constexpr ll INF = 1010000000000000017LL;
constexpr ll MOD = 1000000007LL;

ll n;
ll a[200000];
ll ans;
ll offset0[100001], offset1[100001], offset2[100001];
pair<ll, ll> base_i[100001], base_j[100001];
int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);

    cin >> n;
    rep(i, n) cin >> a[i];
    
    if (n % 2) {
        offset0[0] = 0;
        offset1[0] = 0;
        offset2[0] = 0;
        rep(i, n / 2) {
            offset0[i + 1] = offset0[i] + a[i * 2];
            offset1[i + 1] = offset1[i] + a[i * 2 + 1];
            offset2[i + 1] = offset2[i] + a[i * 2 + 2];
        }
        ans = -INF;
        rep(i, n / 2 + 1)
            base_i[i] = pair<ll, ll>(offset0[i] - offset1[i], i);
        rep(j, n / 2 + 1)
            base_j[j] = pair<ll, ll>(offset1[j] - offset2[j], j);

        sort(base_i, base_i + 100001, greater<>());
        sort(base_j, base_j + 100001, greater<>());        
        
        rep(k, n / 2 + 1) {
            for (ll l = 0; l <= k; ++l) {
                if (base_i[l].second <= base_j[k - l].second)
                    ans = max(ans, base_i[l].first + base_j[k - l].first);
            }
            if (ans != -INF)
                break;
        }
        cout << ans + offset2[n / 2] << endl;
    }
    else {
        offset0[0] = 0;
        offset1[0] = 0;
        rep(i, n / 2) {
            offset0[i + 1] = offset0[i] + a[i * 2];
            offset1[i + 1] = offset1[i] + a[i * 2 + 1];
        }
        ans = -INF;
        rep(i, n / 2 + 1)
            ans = max(ans, offset0[i] - offset1[i] + offset1[n / 2]);
        cout << ans << endl;
    }
}