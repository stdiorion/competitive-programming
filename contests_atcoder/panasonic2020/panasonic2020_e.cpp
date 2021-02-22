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
constexpr ll INF = 1'010'000'000'000'000'017LL;
constexpr ll MOD = 1'000'000'007LL;

string a, b, c;
ll s;
int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);

    cin >> a >> b >> c;
    
    s = len(a) + len(b) + len(c);
    
    rep(2) {
        rep(3) {
            rep(i, len(a) + 1){
                [&] () -> void{
                    rep(l, min(len(a) - i, len(b))) {
                        if (a[i + l] != b[l] && a[i + l] != '?' && b[l] != '?') {
                            return;
                        }
                    }
                    rep(j, max(len(b) + 1, len(a) - i + 1)) {
                        [&] () -> void{
                            rep(l, min(len(b) - j, len(c))){
                                if (b[j + l] != c[l] && b[j + l] != '?' && c[l] != '?') {
                                    return;
                                }
                            }
                            rep(l, min(len(a) - i - j, len(c))){
                                if (a[i + j + l] != c[l] && a[i + j + l] != '?' && c[l] != '?') {
                                    return;
                                }
                            }
                            s = min(s, max({ len(a), len(b) + i, len(c) + i + j }));
                        }();
                    }
                }();
            }
            swap(a, b);
            swap(b, c);
        }
        swap(a, c);
    }
    
    cout << s << endl;
}