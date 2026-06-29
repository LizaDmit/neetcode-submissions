class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        int l = nums.size();
        if (l == 0 || l == 1) {
            return false;}
        std::sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size() - 1; ++i) {
            if (nums[i] == nums[i+1]) {
                return true;}}
       return false; 
    }
};