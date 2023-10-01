#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n;
int graph[17][17];
int dp[17][17][3];

int main(){
    cin >> n;

    for(int i=0; i< n;i++){
        for(int j=0; j< n;j++){
            cin >> graph[i][j];
        }
    }

    dp[0][1][0] = 1;

    for(int i =0; i<n; i++){
        for(int j=0; j<n; j++){
            if(graph[i][j] != 1){
                for(int k=0; k <3; k++){
                    if(k == 0){
                        if(j+1 < n && graph[i][j+1] != 1){
                            dp[i][j+1][k] += dp[i][j][0];
                            dp[i][j+1][k] += dp[i][j][2];
                        }
                    }
                    if(k == 1){
                        if(i+1 < n && graph[i+1][j] != 1){
                            dp[i+1][j][k] += dp[i][j][1];
                            dp[i+1][j][k] += dp[i][j][2];
                        }
                    }
                    if(k == 2){
                        if(j+1 < n && i+1 < n && graph[i+1][j+1] != 1 && graph[i+1][j] != 1 && graph[i][j+1] != 1){
                            dp[i+1][j+1][k] += dp[i][j][0];
                            dp[i+1][j+1][k] += dp[i][j][1];
                            dp[i+1][j+1][k] += dp[i][j][2];
                        }
                    }
                }
            }
        }
    }

    int answer = 0;
    for(int a=0; a<3; a++){
        answer += dp[n-1][n-1][a];
    }


    cout << answer;
    return 0;
}






