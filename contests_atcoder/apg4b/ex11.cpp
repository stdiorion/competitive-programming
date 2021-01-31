#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    int a;
    cin >> a;

    string o;
    int b;
    for (int i = 0; i < n; i++) {
        cin >> o >> b;
        if (o == "+") {
            a += b;
        }
        else if (o == "-") {
            a -= b;
        }
        else if (o == "*") {
            a *= b;
        }
        else if (o == "/" && b != 0) {
            a /= b;
        }
        else {
            cout << "error" << endl;
            break;
        }
        cout << i + 1 << ":" << a << endl;
    }
}