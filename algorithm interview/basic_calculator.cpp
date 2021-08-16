// https://leetcode.com/problems/basic-calculator-iii/
// calculate("2*(5+5*2)/3+(6/2+8)")
int calculate(string s) {
        int i = 0;
        return parse(i, s);
    }
    int getDigit(int &i, string &s){
        int digit = 0;
            if(isdigit(s[i])){
                 digit = s[i]- '0';
                while(i+1 < s.size() && isdigit(s[i+1])){

                    digit = digit*10 + (s[i+1]- '0');
                    i++;
                }
            }
            
            return digit;
        
    }
    int parse(int &i, string &s){
        vector<int> nums;
        char op = '+';int a;
        for(; i < s.size() && s[i] != ')'; i++){
            if(isspace(s[i])) continue;
            int d = s[i] == '(' ? parse(++i, s) : getDigit(i, s);
           
            switch(op){
                case '+': nums.push_back(d);break;
                case '-': nums.push_back(-d);break;
                case '*': nums.back() *= d;break;
                case '/': nums.back() /= d;break;
            }
           
                op = s[i];
            //cout<<op<<endl;
            //else op = '+';
            
            
        }
        //i++;
        return accumulate(nums.begin(), nums.end(), 0);
    }
