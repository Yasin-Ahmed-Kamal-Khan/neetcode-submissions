class Solution {
    public int goodNodes(TreeNode root) {
      int total = 0;
      Stack<Pair> stack = new Stack<>();
      stack.add(new Pair(root, root.val));

      while (!stack.isEmpty()) {
        var cur = stack.pop();

        if (cur.node.val >= cur.maxSoFar) {
          total++;
          if (cur.node.left != null)
            stack.add(new Pair(cur.node.left, cur.node.val));

          if (cur.node.right != null)
            stack.add(new Pair(cur.node.right, cur.node.val));

        } else {
          if (cur.node.left != null)
            stack.add(new Pair(cur.node.left, cur.maxSoFar));

          if (cur.node.right != null)
            stack.add(new Pair(cur.node.right, cur.maxSoFar));
        }
      }

      return total;
    }
}

class Pair {

  TreeNode node;
  int maxSoFar;

  Pair(TreeNode node, int maxSoFar) {
    this.node = node; this.maxSoFar = maxSoFar;
  }

}