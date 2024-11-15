class Solution {
public:
    bool isPalindrome(int x) {
        // Handle edge cases
        if(x < 0 || (x != 0 && x % 10 == 0)) return false;
        
        int reversed_half = 0;
        while(x > reversed_half){
            int last_digit = x % 10;
            reversed_half = reversed_half * 10 + last_digit;
            x = x / 10;
        }
        
        return x == reversed_half || x == reversed_half/10;
    }
};
