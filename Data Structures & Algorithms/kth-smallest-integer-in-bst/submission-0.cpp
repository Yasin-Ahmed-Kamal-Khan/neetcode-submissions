class Solution {
public:
    int counter;
    int val;
    bool done = false;

    int kthSmallest(TreeNode* root, int k) {
      counter = k;
      helper(root);

      return val;
    }

    void helper(TreeNode* node) {
      if (!node) return;

      helper(node->left);
      counter--;
      if (done) return;

      if (counter == 0) {
        val = node->val;
        done = true;
      }

      helper(node->right);
    }
};
