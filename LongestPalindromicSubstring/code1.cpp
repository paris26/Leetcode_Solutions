class Solution {
public:
    int expandAroundCenter(string s, int left, int right){
        while(left >= 0 && right < s.size() && s[left] == s[right]){
            left--;
            right++;
        }
        return (right-left-1);
    }
    string longestPalindrome(string s) {
        if(s.empty()) return "";

        pair<int, int> res={0,1};
        int len1, len2;

        for(int i=0; i<s.size(); i++){

            len1 = expandAroundCenter(s, i, i);
            len2 = expandAroundCenter(s, i, i+1);

            if(len1>len2 && res.second < len1){
                 res = {i - (len1-1)/2, len1};
            }else if( res.second < len2){
                res = {i - (len2-1)/2, len2};
            }
        }
        return s.substr(res.first, res.second);
    }
};
