#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main(){
    int n = 0;
    int k;
    int l[1000000];
    int odd = 0; 
    int tot = 0; 
    int ans = 0; 
    int right = 0;

    cin >> n >> k;
    for(int i = 0; i < n; i++){
        cin >> l[i];
    }


    for(int i = 0; i < n; i++){

        if(l[i]%2 == 0){
            tot++;
        }else{
            if( odd+1 > k){
                ans = max(ans, tot);
                right = i;
                break;
            }else{
                odd++;
            }
        }

        if(odd < k){
            ans = max(ans, i-odd+1);
        }
    }

    for(int i = 0; i < n-right; i++){
        if (l[i] % 2 == 0) {
            tot--;
        }
        else{
            odd--;
        }
        while(right < n){
            if(l[right]%2 == 0){
                tot++;
            }else{
                if(odd+1 > k){
                    ans = max(ans, tot);
                    break;
                }else{
                    odd++;
                }
            }
            right ++;
        }
        if (odd < k){
            ans = max(ans, (right-i-odd));
        }
    }

    cout << ans;

    return 0;
}

