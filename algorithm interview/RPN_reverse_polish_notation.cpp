//  https://leetcode.com/problems/basic-calculator
class Solution {
    unordered_map<char, int> mp{
        {'(', 1}, {'+', 2},{'-', 2}, {'~', 3}
    };
    vector<string>  getRPN(string s){
        vector<string> result;
        vector<char> ops;
        bool expected_value = true;
        for(int i = 0; i < s.size(); i++){
            string d;
            while(i< s.size() && isdigit(s[i])){
               d.push_back(s[i]);
                i++;
            }
           
            if(d.size()) {result.push_back(d);expected_value = false;}
            if(s[i] == '('){ 
                expected_value = true;
                ops.push_back(s[i]);continue;
            }
            if(i < s.size() && mp.count(s[i])){
                while(ops.size() && mp[s[i]] <= mp[ops.back()]){
                    result.push_back(string(1,ops.back()));
                    ops.pop_back();
                }
                //cout<<s[i]<<endl;
                if(expected_value){
                    if(s[i] == '-')
                        ops.push_back('~');
                }else
                    ops.push_back(s[i]);
                expected_value = true;
            }
            if(i < s.size() && s[i] == ')'){
                while(ops.size() && ops.back() != '('){
                    
                    result.push_back(string(1,ops.back()));
                    ops.pop_back();
                }
                //cout<<ops.back();
                ops.pop_back();
            }
        }
        
        while(ops.size()){
            result.push_back(string(1,ops.back()));
            ops.pop_back();
        }
        return result;
    }
    int apply(int a, int b, string op){
        if(op == "+") return a+b;
        else if(op == "-") return a-b;
        else if(op == "/") return a/b;
        else if(op == "*") return a*b;
        return 0;
    }
public:
    int calculate(string s) {
        vector<string> result = getRPN(s);
        for(auto str: result)cout<<str<<endl;
        vector<int> values;
        for(int i = 0; i < result.size(); i++){
            if(mp.count(result[i][0])){
                
                int b = values.back(); values.pop_back();
                if(result[i] == "~"){
                    values.push_back(-b);
                }else{
                    int a = values.back(); values.pop_back();
                    values.push_back(apply(a, b, result[i]));
                }
            }else{
                values.push_back(stoi(result[i]));
            }
        }
        return values.back();
    }
};
