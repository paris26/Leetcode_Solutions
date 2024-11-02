#include <vector>
#include <iostream>
#include <unordered_map>
using namespace std;


class Solution {
    public: 
        vector<int> twoSum(vector<int>& nums, int target){
            unordered_map<int, int> map;
            int complement;
            int n = nums.size();

            for(int i =0; i<n; i++){
                complement = target - nums[i];

                if(map.find(complement) != map.end()){
                    return {map[complement], i};
                }

                map[nums[i]] = i;
            }
            return {};
        }
};