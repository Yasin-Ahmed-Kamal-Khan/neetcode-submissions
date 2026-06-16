class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        std::vector<int> res;
        std::queue<TreeNode*> queue;

        if (!root) return res;

        queue.push(root);

        while (!queue.empty()) {
            int elemsOnThisLevel = queue.size();
            for (int i = 0; i < elemsOnThisLevel - 1; i++) {
                auto cur = queue.front();
                queue.pop();

                if (cur->left) queue.push(cur->left);
                if (cur->right) queue.push(cur->right);
            }

            auto cur = queue.front();
            res.push_back(cur->val);
            queue.pop();

            if (cur->left) queue.push(cur->left);
            if (cur->right) queue.push(cur->right);
        }

        return res;
    }
};
