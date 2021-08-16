//"3+2*2"
 // st [3,22]
 // st[+*]

class Solution {
    unordered_map<char, int> mp{
        {'*', 5},
        {'/', 5},
        {'+', 3},
        {'-', 3}
    };
    bool greater(char a, char b){
        return mp[a] >= mp[b]; 
    }
    int apply(int a, int b, char op){
        cout<<a<<":"<<b<<":"<<op<<endl;
        switch(op){
            case '*':
                return a*b;
            case '/':
                return a/b;
            case '+':
                return a+b;
            case '-':
                return a-b;
        }
        return -1;
    }
public:
    int calculate(string s) {
        stack<char> ops;
        stack<int> numbers;
        int i = 0; 
        int result = 0;
        while(i < s.size()){
            if(isspace(s[i]) == false){
               
               if(isdigit(s[i])){
                    int digit = 0;
                    while(isdigit(s[i])){
                        digit = digit*10+ (s[i]-'0');
                        i++;
                    }
                    numbers.push(digit);
                    continue;
                }
                else{ //operators
                    cout<<s[i]<<endl;
                    while(ops.size() && greater(ops.top(), s[i])){
                        int b= numbers.top();
                        numbers.pop();
                        int a = numbers.top();
                        numbers.pop();
                        int tmp = apply(a, b, ops.top());
                        numbers.push(tmp);
                        ops.pop();
                    }
                    ops.push(s[i]);
                }
            }
            
            i++;
        }
       
        while(ops.size() && numbers.size()){
                    int b= numbers.top();
                    numbers.pop();
                    int a = numbers.top();
                    numbers.pop();
                    int tmp = apply(a, b, ops.top());
                    numbers.push(tmp);
                    ops.pop();
        }
        return numbers.top();
    }
};
