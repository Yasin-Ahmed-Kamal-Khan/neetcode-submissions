class Solution {
    public int maxDepth(TreeNode root) {
      return maxDepthHelper(root, 0);

    }

    private int maxDepthHelper(TreeNode node, int depth) {
      if (node == null) return depth;

      int newDepth = depth + 1;
      int left = maxDepthHelper(node.left, newDepth);
      int right = maxDepthHelper(node.right, newDepth);

      return (right > left) ? right : left;
    }
}
