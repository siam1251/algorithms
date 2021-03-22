int bfs(string &current, string& end){
        
        queue<string> q;
        q.push(current);
        int length = 1;
        while(q.size()){
            queue<string> child_q;
            while(q.size()){
                string front = q.front();
                if(front == end) return length;
                visited.insert(front);
                q.pop();
                vector<string> new_words = get_nextWords(front);
                
                for(auto &&w: new_words){
                    if(visited.count(w) == 0)
                        child_q.push(w);
                }
               
            }
            length++;
            q = std::move(child_q);
        }
        cout<<"end";
        return 0;
        
    }
