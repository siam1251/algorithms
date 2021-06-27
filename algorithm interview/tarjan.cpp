
///https://leetcode.com/problems/critical-connections-in-a-network/
   


class Solution {
    
    unordered_map<int, unordered_set<int>> c;
    vector<bool> on_stack;
    vector<int> level;
    vector<vector<int>> num_cons;
    vector<int> low_level;
    int cur_level = 0;
    stack<int> m_stack;
    
    void DFS( int i, int parent){
        
        cur_level++;
        level[i] = cur_level;
      
        low_level[i] = level[i];
        on_stack[i] = true;
        m_stack.push(i);
        int tmp = INT_MAX;
        for( int n: c[i]){
            c[n].erase(i);
            if(level[n] == INT_MAX){
                
                DFS( n , i);
                
            }
           // level[D] == low_level[D]
           // since there is no path that connects previous visited node from D
          // if it's already part of another strongly connected (they wont be on_stack) we will ignore them
            if(on_stack[n]){
                low_level[i] = min(low_level[i], low_level[n]);
            }
        }
        // we are at the root node of scc
        // current low_level is the minimum
        //      B        E   
        //    /  \     /  \
        //   A -- C---D ---F
        // level[D] == low_level[D]
        // since there is no path that connects previous visited node from D
        if(level[i] == low_level[i]){
            while(m_stack.size()){
                auto node = m_stack.top();
                on_stack[node] = false;
                m_stack.pop();
                low_level[node] = low_level[i];
                if(node == i)break;
            }
        }
        
        
        
        
        
    }
    
    void print(vector<int> & lv){
        cout<<"\n";
        for(int i = 0; i < lv.size(); i++)cout<<i<<":"<<lv[i]<<" ,";
    }
public:
    vector<vector<int>> criticalConnections(int n, vector<vector<int>>& connections) {
        low_level = vector<int>(n, INT_MAX);
        on_stack.resize(n, false);
        level = vector<int>(n, INT_MAX);
      
        for(auto v: connections){
            c[v[0]].insert(v[1]);
            c[v[1]].insert(v[0]);
        }
       
        
        DFS( 0, -1);
        //print(low_level);
        //print(level);
        vector<vector<int>> ret;
        for(auto v: connections){
           // cout<<v[0] <<"-" <<v[1] <<":"<<num_cons[v[0]][v[1]]<<"\n";
            if(low_level[v[0]] != low_level[v[1]] ){
                ret.push_back(v);
            }
        }
        return ret;
        
        
    }
};
