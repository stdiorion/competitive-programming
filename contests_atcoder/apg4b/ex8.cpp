#include <bits/stdc++.h>
using namespace std;

int main() {
    int pat;
    cin >> pat;

    string text;
    int price, n;

    if (pat == 1) {
        cin >> price >> n;
        cout << price * n << endl;
    }
    else {
        cin >> text >> price >> n;
        cout << text + "!" << endl;
        cout << price * n << endl;
    }
}