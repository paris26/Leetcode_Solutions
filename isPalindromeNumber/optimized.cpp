class Solution {
public:
    bool isPalindrome(int x) {
        // Handle edge cases with an extra early check for single digit
        if(x >= 0 && x <= 9) return true;  // Early return for single digits
        if(x < 0 || (x % 10 == 0)) return false;
        
        int reversed_half = 0;
        while(x > reversed_half){
            reversed_half = reversed_half * 10 + x % 10;
            if(x == reversed_half) return true;  // Early exit for even length
            x /= 10;
            if(x == reversed_half) return true;  // Early exit for odd length
        }
        return false;
    }
};
