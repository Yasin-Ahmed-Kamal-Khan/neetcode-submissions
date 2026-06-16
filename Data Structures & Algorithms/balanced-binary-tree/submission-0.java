class Solution {
    boolean balanced = true;
    Map<TreeNode, Integer> map = new HashMap<>();

    public boolean isBalanced(TreeNode root) {
      map.put(null, 0);
      helper(root);

      return balanced;
    }

    private void helper(TreeNode node) {
      if (node == null) return;
      if (!map.containsKey(node.left)) {
        helper(node.left);
      }
      if (!map.containsKey(node.right)) {
        helper(node.right);
      }
      int leftHeight = map.get(node.left);
      int rightHeight = map.get(node.right);

      map.put(node, 1 + Math.max(leftHeight, rightHeight));

      if (Math.abs(leftHeight - rightHeight) > 1) {
        balanced = false;
      }
    }
}
