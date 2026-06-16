class Solution {
public:
    bool same = true;

    bool isSameTree(TreeNode* p, TreeNode* q) {
      helper(p, q);
      return same;
    }

    void helper(TreeNode* p, TreeNode* q) {
      if (p == nullptr and q == nullptr) return;
      else if (p == nullptr) goto notSame;
      else if (q == nullptr) goto notSame;
      else if (p->val != q->val) goto notSame;

      helper(p->left, q->left);
      helper(p->right, q->right);
      return;

      notSame:
        same = false;
        return;
    }
};
