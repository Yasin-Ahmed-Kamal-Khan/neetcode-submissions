class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
      Stack<TreeNode> stackP = new Stack<>();
      Stack<TreeNode> stackQ = new Stack<>();

      stackP.push(p);
      stackQ.push(q);

      while (!stackP.empty()) {
        TreeNode curQ = stackQ.pop();
        TreeNode curP = stackP.pop();
        if (curP != null && curQ == null) return false;
        if (curP == null && curQ != null) return false;
        if (curP != null && curQ != null) {
          if (curP.val != curQ.val) {
            return false;
          }
          stackP.push(curP.left);
          stackQ.push(curQ.left);
          stackP.push(curP.right);
          stackQ.push(curQ.right);
        }
      }
      return true;
    }
}

