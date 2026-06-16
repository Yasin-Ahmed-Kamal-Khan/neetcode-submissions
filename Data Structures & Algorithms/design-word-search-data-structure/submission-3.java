
class WordDictionary {
    Node head = new Node();
    String word;

    public WordDictionary() {

    }

    public void addWord(String word) {
      var cur = head;
      for (char c : word.toCharArray()) {
        cur.addChar(c);
        cur = cur.nextChar(c);
      }
      cur.end = true;
    }

    public boolean search(String word) {
      this.word = word;
      return helper(0, head);
    }

    private boolean helper(int num, Node node) {
      if (num == word.length() && node.end) {
        return true;
      }
      if (num >= word.length()) return false;

      char c = word.charAt(num);
      if (c == '.') {
        for (Node n : node.getAllChildren()) {
          if (helper(num + 1, n)) return true;
        }
        return false;
      }

      if (node.containsChar(c)) {
        return helper(num + 1, node.nextChar(c));
      }

      return false;
    }
}

class Node {
  Map<Character, Node> children =  new HashMap<>();
  boolean end = false;

  boolean containsChar(char c) {
    return children.containsKey(c);
  }

  Node nextChar(char c) {
    return children.get(c);
  }

  Collection<Node> getAllChildren() {
    return children.values();
  }

  void addChar(char c) {
    if (!children.containsKey(c))
      children.put(c, new Node());
  }
}