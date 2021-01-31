#include <bits/stdc++.h>
using namespace std;

int main() {
    int a, b;
    string o;
    cin >> a >> o >> b;

    if (o == "+") 
        cout << a + b << endl;
    else if (o == "-")
        cout << a - b << endl;
    else if (o == "*")
        cout << a * b << endl;
    else if (o == "/") {
        if (b == 0)
            cout << "error" << endl;
        else
            cout << a / b << endl;
    }
    else
        cout << "error" << endl;
}