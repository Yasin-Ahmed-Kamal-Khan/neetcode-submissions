class Solution {
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
      return helper(root, subRoot);
    }

    private boolean helper(TreeNode node, TreeNode subRoot) {
      if (node == null) return false;

      if (!helperHelper(node, subRoot)) {
        return (helper(node.left, subRoot) || helper(node.right, subRoot));
      }

      return true;
    }

    private boolean helperHelper(TreeNode node, TreeNode subRoot) {
      if (node == null && subRoot != null) return false;
      if (node != null && subRoot == null) return false;
      if (node == null && subRoot == null) return true;

      if (node.val == subRoot.val)
        return (
          helperHelper(node.left, subRoot.left) &&
          helperHelper(node.right, subRoot.right)
        );
      return false;
    }
}
