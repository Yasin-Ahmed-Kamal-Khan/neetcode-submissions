class Solution {
public:
    bool isBalanced(TreeNode* root) {
      bool balanced = true;
      std::unordered_map<TreeNode*, int> map;
      std::stack<TreeNode*> stack;
      map.insert({nullptr, 0});
      stack.push(root);


      while (!stack.empty()) {
        TreeNode* current = stack.top();
        if (current == nullptr) {stack.pop(); continue;}
        if (map.find(current->left) == map.end()) {
          stack.push(current->left);
        } else if (map.find(current->right) == map.end()) {
          stack.push(current->right);
        } else {
          int leftHeight = map.at(current->left);
          int rightHeight = map.at(current->right);

          if (std::abs(rightHeight - leftHeight) > 1) balanced = false;

          map.insert({current, std::max(rightHeight, leftHeight) + 1});
          stack.pop();
        }
      }

      return balanced;
    }
};
