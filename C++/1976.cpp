#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

vector<int> parent;
int n,m;
int a,b,c;
vector<int> visited;

int find(int x){
    if(parent[x] != x){
        return find(parent[x]);
    }
    return x;
}

void union_set(int a, int b){
    a = find(a);
    b = find(b);

    if(a < b){
        parent[b] = a;  
    }else{
        parent[a] = b;
    }
}

int main(){
    cin >> n;
    cin >> m;

    for(int i=0; i<n+1;i++){
        parent.push_back(i);
    }

    for(int i=0; i < n; i++){
        for(int j=0; j<n; j++){
            cin >> a;
            if(a == 1){
                union_set(i+1,j+1);
            }
        }
    }

    int tmp;
    for(int i=0; i<m;i++){
        cin >> tmp;
        visited.push_back(tmp);
    }


    bool check = true;
    int current = -1;
    for(int i = 0; i< m; i++){
        if(i==0){
            if(parent[visited[i]] != visited[i]){
                parent[visited[i]] = find(visited[i]);
            }
            current = parent[visited[i]];
        }
        else{
        if(parent[visited[i]] != visited[i]){
            parent[visited[i]] = find(visited[i]);
        }
        if(parent[visited[i]] != current){
            check = false;
            break;
        }

        }
    }

    if(check == true){
        cout << "YES";
    }else{
        cout << "NO";
    }

}


