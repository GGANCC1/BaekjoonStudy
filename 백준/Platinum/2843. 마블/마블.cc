#include<bits/stdc++.h>
using namespace std; 
int n, a[300004], m, t1, t2, uf[300004],isCycle[300004], cnt[300004];
vector<pair<int, int>> v; 
vector<string> ret; 
int uf_find(int a){
    if(uf[a] < 0) return a; 
    return uf[a] = uf_find(uf[a]);
}
void uf_merge(int a, int b){ 
    a = uf_find(a); b = uf_find(b);   
    if(a != b){ 
        uf[b] = a; 
    }else isCycle[a] = 1;  
}
int main(){
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    fill(uf, uf + 300004, -1);
    cin >> n; for(int i = 1; i <= n; i++) cin >> a[i]; 
    cin >> m; 
    for(int i = 0; i < m; i++){
        cin >> t1 >> t2; 
        v.push_back({t1, t2});
        if(t1 == 2) cnt[t2] = 1; 
    }
    for(int i = 1; i <= n; i++){
        if(cnt[i] == 0 && a[i])uf_merge(a[i], i);
    }
    reverse(v.begin(), v.end()); 
    for(auto it : v){
        if(it.first == 1){ 
            if(isCycle[uf_find(it.second)]) ret.push_back("CIKLUS"); 
            else ret.push_back(to_string(uf_find(it.second)));  
        }else if(it.first == 2){
            uf_merge(a[it.second], it.second); 
        }
    } 
    for(int i = ret.size() - 1; i >= 0; i--) cout << ret[i] << "\n";
}