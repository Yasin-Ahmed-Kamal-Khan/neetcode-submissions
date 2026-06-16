class Solution {
    public int diameterOfBinaryTree(TreeNode root) {
      Stack<TreeNode> stack = new Stack<>();
      Map<TreeNode, int[]> map = new HashMap<>();
      map.put(null, new int[] {0, 0});
      stack.push(root);

      while (!stack.empty()) {
        var current = stack.peek();

        if (!map.containsKey(current.left) && current.left != null) {
          stack.push(current.left);
        } else if (!map.containsKey(current.right) && current.right != null) {
          stack.push(current.right);
        } else {
          var leftPair = map.get(current.left);
          var rightPair = map.get(current.right);

          int height = Math.max(leftPair[0], rightPair[0]) + 1;
          int width = Math.max(
            Math.max(leftPair[1], rightPair[1]),
            leftPair[0] + rightPair[0]
          );

          map.put(current, new int[] {height, width});
          stack.pop();
        }
      }



      return map.get(root)[1];
    }
}
