#include<algorithm>
#include<vector>
#include<tuple>
#include<iostream>

using namespace std;

int find_parent(vector<int>& parent, int x){
    if(parent[x] != x){
        parent[x] = find_parent(parent,parent[x]);
    }
    return parent[x];
}

int union_sets(vector<int>& parent, int x, int y){
    x = find_parent(parent, x);
    y = find_parent(parent, y);

    if(x < y){
        parent[y] = x; 
    }else{
        parent[x] = y;
    }
}

int main(){
    int v,e;
    cin >> v >> e;

    int result = 0;

    vector<int> parent(v+1);

    for(int i = 0; i< v+1; i++){
        parent.push_back(i);
    }
    
    vector<tuple<int,int,int> > edges;

    for(int i = 0; i < e; i++){
        int a,b,c;
        cin >> a >> b >> c;
        tuple<int,int,int> tmp = {c,a,b};
        edges.push_back(tmp);
    }

    sort(edges.begin(), edges.end());

    for(int i = 0; i < e; i++){
        int x,y,count;
        count = get<0>(edges[i]);
        x = get<1>(edges[i]);
        y = get<2>(edges[i]);

        if(find_parent(parent, x) != find_parent(parent, y)){
            union_sets(parent, x, y);
        }

        result += count;
    }



}