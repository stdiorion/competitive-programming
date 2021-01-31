#include <bits/stdc++.h>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;

    cout << "A:";
    int i = 0;
    while (i < a) {
        cout << "]";
        i++;
    }
    cout << endl;

    cout << "B:";
    i = 0;
    while (i < b) {
        cout << "]";
        i++;
    }
    cout << endl;
}