
class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
      auto pair = helperDistance(root);
      std::cout << pair.first << pair.second << std::endl;
      return (pair.first > pair.second) ? pair.first : pair.second;
    }

    std::pair<int,int> helperDistance(TreeNode* node) {
      std::pair left = std::pair(0,0);
      std::pair right = std::pair(0,0);

      if (node->left != nullptr) {
        left = helperDistance(node->left);
        left.first++;
      }

      if (node->right != nullptr) {
        right = helperDistance(node->right);
        right.first++;
      }

      int maxDepth = (left.first > right.first) ? left.first : right.first;
      int maxWidth = (left.second > right.second) ? left.second : right.second;
      maxWidth = (maxWidth > left.first + right.first) ? maxWidth : left.first + right.first;


      return std::pair(
        maxDepth,
        maxWidth
      );
    }
};
