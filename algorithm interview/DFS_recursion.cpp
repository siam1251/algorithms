// https://leetcode.com/problems/word-search-ii/
class Solution {
    unordered_set<string> st;
    unordered_set<string> results;
    int mx_len;
    
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        for(auto &&w: words){
            mx_len = max(mx_len, (int)w.size());
            st.insert(w);
        }
        vector<vector<bool>> visited(board.size(), vector<bool>(board[0].size(), false));
        for(int i = 0; i < board.size(); i++){
            for(int j = 0; j < board[0].size(); j++){
                string cur;
                cur.push_back(board[i][j]);
                
                dfs(i, j, cur, board, visited);
            }
        }
        cout<<"result";
        return vector<string>(results.begin(), results.end());
        
    }
    
    vector<int> X{0, 0, 1,-1};
    vector<int> Y{1,-1, 0 ,0};
    
    void dfs(int y, int x, string &cur, vector<vector<char>>& board, vector<vector<bool>>& visited){
        //cout<<cur<<endl;
        if(cur.size() > mx_len) return;
        if(st.count(cur)){
            
            results.insert(cur);
        }
        if(visited[y][x]) return;
        visited[y][x] = true;
        for(int i = 0; i < Y.size(); i++){
            int xx = x+X[i];
            int yy = y+Y[i];
            if(xx >= 0 && xx < board[0].size() && yy >= 0 && yy < board.size() && visited[yy][xx] == false){
                cur.push_back(board[yy][xx]);
                //visited[yy][xx] = true;
                dfs(yy, xx, cur, board, visited);
                //visited[yy][xx] = false;
                cur.pop_back();
            }
        }
        visited[y][x] = false;
    }
};
