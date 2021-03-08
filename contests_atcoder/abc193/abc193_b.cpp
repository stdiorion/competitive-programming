#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int ans = 1001001001;
    for (int i = 0; i < n; ++i) {
        int a, p, x;
        cin >> a >> p >> x;
        if (a < x && p < ans) {
            ans = p;
        }
    }
    if (ans == 1001001001) ans = -1;
    cout << ans << endl;
}