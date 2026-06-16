class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> numSet = unordered_set<int>();
        for (int num : nums) {
            if (numSet.find(num) == numSet.end()) {
                numSet.insert(num);
            } else return true;
        }
        return false;
    }
};
