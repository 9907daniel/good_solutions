#include <string>
#include <iostream>

using namespace std;

int main(){
    int n;
    int l[100000];

    cin >> n;
    
    for(int i = 0; i < n ; i++){
        cin >> l[i];
    }

    int start = 0;
    int end = n-1;
    int answer = 0;

    while(start <= end){
        int smaller = min(l[start],l[end]);
        int difference = end-start-1;

        answer = max(smaller*difference, answer);
        if(l[start] < l[end]){
            start++;
        }else{
            end -= 1;
        }

    }
    cout << answer;
    return 0;
}