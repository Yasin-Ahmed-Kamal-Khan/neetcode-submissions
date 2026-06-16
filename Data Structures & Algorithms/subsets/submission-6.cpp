class Solution {
public:
    vector<vector<int>> result;
    vector<int> nums;

    vector<vector<int>> subsets(vector<int>& nums) {
      this->nums = nums;
      vector<int> subset;

      dfs(0, subset);

      return result;
    }

    void dfs(int index, vector<int>& subset) {
      if (index >= nums.size()) {
        result.push_back(subset);
        return;
      }

      subset.push_back(nums[index]);
      dfs(index + 1, subset);
      subset.pop_back();
      dfs(index + 1, subset);
    }
};
