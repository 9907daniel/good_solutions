// 10:02
// 
// N = 20만 -> NlogN / N
// 
// 1) 한번의 탐새을 통해 찾아야한다..
// 
// 알고리즘 : 슬라이등 윈도우
//
// 1. 일단 조건을 만족하는 첫 배열을 구해준다.. 
// 2. 탐색을 하며 뒤에를 하나 빼주고 앞에를 더해준다
// 3. 늘릴수 있다면 늘리고, 더이상 줄이지는 않는다


#include <string>
#include <iostream>
#include <unordered_map>

using namespace std;

int l[200000];
int n,k;

int main(){
    cin >> n >> k;

    for(int i = 0; i< n; i++){
        cin >> l[i];
    }

    unordered_map<int,int> dic;
    int left = 0;
    int right = 0;

    for(int i = 0; i < n; i ++ ){
        if (dic.find(l[i]) != dic.end()){
            if(dic[l[i]] < k ){
                dic[l[i]] += 1;
            }else{
                right = i;
                break;
            }
        }else{
            dic[l[i]] = 1;
        }
    }

    while(right < n){
        if (dic[l[left]] == 1){
            dic.erase(l[left]);
        }else{
            dic[l[left]] -= 1;
        }
        
        left += 1;
        right += 1;

        while (right < n){
            if(dic.find(l[right]) != dic.end()){
                if (dic[l[right]] < k){
                    dic[l[right]] += 1;
                }else{
                    dic[l[right]] += 1;
                    break;
                }
            }else{
                dic[l[right]] = 1;
            }
            right += 1;

        }
    }

    int answer = 0;
    for(int i = 0; i < 100000; i++){
        if(dic.find(i) != dic.end()){
            answer += dic[i];

            cout << i << dic[i] << endl;

        }
    }
    return 0;
}



