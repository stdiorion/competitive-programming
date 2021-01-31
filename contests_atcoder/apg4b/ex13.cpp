#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    
    vector<int> scores(n);
    
    for (int i = 0;i < n;i++) {
        cin >> scores.at(i);
    }
    
    int avg = accumulate(scores.begin(), scores.end(), 0) / scores.size();
    
    int ans = 0;
    
    for (int i = 0;i < n;i++) {
        cout << abs(scores.at(i) - avg) << endl;
    }
}