//Worst-case performance	Θ(m) preprocessing + Θ(n) matching[note 1]
//Worst-case space complexity	Θ(m)
//
vector<int> build_pattern(){
  vector<int> dp(token.size(), 0);
  int j = 0;
  for(int i = 1; i < token.size();){
      if(token[i] == token[j]){
          dp[i] = dp[j]+1;
          j++; i++;
      }else{

          if(j != 0){
             j = dp[j-1];
          }else{
              dp[i] = 0;
              i++;
          }
      }

  }
  return dp;
}

bool KMP(string &s, string token){
        
    auto dp = build_pattern(token);
    j = 0;
    for(int i = 0; i < s.size();){
        if(s[i] == token[j]){ j++;i++;}
        else {
            if(j != 0)
                j = dp[j-1];
            else i++;
        }
        if(j == token.size()) return true;
    }
    return false;
}
