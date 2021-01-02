#include <iostream>
using namespace std;

int r, c, k;
int items[3000][3000];
long dp[3000][3000][4];

main() {
    cin >> r >> c >> k;
    
    for(int i = 0; i < k; i++){
        int y, x, v;
        cin >> y >> x >> v;
        y--, x--;
        items[y][x] = v;
    }

    for(int y = 0; y < r; y++){
        for(int x = 0; x < c; x++){
            if(y != 0){
                dp[y][x][0] = max(max(dp[y - 1][x][0], dp[y - 1][x][1]), max(dp[y - 1][x][2], dp[y - 1][x][3]));
                dp[y][x][1] = dp[y][x][0] + items[y][x];
            }

            if(x != 0){
                dp[y][x][0] = max(dp[y][x][0], dp[y][x - 1][0]);
                for(int i = 0; i < 3; i++){
                    dp[y][x][i + 1] = max(dp[y][x][i + 1], dp[y][x - 1][i + 1]);
                    dp[y][x][i + 1] = max(dp[y][x][i + 1], dp[y][x - 1][i] + items[y][x]);
                }
            }
            else{
                dp[y][x][1] = dp[y][x][0] + items[y][x];
            }
        }
    }

    cout << max(max(dp[r - 1][c - 1][0], dp[r - 1][c - 1][1]), max(dp[r - 1][c - 1][2], dp[r - 1][c - 1][3])) << endl;
}