class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
      List<List<Integer>> bigList = new LinkedList<>();

      Queue<TreeNode> nextLevel = new ArrayDeque<>();
      Queue<TreeNode> currentLevel = new ArrayDeque<>();

      List<Integer> list = new LinkedList<>();
      if (root == null) return bigList;

      currentLevel.add(root);

      while (!nextLevel.isEmpty() || !currentLevel.isEmpty()) {
        if (currentLevel.isEmpty()) {
          bigList.add(list);
          list = new LinkedList<>();
          currentLevel = nextLevel;
          nextLevel = new ArrayDeque<>();
        }

        TreeNode cur = currentLevel.remove();
        if (cur == null) continue;

        list.add(cur.val);
        if (cur.left != null) nextLevel.add(cur.left);
        if (cur.right != null) nextLevel.add(cur.right);
      }

      if (list != null) bigList.add(list);
      return bigList;
    }
}
