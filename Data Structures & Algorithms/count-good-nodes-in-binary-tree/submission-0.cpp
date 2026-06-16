
class Solution {
public:
    int total = 0;

    int goodNodes(TreeNode* root) {
      helper(root, root->val);

      return total;
    }

    void helper(TreeNode* node, int maxSoFar) {
      if (!node) return;
      if (node->val >= maxSoFar) {
        total++;
        maxSoFar = node->val;
      }

      helper(node->right, maxSoFar);
      helper(node->left, maxSoFar);
    }
};
