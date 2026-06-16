class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
      std::unordered_map<TreeNode*, std::pair<int, int>> map;
      map.insert({nullptr, {0, 0}});
      std::stack<TreeNode*> stack;

      stack.push(root);

      while (!stack.empty()) {
        auto current = stack.top();

        if (current->left != nullptr && map.find(current->left) == map.end()) {
          stack.push(current->left);
        } else if (current->right != nullptr && map.find(current->right) == map.end()) {
          stack.push(current->right);
        } else {
          current = stack.top();
          stack.pop();
          auto leftPair = map[current->left];
          auto rightPair = map[current->right];
          int height = 1 + std::max(leftPair.first, rightPair.first);
          int diameter = std::max(
            leftPair.first + rightPair.first,
            std::max(
              leftPair.second, rightPair.second
            )
          );

          map.insert({current, {height, diameter}});
        }
      }

      return map[root].second;
    }
};
