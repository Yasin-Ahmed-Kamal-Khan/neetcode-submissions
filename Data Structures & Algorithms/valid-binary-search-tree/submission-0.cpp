
class Solution {
public:
    bool isValidBST(TreeNode* root) {
      return
        helper(root->left, root->val, std::numeric_limits<int>::min()) &&
        helper(root->right, std::numeric_limits<int>::max(), root->val);
    }

    bool helper(TreeNode* node, int biggest, int smallest) {
      if (!node) return true;

      if (node->val >= biggest || node->val <= smallest) return false;

      bool leftValid;
      if (!node->left) leftValid = true;
      else leftValid = helper(node->left, node->val, smallest);

      bool rightValid;
      if (!node->right) rightValid = true;
      else rightValid = helper(node->right, biggest, node->val);

      return leftValid && rightValid;
    }
};
