class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        TreeNode cur = root;
        List<Integer> list = new LinkedList<>();
        Stack<Pair> stack = new Stack<>();
        int curDepth = 0;
        int maxDepth = 0;

        while (!stack.isEmpty() || cur != null) {
            if (cur == null) {
                Pair curPair = stack.pop();
                curDepth = curPair.depth;
                cur = curPair.node;
            }

            if (cur.left != null) stack.add(new Pair(cur.left, curDepth + 1));

            if (curDepth == maxDepth) {
                list.add(cur.val);
                maxDepth++;
            }

            curDepth++;
            cur = cur.right;
        }

        return list;
    }
}

class Pair {
    Pair(TreeNode node, int depth) {
        this.node = node; this.depth = depth;
    }

    TreeNode node;
    int depth;
}