class Solution {
public:
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        std::stack<TreeNode*> stack;
        stack.push(root);

        while (!stack.empty()) {
            TreeNode* cur = stack.top();
            if (cur == nullptr) {stack.pop(); continue;}

            if (helper(cur, subRoot)) {
                return true;
            }
            stack.pop();
            stack.push(cur->left);
            stack.push(cur->right);
        }

        return false;
    }

    bool helper(TreeNode* node, TreeNode* subRoot) {
        if (node == nullptr && subRoot == nullptr) return true;
        if ((node == nullptr && subRoot != nullptr) ||
            (node != nullptr && subRoot == nullptr)) return false;

        return (
            (node->val == subRoot->val) &&
            helper(node->left, subRoot->left) &&
            helper(node->right, subRoot->right)
        );
    }
};
