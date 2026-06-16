
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
      std::stack<TreeNode*> pStack;
      std::stack<TreeNode*> qStack;

      findNode(root, p, pStack);
      findNode(root, q, qStack);

      while (pStack.size() != qStack.size()) {
        if (pStack.size() > qStack.size()) pStack.pop();
        else qStack.pop();
      }

      while (pStack.top()->val != qStack.top()->val) {
        pStack.pop(); qStack.pop();
      }

      return pStack.top();
    }


    bool findNode(TreeNode* root, TreeNode* p, std::stack<TreeNode*>& stack) {
      stack.push(root);
      if (!root) {stack.pop(); return false;}

      if (root->val == p->val) return true;

      if (findNode(root->left, p, stack)) return true;
      if (findNode(root->right, p, stack)) return true;
      stack.pop();
      return false;
    }

};
